"""
Constants that are used throughout the project.
"""

import logging
from datetime import datetime

from src.utils import project_root, Path


# DATE
DATE_TODAY = datetime.today().strftime('%Y_%m_%d')
DATETIME_NOW = datetime.now().strftime("%Y%m%d_%H%M")


# FOR LOGGER ONLY
LOG_TIME = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

FORMATTER = logging.Formatter(f'{LOG_TIME} :: %(name)s :: %(levelname)s :: %(funcName)s :: %(message)s')
# PROJECT_ROOT = Path(__file__).cwd()
PROJECT_ROOT = project_root(Path(__file__).resolve().parent, '.gitignore')
PATH_TO_LOGS = PROJECT_ROOT / 'logs'
# PATH_TO_LOGS = Path(__file__).cwd()
# LOG_FILE = PATH_TO_LOGS / 'logs/' / ("app_logger_" + datetime.today().strftime("%Y%m%d") + ".log")
LOG_FILE = PATH_TO_LOGS / ("app_logger_" + datetime.today().strftime("%Y%m%d") + ".log")


# DATABASE INITIALIZATION
INIT_DB = project_root(Path(__file__).resolve().parent, '.gitignore') / 'sql/init.sql'

# PG_DUMP FOR BACKUP FUNCTIONALITY
# PG_DUMP = r'C:\Program Files\PostgreSQL\16\bin\pg_dump.exe'
PG_DUMP = 'pg_dump'


# PATHS TO DATA AND FILES
PATH_TO_DATA_STORAGE = project_root(Path(__file__).resolve().parent, '.gitignore') / 'src/data'

# BACKUPS LOCATION
PATH_TO_BACKUPS = project_root(Path(__file__).resolve().parent, '.gitignore') / 'backups'
BACKUP_FOLDER_TODAY = PATH_TO_BACKUPS / f"backup_{DATE_TODAY}"

# BACKUP FOLDERS FOR DATABASE
DB_BACKUP_FILE = BACKUP_FOLDER_TODAY / f"db_backup_{DATETIME_NOW}.sql"


# DATAFRAME SCHEMAS

