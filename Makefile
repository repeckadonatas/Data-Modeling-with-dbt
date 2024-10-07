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
	docker compose down && docker compose up --scale spark-worker=3

spark-submit:
	docker exec spark-master spark-submit \
 	--master spark://spark-master:7077 --deploy-mode client ./apps/$(app)


# FOR DATABASE
db-up:
	docker compose -f docker-compose.app.yml up

db-down:
	docker compose -f docker-compose.app.yml down


# FOR DBT
dbt-build:
	docker compose -f docker-compose.dbt.yml build dbt_core_local --no-cache

dbt-up:
	docker compose -f docker-compose.dbt.yml up

dbt-down:
	docker compose -f docker-compose.dbt.yml down

dbt-init:
	#docker compose -f docker-compose.dbt.yml run --rm dbt dbt init
	docker compose -f docker-compose.dbt.yml run dbt dbt init

dbt-run:
	docker compose -f docker-compose.dbt.yml run dbt dbt run

dbt-test:
	docker compose -f docker-compose.dbt.yml run dbt dbt test

dbt-compile:
	docker compose -f docker-compose.dbt.yml run dbt dbt compile

dbt-docs-generate:
	docker compose -f docker-compose.dbt.yml run dbt dbt docs generate

dbt-shell:
	docker compose -f docker-compose.dbt.yml run dbt bash