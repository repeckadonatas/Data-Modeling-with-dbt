import pyspark
from sqlalchemy import inspect
from sqlalchemy.exc import SQLAlchemyError, OperationalError, DBAPIError, DatabaseError, DisconnectionError

import src.db_functions.db_tables as db_tables
from src.db_functions.db_connection import db_logger, DatabaseConnection


def create_tables(db_conn: DatabaseConnection) -> None:
    """
    Creates tables in a database if they do not exist.
    :param db_conn: SQLAlchemy database engine.
    """
    try:
        engine = db_conn.engine
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
    except (SQLAlchemyError, OperationalError, DatabaseError, DisconnectionError, DBAPIError, AttributeError) as e:
        db_logger.error('An error occurred while creating tables: %s', e, exc_info=True)


def get_tables_in_db(db_conn: DatabaseConnection) -> list:
    """
    Returns a list of all the tables in the database.
    :param db_conn: SQLAlchemy database engine.
    :return: List of tables in the database.
    """
    engine = db_conn.engine
    inspect_db = inspect(engine)
    get_tables = inspect_db.get_table_names()

    return get_tables


def load_to_database(db_conn: DatabaseConnection,
                     dataframe: pyspark.sql.DataFrame,
                     table_name: str) -> None:
    """
    Function to load the data of a dataframe to a specified table in the database.
    :param db_conn: SQLAlchemy database engine.
    :param dataframe: dataframe to load data from.
    :param table_name: table to load the data to.
    """
    try:
        engine = db_conn.engine
        jdbc_url = f'jdbc:postgresql://{engine.url.host}:{engine.url.port}/{engine.url.database}'

        properties = {
            "user": engine.url.username,
            "password": engine.url.password,
            "driver": "org.postgresql.Driver"
        }

        dataframe.write.jdbc(url=jdbc_url,
                             table=table_name,
                             mode="overwrite",
                             properties=properties)


    except (SQLAlchemyError, OperationalError, DatabaseError, DisconnectionError, DBAPIError, AttributeError) as e:
        db_logger.error("An error occurred while loading the data: %s. "
                        "Rolling back the last transaction", e, exc_info=True)
        engine.dispose()
