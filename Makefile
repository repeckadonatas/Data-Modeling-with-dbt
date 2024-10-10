# FOR SPARK CLUSTER
spark-build-no-cache:
	docker compose -f docker-compose.spark.yml build standalone_spark_cluster --no-cache

spark-up:
	docker compose -f docker-compose.spark.yml up

spark-down:
	docker compose -f docker-compose.spark.yml down -v

spark-restart:
	docker compose -f docker-compose.spark.yml down -v && \
	docker compose -f docker-compose.spark.yml up

spark-run-scaled:
	docker compose -f docker-compose.spark.yml down && \
	docker compose -f docker-compose.spark.yml up --scale spark-worker=3

spark-submit:
	docker exec spark-master spark-submit \
 	--master spark://spark-master:7077 --deploy-mode client ./apps/$(app)


# FOR DATABASE
db-up:
	docker compose -f docker-compose.db.yml up

db-down:
	docker compose -f docker-compose.db.yml down


# FOR DBT
dbt-image-build:
	docker compose -f docker-compose.dbt.yml build dbt_core_local --no-cache

dbt-init:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt init

dbt-build:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt build --select $(model) --profiles-dir /usr/app/dbt

dbt-run-all:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt run

dbt-run-select:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt run --select $(model) --profiles-dir /usr/app/dbt

dbt-test:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt test

dbt-debug:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt debug

dbt-compile:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt compile

dbt-docs:
	docker compose -f docker-compose.dbt.yml run --rm dbt dbt docs generate

dbt-shell:
	docker compose -f docker-compose.dbt.yml run --rm dbt bash