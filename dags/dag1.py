from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import random

def welcome(name): print(f'Welcome to Airflow {name}')

output_file = '/tmp/random.txt'
def nums():
    num = random.randint(1, 50)
    with open(output_file, "w") as f:
        f.write(str(num))
    print(f"random num is saved")

with DAG(
    dag_id='first_taskk',
    start_date=datetime(2025,10,2),
    schedule_interval=timedelta(minutes=1),
    catchup=False
) as dag:
    task_prnt=BashOperator(
        task_id='task_prnt',
        bash_command='date'
    )
    welcome_print = PythonOperator(
        task_id="welcome_print",
        python_callable=welcome,
        op_kwargs={'name': 'Yasmine'}
    )
    task_numss = PythonOperator(
        task_id="task_numss",
        python_callable=nums
    )
    task_prnt>>welcome_print>>task_numss
