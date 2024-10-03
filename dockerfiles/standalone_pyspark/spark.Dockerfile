FROM python:3.11.4

ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/usr/local
ENV POETRY_VIRTUALENVS_CREATE=false

FROM eclipse-temurin:17-jre-alpine

ENV JAVA_HOME = /opt/java/openjdk
ENV PATH="${JAVA_HOME}/bin:${PATH}"

ENV APACHE_SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3
#TODO ENV SPARK_HOME="/opt/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}"
#TODO ENV PATH="$PATH:$SPARK_HOME/bin"


RUN apt-get update && \
    apt-get install -y --no-install-recommends

https://dlcdn.apache.org/spark/spark-3.5.3/spark-3.5.3-bin-hadoop3.tgz
# Spark installation
WORKDIR /tmp
RUN wget -q "https://archive.apache.org/dist/spark/spark-${APACHE_SPARK_VERSION}/spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    echo "${spark_checksum} *spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" | sha512sum -c - && \
    tar xzf "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -C /usr/local --owner root --group root --no-same-owner && \
    rm "spark-${APACHE_SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

wget https://downloads.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz
tar xvf spark-3.2.0-bin-hadoop3.2.tgz


RUN mkdir libs
COPY /libs/postgresql-42.7.4.jar /libs





CMD ["/entrypoint.sh"]