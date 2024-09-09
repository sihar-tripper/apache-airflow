FROM apache/airflow:2.10.1

COPY requirements.txt /. 

RUN pip install --no-cache-dir -r /requirements.txt

USER root

RUN apt-get update && apt-get install -y --no-install-recommends

USER airflow