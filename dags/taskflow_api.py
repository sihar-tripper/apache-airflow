from airflow import DAG 
from airflow.decorators import task
from datetime import datetime, timedelta

default_args= {
    'owner': 'sihar',
    'start_date': datetime(2024,8,25),
    'retries': 3,
    'retry_delay': timedelta(minutes=3)
}

@task()
def get_name():
    return 'sihar'

@task()
def present(name):
    print(f'hello {name} welcome to the board')


with DAG(
    'tes_taskflow',
    default_args= default_args,
    schedule_interval= '@daily'
) as dag:
    name = get_name()
    present(name)
    
    