CREATE ROLE root;
ALTER ROLE root WITH LOGIN;
CREATE DATABASE "root";
CREATE DATABASE "sales_data_db";

CREATE ROLE db_admin;
GRANT ALL PRIVILEGES ON DATABASE "sales_data_db" TO db_admin;

ALTER ROLE db_admin WITH PASSWORD :'postgres_password';

CREATE EXTENSION IF NOT EXISTS dblink;

DO
$do$
BEGIN
   IF EXISTS (SELECT FROM pg_database WHERE datname = 'sales_data_db') THEN
      RAISE NOTICE 'Database already exists';
   ELSE
      PERFORM dblink_exec('dbname=' || current_database()
                        , 'CREATE DATABASE "sales_data_db"');
   END IF;
END
$do$;

CREATE USER airflow WITH PASSWORD 'airflow';
GRANT ALL PRIVILEGES ON DATABASE "sales_data_db" TO airflow;