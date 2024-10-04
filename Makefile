# FOR SPARK CLUSTER
spark-build-no-cache:
	docker compose -f docker-compose.spark.yml build standalone_spark_cluster --no-cache

spark-up:
	docker compose -f docker-compose.spark.yml up

spark-down:
	docker compose -f docker-compose.spark.yml down -v

spark-run-scaled:
	docker compose down && docker compose up --scale spark-worker=3

spark-submit:
	docker exec standalone_spark_cluster spark-submit --master spark://spark-master:7077 --deploy-mode client ./apps/$(app)

# FOR DATABASE
db-up:
	docker compose -f docker-compose.app.yml up

db-down:
	docker compose -f docker-compose.app.yml down