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
        task_id= 'task_1',
        bash_command= 'date')

    t2 = BashOperator(
        task_id = 'task_2',
        bash_command = 'echo hello word')
    
    t3 = BashOperator(
        task_id = 'task_3',
        bash_command = 'echo third task'
    )

    t1 >> t2 >> t3 
