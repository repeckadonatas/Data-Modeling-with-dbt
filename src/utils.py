import os
from pathlib import Path

from dotenv import load_dotenv, find_dotenv


# PROJECT AGNOSTIC FUNCTIONS
def project_root(current_dir: Path,
                 root_dir_marker: str) -> Path:
    """
    Points the logger to the project root directory
    based on a specific marker located in the project's root directory.
    :param current_dir: directory to start the search from
    :param root_dir_marker: marker that indicates the root directory
    :return: path to the project's root directory
    """
    for parent in current_dir.resolve().parents:
        if (parent / root_dir_marker).exists():
            return parent
    return current_dir.resolve()


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
                         table_mapping: dict) -> tuple | None:      # SO FAR NOT VERY USEFUL...
    """
    To map the correct dataframe with the table to load the data to.
    The function is used to make sure that the data of a dataframe
    is loaded into a correct table in the database.
    Mapping logic is determined by a supplied table mapping dictionary.
    :param file_name: file name to determine the table name.
    :param table_mapping: a dictionary with dataframe names and matching table names.
    """
    file_name_lower = file_name.lower()
    for prefix, (table_name, table) in table_mapping.items():
        if file_name_lower.startswith(prefix.lower()):
            return table_name, table
    return None
