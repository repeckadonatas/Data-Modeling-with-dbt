import os
from datetime import datetime

import pyspark
from pyspark.sql.functions import lit
from dotenv import load_dotenv, find_dotenv


# REUSABLE FUNCTIONS
def env_config() -> os.environ:
    """
    Gets database connection credentials from .env file.
    :return: os.environ.
    """
    load_dotenv(find_dotenv('.env', usecwd=True))

    return os.environ


def read_dict(dict_name: dict) -> list:
    """
    Reads a dictionary to get the keys and values.
    :param dict_name: the name of a dictionary to read.
    :return: a list of key/value pairs.
    """
    return [(dict_key, dict_value) for dict_key, dict_value in dict_name.items()]


def get_files_in_directory(dir_path: str) -> list:
    """
    Reads files in a set directory.
    Returns a list of names of files in the directory
    to be iterated through.
    :param dir_path: path to a directory to read.
    :return: a list of file names in the directory.
    """
    files = os.scandir(dir_path)

    list_of_files = []
    for file in files:
        if file.is_dir() or file.is_file():
            list_of_files.append(file.name)
    return list_of_files


def remove_files_in_directory(dir_path: str) -> None:
    """
    Removes files in a set directory.
    :param dir_path: path to a directory.
    """
    files = os.scandir(dir_path)
    for file in files:
        os.remove(file)


def determine_table_name(file_name: str,
                         table_mapping: dict) -> (str | None):
    """
    To map the correct dataframe with the table to load the data to.
    The function is used to make sure that the data of a dataframe
    is loaded into a correct table in the database.
    Mapping logic is determined by a supplied table mapping dictionary.
    :param file_name: file name to determine the table name.
    :param table_mapping: a dictionary with dataframe names and matching table names.
    """
    file_name_lower = file_name.lower()
    for prefix, table in table_mapping.items():
        if file_name_lower.startswith(prefix.lower()):
            return table


def add_timestamp(dataframe: pyspark.sql.DataFrame) -> pyspark.sql.DataFrame:
    """
    Adds a timestamp to the dataframe.
    :param dataframe: a dataframe to add the timestamp to.
    :return: a dataframe with the timestamp added.
    """
    date_now = datetime.now()
    dataframe = dataframe.withColumn('timestamp', lit(date_now))

    return dataframe
