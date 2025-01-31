
import pandas as pd
import datetime as dt
from datetime import timedelta
from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.python import PythonOperator 

default_argsList = {
    'owner': "emmanuel", 'start_date': dt.datetime(2024, 12, 28),
    'retries': 1, 'retry_delay': timedelta(minutes=5),
}

def csvToJson():
    file_dt = pd.read_csv('createCsv.csv')
    for i, x in file_dt.iterrows(): print(x['name'], i)
    file_dt.to_json("fromAirflow.json", orient="records")
    

with DAG(dag_id="a_dag_test", default_args=default_argsList, schedule=timedelta(minutes=5)) as dag:
    working_with_bash = BashOperator(task_id='bash1',bash_command='echo "task on python completed"')
    working_with_python = PythonOperator(task_id='python1', python_callable=csvToJson)
    working_with_python >> working_with_bash ## python runs before bash
    # working_with_bash >> working_with_python
    # working_with_bash.set_downstream(working_with_python)
    ##meaning workingwithpython (upstream)
    ##              |
    ##        workingwithbash (downstream)



