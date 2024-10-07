FROM python:3.11.4

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
            git \
            libpq-dev \
            gcc && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir dbt-core dbt-postgres

WORKDIR /usr/app/dbt

ENV DBT_PROFILES_DIR=/usr/app/dbt

ENV PATH="/root/.local/bin:${PATH}"

RUN dbt --version

CMD ["dbt", "--version"]