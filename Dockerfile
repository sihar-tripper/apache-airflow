FROM apache/airflow:2.9.3

COPY requirements.txt /requirements.txt 
RUN pip install --no-cache-dir -r /requirements.txt
USER root
RUN apt-get update && apt-get install -y --no-install-recommends sudo git \
    && apt-get clean && rm -rf /var/lib/apt/lists/*
USER airflow