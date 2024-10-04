FROM python:3.11.4

# Dependencies for Adoptium
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            wget \
            apt-transport-https \
            gpg \
            gnupg \
            software-properties-common && \
    rm -rf /var/lib/apt/lists/*

# Adding Adoptium repository
RUN wget -O - https://packages.adoptium.net/artifactory/api/gpg/key/public | gpg --dearmor | tee /etc/apt/trusted.gpg.d/adoptium.gpg > /dev/null && \
    echo "deb https://packages.adoptium.net/artifactory/deb $(awk -F= '/^VERSION_CODENAME/{print$2}' /etc/os-release) main" | tee /etc/apt/sources.list.d/adoptium.list

# Updating the image, installing necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            temurin-17-jdk \
            curl \
            unzip \
            rsync \
            ssh && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Environment variables for Poetry
ENV POETRY_VERSION=1.8.2
ENV POETRY_HOME=/usr/local
ENV POETRY_VIRTUALENVS_CREATE=false

# Environment variables for Spark and JDK
ENV JAVA_HOME=/usr/lib/jvm/temurin-17-jdk-amd64
ENV PATH="${JAVA_HOME}/bin:${PATH}"

ENV SPARK_VERSION=3.5.1
ENV HADOOP_VERSION=3
ENV SPARK_HOME=${SPARK_HOME:-"/opt/spark"}
ENV HADOOP_HOME=${HADOOP_HOME:-"/opt/hadoop"}

# Creating necessary directories
RUN mkdir -p ${SPARK_HOME} && \
    mkdir -p ${HADOOP_HOME} && \
    mkdir libs

COPY libs/postgresql-42.7.4.jar /libs/

# Changing working directory
WORKDIR ${SPARK_HOME}

# Installing Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - --version=$POETRY_VERSION

COPY poetry.lock pyproject.toml ./

# Installing dependencies
RUN poetry install --no-root

# Spark installation
RUN curl "https://archive.apache.org/dist/spark/spark-${SPARK_VERSION}/spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" -o "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" && \
    tar -xvzf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz" --directory ${SPARK_HOME} --strip-components 1 && \
    rm -rf "spark-${SPARK_VERSION}-bin-hadoop${HADOOP_VERSION}.tgz"

RUN pip3 install pyspark==${SPARK_VERSION}

# Environment variables for Spark
ENV PATH="${SPARK_HOME}/sbin:${SPARK_HOME}/bin:${PATH}"
ENV SPARK_HOME="${SPARK_HOME}"
ENV SPARK_MASTER="spark://spark-master:7077"
ENV SPARK_MASTER_HOST=spark-master
ENV SPARK_MASTER_PORT=7077
ENV PYSPARK_PYTHON=python3

# Spark default configs
COPY conf/spark-defaults.conf "$SPARK_HOME/conf/"

# Setting binaries and scripts to be executable
RUN chmod u+x /opt/spark/sbin/* && \
    chmod u+x /opt/spark/bin/*

ENV PYTHONPATH=${SPARK_HOME}/python/:${PYTHONPATH}

COPY scripts/entrypoint.sh $SPARK_HOME/

RUN chmod u+x $SPARK_HOME/entrypoint.sh
RUN ls -l $SPARK_HOME/entrypoint.sh

ENTRYPOINT ["/opt/spark/entrypoint.sh"]

#CMD ["/bin/bash", "${SPARK_HOME}/entrypoint.sh"]