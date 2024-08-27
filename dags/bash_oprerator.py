from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2023, 8, 26),
    'retries': 1,
}

with DAG(
    dag_id='bash_operator',
    default_args=default_args,
    schedule_interval='@daily',
    catchup=True
) as dag:
    
    t1 = BashOperator(
        task_id= 'print_date',
        bash_command= 'date')

    t2 = BashOperator(
        task_id = 'hello_world',
        bash_command = 'echo hello word')
    
    t1 >> t2
