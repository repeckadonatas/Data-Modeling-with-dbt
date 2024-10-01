"""
Constants that are used throughout the project.
"""

import logging
from datetime import datetime

from pyspark.sql.types import (StructType, StructField, StringType, IntegerType,
                               DoubleType, DateType)

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
PATH_TO_DATA_STORAGE = project_root(Path(__file__).resolve().parent, '.gitignore') / 'src' / 'input'


# BACKUPS LOCATION
PATH_TO_BACKUPS = project_root(Path(__file__).resolve().parent, '.gitignore') / 'backups'
BACKUP_FOLDER_TODAY = PATH_TO_BACKUPS / f"backup_{DATE_TODAY}"


# BACKUP FOLDERS FOR DATABASE
DB_BACKUP_FILE = BACKUP_FOLDER_TODAY / f"db_backup_{DATETIME_NOW}.sql"


# DATAFRAME SCHEMAS
CIRCUITS_SCHEMA = StructType(
    [
        StructField('circuit_id', IntegerType(), False),
        StructField('circuit_ref', StringType(), True),
        StructField('circuit_name', StringType(), True),
        StructField('circuit_location', StringType(), True),
        StructField('country', StringType(), True),
        StructField('latitude', DoubleType(), True),
        StructField('longitude', DoubleType(), True),
        StructField('altitude', IntegerType(), True),
        StructField('circuit_url', StringType(), True)
    ]
)

CONSTRUCTOR_RESULTS_SCHEMA = StructType(
    [
        StructField('constructor_results_id', IntegerType(), False),
        StructField('race_id', IntegerType(), False),
        StructField('constructor_id', IntegerType(), False),
        StructField('points', DoubleType(), True),
        StructField('status', StringType(), True),
    ]
)

CONSTRUCTOR_STANDINGS_SCHEMA = StructType(
    [
        StructField('constructor_standings_id', IntegerType(), False),
        StructField('race_id', IntegerType(), False),
        StructField('constructor_id', IntegerType(), False),
        StructField('constructor_points', DoubleType(), True),
        StructField('constructor_position', IntegerType(), True),
        StructField('position_text', IntegerType(), True),
        StructField('constructor_wins', IntegerType(), False),
    ]
)

CONSTRUCTORS_SCHEMA = StructType(
    [
        StructField('constructor_id', IntegerType(), False),
        StructField('constructor_ref', StringType(), True),
        StructField('constructor_name', StringType(), True),
        StructField('constructor_nationality', StringType(), True),
        StructField('constructor_url', StringType(), True)
    ]
)

DRIVER_STANDINGS_SCHEMA = StructType(
    [
        StructField('driver_standings_id', IntegerType(), False),
        StructField('race_id', IntegerType(), False),
        StructField('driver_id', IntegerType(), False),
        StructField('driver_points', DoubleType(), True),
        StructField('driver_position', IntegerType(), True),
        StructField('position_text', IntegerType(), True),
        StructField('driver_wins', IntegerType(), False),
    ]
)

DRIVERS_SCHEMA = StructType(
    [
        StructField('driver_id', IntegerType(), False),
        StructField('driver_ref', StringType(), True),
        StructField('driver_number', IntegerType(), True),
        StructField('driver_code', StringType(), True),
        StructField('first_name', StringType(), True),
        StructField('last_name', StringType(), True),
        StructField('date_of_birth', DateType(), True),
        StructField('driver_nationality', StringType(), True),
        StructField('driver_url', StringType(), True),
    ]
)

LAP_TIMES_SCHEMA = StructType(
    [
        StructField('race_id', IntegerType(), False),
        StructField('driver_id', IntegerType(), False),
        StructField('lap', IntegerType(), False),
        StructField('driver_position', IntegerType(), True),
        StructField('lap_time', StringType(), True),
        StructField('milliseconds', IntegerType(), True)
    ]
)

PIT_STOPS_SCHEMA = StructType(
    [
        StructField('race_id', IntegerType(), False),
        StructField('driver_id', IntegerType(), False),
        StructField('pit_stop_number', IntegerType(), False),
        StructField('lap', IntegerType(), False),
        StructField('time_of_stop', StringType(), False),
        StructField('stop_duration', StringType(), True),
        StructField('milliseconds', IntegerType(), True)
    ]
)

QUALIFYING_SCHEMA = StructType(
    [
        StructField('qualify_id', IntegerType(), False),
        StructField('race_id', IntegerType(), False),
        StructField('driver_id', IntegerType(), False),
        StructField('constructor_id', IntegerType(), False),
        StructField('driver_number', IntegerType(), False),
        StructField('qualify_position', IntegerType(), True),
        StructField('q1_lap_time', StringType(), True),
        StructField('q2_lap_time', StringType(), True),
        StructField('q3_lap_time', StringType(), True),
    ]
)

RACES_SCHEMA = StructType(
    [
        StructField('race_id', IntegerType(), False),
        StructField('race_year', IntegerType(), True),
        StructField('round', IntegerType(), True),
        StructField('circuit_id', StringType(), False),
        StructField('race_name', StringType(), True),
        StructField('race_date', DateType(), True),
        StructField('race_start_time', StringType(), True),
        StructField('race_url', StringType(), True),
        StructField('fp1_date', DateType(), True),
        StructField('fp1_time', StringType(), True),
        StructField('fp2_date', DateType(), True),
        StructField('fp2_time', StringType(), True),
        StructField('fp3_date', DateType(), True),
        StructField('fp3_time', StringType(), True),
        StructField('qualifying_date', DateType(), True),
        StructField('qualifying_start_time', StringType(), True),
        StructField('sprint_date', DateType(), True),
        StructField('sprint_start_time', StringType(), True)
    ]
)

RESULTS_SCHEMA = StructType(
    [
        StructField('result_id', IntegerType(), False),
        StructField('race_id', IntegerType(), False),
        StructField('driver_id', IntegerType(), False),
        StructField('constructor_id', IntegerType(), False),
        StructField('driver_number', IntegerType(), True),
        StructField('grid_position', IntegerType(), False),
        StructField('official_position', IntegerType(), True),
        StructField('position_text', StringType(), False),
        StructField('position_order', IntegerType(), False),
        StructField('driver_points', DoubleType(), True),
        StructField('laps_completed', IntegerType(), True),
        StructField('finish_time', StringType(), True),
        StructField('time_milliseconds', IntegerType(), True),
        StructField('fastest_lap', IntegerType(), True),
        StructField('fastest_lap_rank', IntegerType(), True),
        StructField('fastest_lap_time', StringType(), True),
        StructField('fastest_lap_speed', StringType(), True),
        StructField('status_id', IntegerType(), False)
    ]
)

SEASONS_SCHEMA = StructType(
    [
        StructField('year', IntegerType(), False),
        StructField('url', StringType(), False)
    ]
)

SPRINT_RESULTS_SCHEMA = StructType(
    [
        StructField('sprint_result_id', IntegerType(), False),
        StructField('race_id', IntegerType(), False),
        StructField('driver_id', IntegerType(), False),
        StructField('constructor_id', IntegerType(), False),
        StructField('driver_number', IntegerType(), True),
        StructField('grid_position', IntegerType(), False),
        StructField('official_position', IntegerType(), True),
        StructField('position_text', StringType(), False),
        StructField('position_order', IntegerType(), False),
        StructField('driver_points', DoubleType(), True),
        StructField('laps_completed', IntegerType(), True),
        StructField('finish_time', StringType(), True),
        StructField('time_milliseconds', IntegerType(), True),
        StructField('fastest_lap', IntegerType(), True),
        StructField('fastest_lap_time', StringType(), True),
        StructField('status_id', IntegerType(), False)
    ]
)

STATUS_SCHEMA = StructType(
    [
        StructField('status_id', IntegerType(), False),
        StructField('status', StringType(), False)
    ]
)

FILE_SCHEMA_DICT = {
    'circuits.csv':              ('CIRCUITS_SCHEMA', CIRCUITS_SCHEMA),
    'constructor_results.csv':   ('CONSTRUCTOR_RESULTS_SCHEMA', CONSTRUCTOR_RESULTS_SCHEMA),
    'constructor_standings.csv': ('CONSTRUCTOR_STANDINGS_SCHEMA', CONSTRUCTOR_STANDINGS_SCHEMA),
    'constructors.csv':          ('CONSTRUCTORS_SCHEMA', CONSTRUCTORS_SCHEMA),
    'driver_standings.csv':      ('DRIVER_STANDINGS_SCHEMA', DRIVER_STANDINGS_SCHEMA),
    'drivers.csv':               ('DRIVERS_SCHEMA', DRIVERS_SCHEMA),
    'lap_times.csv':             ('LAP_TIMES_SCHEMA', LAP_TIMES_SCHEMA),
    'pit_stops.csv':             ('PIT_STOPS_SCHEMA', PIT_STOPS_SCHEMA),
    'qualifying.csv':            ('QUALIFYING_SCHEMA', QUALIFYING_SCHEMA),
    'races.csv':                 ('RACES_SCHEMA', RACES_SCHEMA),
    'results.csv':               ('RESULTS_SCHEMA', RESULTS_SCHEMA),
    'seasons.csv':               ('SEASONS_SCHEMA', SEASONS_SCHEMA),
    'sprint_results.csv':        ('SPRINT_RESULTS_SCHEMA', SPRINT_RESULTS_SCHEMA),
    'status.csv':                ('STATUS_SCHEMA', STATUS_SCHEMA)
}


FILE_TABLE_MAP = {
    'circuits.csv': 'circuits',
    'constructor_results.csv': 'constructor_results',
    'constructor_standings.csv': 'constructor_standings',
    'constructors.csv': 'constructors',
    'driver_standings.csv': 'driver_standings',
    'drivers.csv': 'drivers',
    'lap_times.csv': 'lap_times',
    'pit_stops.csv': 'pit_stops',
    'qualifying.csv': 'qualifying',
    'races.csv': 'races',
    'results.csv': 'results',
    'seasons.csv': 'seasons',
    'sprint_results.csv': 'sprint_results',
    'status.csv': 'status'
}
