from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import BranchPythonOperator
from airflow.utils.dates import days_ago

def pilih_cabang():
    # Logika untuk menentukan cabang mana yang diambil
    if False:  # Contoh kondisi yang selalu benar
        return 'cabang_1'
    else:
        return 'cabang_2'

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': days_ago(1),
}

dag = DAG(
    'contoh_branching',
    default_args=default_args,
    description='Contoh DAG dengan branching',
    schedule_interval=None,
)

mulai = DummyOperator(
    task_id='mulai',
    dag=dag,
)

branch_task = BranchPythonOperator(
    task_id='pilih_cabang',
    python_callable=pilih_cabang,
    dag=dag,
)

cabang_1 = DummyOperator(
    task_id='cabang_1',
    dag=dag,
)

cabang_2 = DummyOperator(
    task_id='cabang_2',
    dag=dag,
)

selesai = DummyOperator(
    task_id='selesai',
    dag=dag,
)

# Menyusun alur DAG
mulai >> branch_task
branch_task >> [cabang_1, cabang_2]
cabang_1 >> selesai
cabang_2 
