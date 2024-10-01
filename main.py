from src.db_functions.db_connection import DatabaseConnection
from src.db_functions.db_tables import *
from src.db_functions.db_operations import *
from src.staging.data_staging import *

import src.logger as log
from src.utils import get_files_in_directory
from src.constants import PATH_TO_DATA_STORAGE


def run_spark_session():
    try:
        with SparkSessionManager() as spark:
            csv_files = get_files_in_directory(PATH_TO_DATA_STORAGE)
            for csv_file in csv_files:
                schema_name = schema_select(csv_file)
                if schema_name:
                    try:
                        df = create_dataframe(spark, csv_file, schema_name)
                        df = add_timestamp(df)
                        df.show(5)
                    except PySparkException as err:
                        staging_logger.warning('Error while processing file "%s": %s', csv_files, err, exc_info=True)
                else:
                    staging_logger.warning('Skipping file "%s" processing due to missing schema', csv_file)
    except PySparkException as err:
        staging_logger.error('Spark Error: %s', err, exc_info=True)


def run_db_operations():
        try:
            with DatabaseConnection() as dc:
                if dc is not None:
                    create_tables(dc)
                    tables = get_tables_in_db(dc)
                    table_count = len(tables)
                    db_logger.info(f'\nFound %s table{"s" if table_count != 1 else ""} in a database:\n'
                                   '%s', table_count, tables)
        except SQLAlchemyError as e:
            db_logger.error('An error occurred while creating tables: %s', e, exc_info=True)


