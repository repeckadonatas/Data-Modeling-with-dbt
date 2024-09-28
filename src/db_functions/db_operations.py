import sqlalchemy
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError, OperationalError, DBAPIError, DatabaseError, DisconnectionError

import src.db_functions.db_tables as db_tables
from src.db_functions.db_connection import db_logger, JobsDataDatabase


# class DataUpload(JobsDataDatabase):
#     """
#     Functions that determine the logic of data upload process.
#     """
#
#     def __init__(self):
#         super().__init__()

def create_tables(engine: sqlalchemy.engine) -> None:
    """
    Creates tables in a database if they do not exist.
    :param engine: SQLAlchemy database engine.
    """
    try:
        inspector = inspect(engine)

        for table in db_tables.Base.metadata.tables.values():
            table_name = table.name

            if not inspector.has_table(table_name):
                with engine.begin() as connection:
                    table.create(connection)
                db_logger.info('Table "%s" created successfully!', table_name)
            else:
                db_logger.info('Table "%s" already exists. Skipping creation.', table_name)

        print()
    except (OperationalError, DatabaseError, DisconnectionError, DBAPIError, AttributeError) as e:
        db_logger.error('An error occurred while creating tables: %s', e, exc_info=True)

def get_tables_in_db(engine: sqlalchemy.engine) -> list:
    """
    Returns a list of all the tables in the database.
    :param engine: SQLAlchemy database engine.
    :return: List of tables in the database.
    """
    inspect_db = inspect(engine)
    tables_list = []

    for table in inspect_db.get_table_names():
        tables_list.append(table)

    return tables_list

def load_to_database(engine: sqlalchemy.engine,
                     dataframe: pyspark.sql.DataFrame,
                     table_name: str) -> None:
    """
    Function to load the data of a dataframe to a specified table in the database.
    :param engine: SQLAlchemy database engine.
    :param dataframe: dataframe to load data from.
    :param table_name: table to load the data to.
    """
    try:
        dataframe.to_sql(table_name,
                         con=engine,
                         if_exists='replace',
                         index=False)

    except Exception as e:
        db_logger.error("An error occurred while loading the data: %s. "
                        "Rolling back the last transaction", e, exc_info=True)
        engine.rollback()
