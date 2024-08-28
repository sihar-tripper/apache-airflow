from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime, timedelta


def hello_word():
    print('hello word')

def hello(first_name:str, last_name:str):
    print(f'hello {first_name} {last_name}')



default_args ={
    'owner': 'sihar',
    'start_date': datetime(2024, 8, 25),
    'retries': 3,
    'retry_delay': timedelta(minutes=5)
}

with DAG(
    dag_id='python_operator',
    default_args=default_args,
    schedule_interval='@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id = 'task_1',
        python_callable= hello_word
    )

    task2 = PythonOperator(
        task_id= 'task_2',
        python_callable= hello,
        op_kwargs= {'first_name': 'sihar','last_name': 'pangaribuan'}
    )

    task1 >> task2