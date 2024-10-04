#!/bin/bash

set -e

SPARK_WORKLOAD=$1

echo "SPARK_WORKLOAD: $SPARK_WORKLOAD"

if [ "$SPARK_WORKLOAD" == "master" ];
then
  start-master.sh -p 7077

elif [ "$SPARK_WORKLOAD" == "worker" ];
then
  WORKER_PORT=${2:-8080}
  echo "$WORKER_PORT"

  start-worker.sh spark://spark-master:7077 --webui-port "$WORKER_PORT"
fi