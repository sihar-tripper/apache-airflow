#import libraries needed
from airflow import DAG 
from datetime import datetime, timedelta
from airflow.operators.python_operator import PythonOperator

#function to pull data with return
def show_name():
    return "sihar"

#function to get data by xcom
def great(ti):
    name = ti.xcom_pull(task_ids= 'great')
    print(f'hello {name}')

#function to push data to xcom
def push_data(ti):
    ti.xcom_push(key= 'first_name', value= 'sihar')
    ti.xcom_push(key= 'last_name', value= 'pangrib')

# get data from xcom
def get_data(ti):
    first_name= ti.xcom_pull(task_ids= 'push_data', key= 'first_name')
    last_name= ti.xcom_pull(task_ids= 'push_data', key= 'last_name')
    print(f'hello {first_name} {last_name}')


default_args= {
    'owner': 'sihar',
    'start_date': datetime(2024, 8, 25),
    'retries': 3,
    'retry_delay': timedelta(minutes=2)
}

with DAG(
    'xcom_test',
    default_args=default_args,
    schedule_interval= '@daily'
) as dag:
    
    task1 = PythonOperator(
        task_id= 'great',
        python_callable= show_name
    )

    task2 = PythonOperator(
        task_id= 'get_name',
        python_callable= great
    )

    task3 = PythonOperator(
        task_id= 'push_data',
        python_callable= push_data
    )

    task4 = PythonOperator(
        task_id= 'get_data',
        python_callable= get_data
    )


    task1 >> task2 >> task3 >> task4