from sqlalchemy import Column, String, Float, Integer, DateTime
from sqlalchemy import ForeignKey
from sqlalchemy.ext.declarative import declarative_base

import src.logger as log

tables_logger = log.app_logger(__name__)

Base = declarative_base()


# class StagingLayerTable(Base):
#     __tablename__ = 'staging_jobs_listings_data'
#     __table_args__ = {'schema': 'staging'}
#
#     id = Column(Integer, primary_key=True, autoincrement=True)
#     api_source = Column(String())
#     timestamp = Column(DateTime(timezone=True))
#     data = Column(JSONB())


class CircuitsTable(Base):
    __tablename__ = 'circuits'

    circuit_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    circuit_ref = Column(String(), nullable=False)
    circuit_name = Column(String(), nullable=False)
    circuit_location = Column(String(), default=None)
    country = Column(String(), default=None)
    latitude = Column(Float(), default=None)
    longitude = Column(Float(), default=None)
    altitude = Column(Integer(), default=None)
    circuit_url = Column(String(), nullable=False)
    timestamp = Column(DateTime(timezone=True))  # <- ADD TIMESTAMP FUNCTION!!!!


class ConstructorsTable(Base):
    __tablename__ = 'constructors'

    constructor_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    constructor_ref = Column(String(), nullable=False)
    constructor_name = Column(String(), nullable=False)
    constructor_nationality = Column(String(), default=None)
    constructor_url = Column(String(), nullable=False)
    timestamp = Column(DateTime(timezone=True))


class ConstructorResultsTable(Base):
    __tablename__ = 'constructor_results'

    constructor_result_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    constructor_id = Column(Integer(), ForeignKey('constructors.constructor_id'), nullable=False)
    points = Column(Float(), default=None)
    status = Column(String(), default=None)
    timestamp = Column(DateTime(timezone=True))


class ConstructorStandingsTable(Base):
    __tablename__ = 'constructor_standings'

    constructor_standings_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    constructor_id = Column(Integer(), ForeignKey('constructors.constructor_id'), nullable=False)
    constructor_points = Column(Float(), default=None)
    constructor_position = Column(Integer(), default=None)
    position_text = Column(String(), default=None)
    constructor_wins = Column(Integer(), nullable=False, default=0)
    timestamp = Column(DateTime(timezone=True))


class DriversTable(Base):
    __tablename__ = 'drivers'

    driver_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    driver_ref = Column(String(), nullable=False)
    driver_number = Column(Integer(), default=None)
    driver_code = Column(String(), default=None)
    first_name = Column(String(), nullable=False)
    last_name = Column(String(), nullable=False)
    date_of_birth = Column(DateTime(), default=None)
    driver_nationality = Column(String(), default=None)
    driver_url = Column(String(), nullable=False)
    timestamp = Column(DateTime(timezone=True))


class DriverStandingsTable(Base):
    __tablename__ = 'driver_standings'

    driver_standings_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.driver_id'), nullable=False)
    points = Column(Float(), default=0)
    position = Column(Integer(), default=None)
    position_text = Column(String(), default=None)
    wins = Column(Integer(), default=0)
    timestamp = Column(DateTime(timezone=True))


class LapTimesTable(Base):
    __tablename__ = 'lap_times'

    lap_times_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.driver_id'), nullable=False)
    lap = Column(Integer(), nullable=False, default=None)
    driver_position = Column(Integer(), default=None)
    lap_time = Column(String(), default=None)
    milliseconds = Column(Integer(), default=None)
    timestamp = Column(DateTime(timezone=True))


class PitStopsTable(Base):
    __tablename__ = 'pit_stops'

    pit_stops_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.driver_id'), nullable=False)
    pit_stop_number = Column(Integer(), nullable=False, default=None)
    lap_number = Column(Integer(), nullable=False, default=None)
    time_of_stop = Column(String(), nullable=False, default=None)
    stop_duration = Column(String(), default=None)
    milliseconds = Column(Integer(), default=None)
    timestamp = Column(DateTime(timezone=True))


class QualifyingTable(Base):
    __tablename__ = 'qualifying'

    qualify_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.driver_id'), nullable=False)
    constructor_id = Column(Integer(), ForeignKey('constructors.constructor_id'), nullable=False)
    driver_number = Column(Integer(), nullable=False, default=0)
    qualify_position = Column(Integer(), default=None)
    q1_lap_time = Column(String(), default=None)
    q2_lap_time = Column(String(), default=None)
    q3_lap_time = Column(String(), default=None)
    timestamp = Column(DateTime(timezone=True))


class RacesTable(Base):
    __tablename__ = 'races'

    race_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_year = Column(Integer(), ForeignKey('seasons.season_id'), nullable=False)    #TODO
    round = Column(Integer(), default=0)
    circuit_id = Column(Integer(), ForeignKey('circuits.circuit_id'), nullable=False)    #TODO
    race_name = Column(String(), nullable=False)
    race_date = Column(DateTime(), nullable=False, default=0000-00-0)
    race_start_time = Column(String())
    race_url = Column(String())
    fp1_date = Column(DateTime(), default=None)
    fp1_time = Column(String(), default=None)
    fp2_date = Column(DateTime(), default=None)
    fp2_time = Column(String(), default=None)
    fp3_date = Column(DateTime(), default=None)
    fp3_time = Column(String(), default=None)
    qualifying_date = Column(DateTime(), default=None)
    qualifying_start_time = Column(String(), default=None)
    sprint_date = Column(DateTime(), default=None)
    sprint_start_time = Column(String(), default=None)
    timestamp = Column(DateTime(timezone=True))


class ResultsTable(Base):
    __tablename__ = 'results'

    result_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.driver_id'), nullable=False)
    constructor_id = Column(Integer(), ForeignKey('constructors.constructor_id'), nullable=False)
    driver_number = Column(Integer(), default=0)
    grid_position = Column(Integer(), nullable=False, default=0)
    official_position = Column(Integer(), default=None)
    position_text = Column(String(), nullable=False, default=None)
    position_order = Column(Integer(), nullable=False, default=0)
    driver_points = Column(Float(), nullable=False, default=0)
    laps_completed = Column(Integer(), nullable=False, default=0)
    finish_time = Column(String(), default=None)
    milliseconds = Column(Integer(), default=None)
    fastest_lap = Column(Integer(), default=None)
    fastest_lap_rank = Column(Integer(), default=0)
    fastest_lap_time = Column(String(), default=None)
    fastest_lap_speed = Column(String(), default=None)
    status_id = Column(Integer(), ForeignKey('status.status_id'), nullable=False)
    timestamp = Column(DateTime(timezone=True))


class SprintResultsTable(Base):
    __tablename__ = 'sprint_results'

    sprint_result_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False)
    race_id = Column(Integer(), ForeignKey('races.race_id'), nullable=False)
    driver_id = Column(Integer(), ForeignKey('drivers.driver_id'), nullable=False)
    constructor_id = Column(Integer(), ForeignKey('constructors.constructor_id'), nullable=False)
    driver_number = Column(Integer(), default=None)
    grid_position = Column(Integer(), nullable=False, default=0)
    official_position = Column(Integer(), default=None)
    position_text = Column(String(), nullable=False, default=None)
    position_order = Column(Integer(), nullable=False, default=0)
    driver_points = Column(Float(), nullable=False, default=0)
    laps_completed = Column(Integer(), nullable=False, default=0)
    finish_time = Column(String(), default=None)
    milliseconds = Column(Integer(), default=None)
    fastest_lap = Column(Integer(), default=None)
    fastest_lap_time = Column(String(), default=None)
    status_id = Column(Integer(), ForeignKey('status.status_id'), nullable=False)
    timestamp = Column(DateTime(timezone=True))


class SeasonsTable(Base):
    __tablename__ = 'seasons'

    year = Column(Integer(), primary_key=True, nullable=False, default=0)
    season_url = Column(String(), nullable=False)
    timestamp = Column(DateTime(timezone=True))


class StatusTable(Base):
    __tablename__ = 'status'

    status_id = Column(Integer(), primary_key=True, autoincrement=True, nullable=False, default=None)
    status = Column(String(), nullable=False)
    timestamp = Column(DateTime(timezone=True))
