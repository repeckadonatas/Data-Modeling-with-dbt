build-no-cache:
	docker compose -f docker-compose.spark.yml build --no-cache

up:
	docker compose -f docker-compose.spark.yml up

down:
	docker compose -f docker-compose.spark.yml down -v

run-scaled:
	docker compose down && docker compose up --scale spark-worker=3

submit:
	docker exec standalone_spark_cluster spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/$(app)