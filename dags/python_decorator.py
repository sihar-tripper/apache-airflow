from airflow.decorators import dag, task 
from datetime import datetime, timedelta

default_args={
    'owner': 'sihar',
    'start_date': datetime(2024, 8, 25),
    'retries': 3,
    'retry_dlay': timedelta(minutes=3)
}

@dag(dag_id= 'dag_with_decorators',
     default_args= default_args, 
     schedule_interval= '@daily')
def hello_word():

    @task(multiple_outputs= True)
    def get_name():
        return {'first_name': 'sihar',
                'last_name': 'pangaribuan'}
    
    @task()
    def get_age():
        return '19'
    
    @task()
    def greet(first_name, last_name, age):
        print(f'hello word by {first_name} {last_name}, and my age {age}')

    
    name_dict= get_name()
    age= get_age()
    hello = greet(name_dict['first_name'], name_dict['last_name'], age)

hello_word()