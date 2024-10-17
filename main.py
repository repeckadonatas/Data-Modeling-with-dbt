from threading import Event
from queue import Queue
import concurrent.futures
from concurrent.futures import CancelledError, TimeoutError, BrokenExecutor

from src.db_functions.db_operations import *
from src.staging.data_staging import *
from src.utils import get_files_in_directory
from src.constants import PATH_TO_DATA_STORAGE, FILE_TABLE_MAP

main_logger = log.app_logger(__name__)


def run_spark_session(queue: Queue,
                      event: Event,
                      spark: SparkSessionManager) -> None:
    try:
        while not event.is_set():
            csv_files = get_files_in_directory(PATH_TO_DATA_STORAGE)
            for csv_file in csv_files:
                schema_name = schema_select(csv_file)
                if schema_name:
                    df = create_dataframe(spark.spark, csv_file, schema_name)
                    df = add_timestamp(df)
                    queue.put([csv_file, df])
                    main_logger.info('A dataframe for file "%s" was put into queue', csv_file)
                else:
                    main_logger.warning('Skipping file "%s" processing due to missing schema', csv_file)

            event.set()
    except PySparkException as err:
        main_logger.error('Spark Error: %s', err, exc_info=True)


def run_db_operations(queue: Queue,
                      event: Event) -> None:
        try:
            with DatabaseConnection() as dc:
                main_logger.info('Preparing for data upload...')
                if dc is not None:
                    create_tables(dc)
                    tables = get_tables_in_db(dc)
                    table_count = len(tables)
                    main_logger.info(f'Found %s table{"s" if table_count != 1 else ""} in a database:\n'
                                   '%s', table_count, tables)

                    while not event.is_set() or not queue.empty():
                        main_logger.info('Getting data from queue...')
                        queue_items = queue.get(timeout=5)
                        if queue_items is None:
                            main_logger.warning('Queue is empty...')
                            break

                        file_name, dataframe = queue_items
                        if file_name in FILE_TABLE_MAP:
                            table_name, table = FILE_TABLE_MAP[file_name]
                            load_to_database(dc, dataframe, table_name)
                            main_logger.info('Dataframe "%s" loaded to table "%s" successfully!', file_name,
                                             table_name)
                        else:
                            main_logger.warning('Dataframe "%s" did not match table "%s"', file_name, table_name)
                            print(f'\n{table_name, table}\n')

        except SQLAlchemyError as e:
            main_logger.error('An error occurred: %s', e, exc_info=True)


if __name__ == '__main__':

    try:
        queue = Queue(maxsize=14)
        event = Event()
        spark = SparkSessionManager()
        with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
            tasks = [executor.submit(run_spark_session(queue, event, spark)),
                     executor.submit(run_db_operations(queue, event))]

            concurrent.futures.wait(tasks)

    except (CancelledError, TimeoutError, BrokenExecutor) as err:
        main_logger.error('An error occurred: %s\n', err, exc_info=True)
    finally:
        spark.__exit__(None, None, None)

    main_logger.info('Data upload complete.\n')