# Sales Data Modeling


## About

This project is an exercise in learning to use dbt (Data Build Tool) and learning how to apply dbt on an already existing database with well established structure. The project envelopes the use of Python, SQL, Docker, Spark and dbt.

The project uses **[Formula 1 World Championship (1950-2024)](https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020?select=circuits.csv)** dataset from Kaggle. The relevant data is stored as CSV files. As there is no need for periodic data ingestion the data is downloaded and stored locally. 

Although this project could have been done in an easier way, for this project I chose to use Spark to create dataframes and upload them to the database. The most challenging part was to properly create a stand-alone Spark cluster that will be running in a Docker container. \
This local Spark container had to be running all the time unless a `docker compose down -v` command was issued. Also, while the container was running it had to be accessible by Python code so that I could issue `spark submit` command to run a Spark job. This was achieved by using `volume` section in a Docker Compose file dedicated for running Spark jobs in a Spark container.

The same approach was used for dbt setup. For this project **dbt-core** was used. A custom Dockerfile for it was created and the connection to the container was made using `volume` section in a Docker Compose file that was dedicated for running dbt container.

Since there are multiple Docker, Spark and dbt commands that need to be issued, to make running these commands easier I utilised Makefile to create aliases for each command that can be used in this project.

The part of Python code used for running Spark job uses Threading as a concurrency method. Threading is suitable when looking to parallelize heavy I/O work, such as HTTP calls, reading from files and processing data. This also help tremendously in making sure that all the necessary tasks would run in a correct order of operations.


## Tech Stack Used

* Programing language - **Python**;
* Data storage and querying - **PostgreSQL**;
* Data cleaning and normalization - **Spark (PySpark)**;
* Package and dependency management - **Poetry**;
* Containerization - **Docker**;
* Data modeling on a database side - **dbt**


## Project Deliveries Plan

* **Database**:
  * For a database I chose PostgreSQL as it offers more features than some other databases (i.e. MySQL), it is free, easy-to-implement database management system and is better suited for enterprise-level applications.


* **Data preparation**: 
  * **PySpark** library is used to create dataframes from CSV files. The changes made to dataframes:
    * A custom schema is applied with proper data type casting;
    * A timestamp is added of when the data was uploaded;
    * Some columns are renamed to make more sense of data stored.


* **Data upload to a database**:
  * Once the data is prepared for uploading, datasets are first placed in a queue and after matching the datasets with the table in a database, the data is then uploaded to corresponding table.


* **Tables**:
  * The database contains multiple tables for data storage. 
  * For storing CSV data in a `public` layer:
    * `drivers`
    * `constructors`
    * `circuits`
    * `seasons`
    * `status`
    * `races`
    * `qualifying`
    * `results`
    * `driver_standings`
    * `sprint_results`
    * `lap_times`
    * `pit_stops`
    * `constructor_results`
    * `constructor_standings`
    * This data is also regarded as **raw** data in **dbt**. 

  * For project's **dbt** part, data is contained in multiple tables that are regarded as a soft wrap on the already existing tables. These tables are stored in `dbt_schema` schema as views:
    * `stg_drivers`
    * `stg_constructors`
    * `stg_circuits`
    * `stg_seasons`
    * `stg_status`
    * `stg_races`
    * `stg_qualifying`
    * `stg_results`
    * `stg_driver_standings`
    * `stg_sprint_results`
    * `stg_lap_times`
    * `stg_pit_stops`
    * `stg_constructor_results`
    * `stg_constructor_standings`
  * Going further in data modeling using **dbt**, intermediate tables are also stored in `dbt_schema`:
    * `int_constructor_total_points_season`
    * `int_driver_total_points_season`
    * `int_race_results`
  * Mart tables are stored in their respective schemas:
    * In `dbt_schema_core_schema`:
        * `dim_constructors`
        * `dim_drivers`
    * In `dbt_schema_constructor_performance_schema`:
      * `fct_constructor_performance`
    * In `dbt_schema_driver_performance_schema`:
      * `fct_driver_performance`


* **Containerization**
  * The project uses containerized **Spark** and **dbt** images. Prior to using the images, they have to be built using `make spark-build-no-cache` and `make dbt-image-build` commands. Once the images are built:
    * Spark cluster does require for container to run using `make spark-up` command;
    * dbt container will run once a command is issued, and after it will be removed. This is done to prevent creating multiple containers that are only used once;
    * All possible commands for this project are set up in Makefile that is stored in a project's root directory.


## How To Use The Program

### 1. Using Docker Images

Prior to using Spark and dbt, their respective Docker Images have to be built:
- Once the project pulled from git, run `make spark-build-no-cache` and `make dbt-image-build` commands.
- The project contains the necessary files for a successful creation of both images. While building Spark image, some necessary files will be downloaded again into the image container. This is done to ensure a smooth Spark image build and later operation.
- Make sure to have `.env` and `.env.spark` files ready (check **Important** section below).
- In the terminal window navigate to `scripts` folder and run `create_folders_set_permissions.sh` script.
- The necessary folders `logs`, `dags` and `backups` will be created automatically.
- In the terminal window navigate to `scripts` folder and run `start_app_airflow_containers.sh` script. This will start Docker containers of application and Airflow images.
- The Images of the applications are pulled from a public repository on Docker Hub.
- In case a restart is needed, run `restart_app_airflow_containers.sh` script.
- To stop running images and remove them, run `stop_app_airflow_containers.sh` script.


**Note:**

Every time the program runs, a log file is created in `logs` folder for that day. Information about any subsequent run is appended to the log file of that day. The program logs every data transformation and data upload to the database. Errors are also logged into the same log file for the current day of the run.

Additionally, when dbt service is run, logs are stored in `dbt` folder as it is the default location.


### **Important:**

1. **For database connection:**

To connect to the database, the `src/db_functions/db_connection.py` file needs to read connection values from `.env` file:

|                                                       |
|-------------------------------------------------------|
| PGUSER = db_username                                  | 
| PGPASSWORD = user_password                            | 
| PGHOST = host_name                                    |
| PGPORT = port                                         |
| PGDATABASE =  database_name                           |

\
1.1. **For PostgreSQL Docker image:**

When using Docker, **PostgreSQL** needs **POSTGRES_USER**, **POSTGRES_PASSWORD** and **POSTGRES_DB** environment variables to be passed. For this reason the YAML file can be set up to read these environment variables from `.env` file.

Once the `make db-up` command is issued, an `init.sql` file will be run to create a database and necessary user. To set up a new user with necessary credentials, edit the `init.sql` file in `sql` folder. 

\
1.2 **To Connect to a PostgreSQL database from OUTSIDE the Docker container:**

When connecting to a database from **outside** the Docker container, for connection parameters in database connection window use:
* **PORT**,
* **DATABASE**,
* **USER**, 
* **PASSWORD** 
* and **HOST** variable. 

For **HOST** use `localhost` or `127.0.0.1`. \
For when the application running in Docker and other services need to connect to Postgres, **HOST** should be the name of Postgres database service in YAML file. In this case it is `project-db`.

\
1.3 **For Spark Image:**

Spark Image requires `.env.spark` file that contains the following Spark option:
* **SPARK_NO_DAEMONIZE=true**
This command allows Spark container to run indefinitely until a `make spark-down` command is run.

Spark Image also uses a `entrypoint.sh` shell script located in `scripts` folder. It is used to correctly bind Spark worker node and Spark master node ports.

\
**Note:**

Store the `.env` file in the root directory of the project folder to connect to the database to use it with no issues and `.env.spark` file to make sure that Spark container remains running.


## Concurrency method used

The program uses Threading as concurrency method to fetch, transform and upload the data. Threading is suitable when looking to parallelize heavy I/O work, such as HTTP calls, reading from files and processing data. 

Here, Python's own `threading` and `concurrent.futures` modules are used. The `concurrent.futures` module provides a high-level interface for asynchronously executing callables. The asynchronous execution is performed with threads using `threading` module.
The `concurrent.futures` module allows for an easier way to run multiple tasks simultaneously using multi-threading to go around GIL limitations.


Using **ThreadPoolExecutor** subclass uses a pool of threads to execute calls asynchronously. All threads enqueued to **ThreadPoolExecutor** will be joined before the interpreter can exit.


## What could be improved or changed (TODO!!!!)

* The Spark dataframe upload to a database function could ditch the workaround to use Pandas API so that the dataframes could be uploaded to tables defined with SQLAlchemy. The same table definition could have been achieved with Spark. Or a different workaround could have been implemented.
