CREATE ROLE root;
ALTER ROLE root WITH LOGIN;
CREATE DATABASE "root";

CREATE EXTENSION IF NOT EXISTS dblink;

DO
$do$
BEGIN
   IF NOT EXISTS (SELECT FROM pg_catalog.pg_roles WHERE rolname = '${PGUSER}') THEN
      CREATE ROLE ${PGUSER} WITH LOGIN PASSWORD ${PGPASSWORD};
   END IF;

   IF EXISTS (SELECT FROM pg_database WHERE datname = '${PGDATABASE}') THEN
      RAISE NOTICE 'Database already exists';
   ELSE
      PERFORM dblink_exec('dbname=' || current_database()
                        , 'CREATE DATABASE "${PGDATABASE}"');
   END IF;
END
$do$;

\c ${PGDATABASE}

GRANT ALL PRIVILEGES ON DATABASE ${PGDATABASE} TO ${PGUSER};

-- CREATE USER airflow WITH PASSWORD 'airflow';
-- GRANT ALL PRIVILEGES ON DATABASE "sales_data_db" TO airflow;

-- CREATE ROLE db_admin;
-- ALTER ROLE db_admin WITH LOGIN;
-- CREATE USER db_admin WITH PASSWORD :'postgres_password';
-- ALTER ROLE db_admin WITH PASSWORD :'postgres_password';
--