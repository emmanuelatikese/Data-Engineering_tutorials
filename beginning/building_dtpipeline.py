from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator
import pandas as pd
import psycopg2 as db
from elasticsearch import Elasticsearch
import urllib3


def ExtractDB():
    try:
        conn_str = "dbname='users' host='localhost' user='postgres' password='password'"
        conn = db.connect(conn_str)
        df = pd.read_sql("SELECT * FROM userstable", conn)
        df.to_csv("pipeline.csv")
    except Exception as e:
        print("{} just occured in function".format(e))
        conn.rollback()
    finally:
        if conn: conn.close()

def AddToElastic():
    try:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        es = Elasticsearch(["https://localhost:9200"], http_auth=('elastic', 'Z+UDEk-BsA1pOpsW1OTn'), verify_certs=False)
        df = pd.read_csv("pipeline.csv")
        for _, r in df.iterrows():
            body = r.to_json()
            es.index(index="userstable", body=body)
        print("completely successful")
    except Exception as e:
        print("This is the Error you got in Elastic: ", e)


from airflow import DAG
import datetime as dt 
from datetime import timedelta 

args_def = {
    'owner': "emmanuel", 'start_date': dt.datetime(2025, 1, 1),
    'retries': 1, 'retry_delay': timedelta(minutes=5),
}


with DAG(dag_id="my_pipeline", default_args= args_def, schedule=timedelta(minutes=5)) as dag:
    get_data_fromDb = PythonOperator(task_id="task1", python_callable=ExtractDB)
    add_dataToElastic = PythonOperator(task_id="task2", python_callable=AddToElastic)
    bash_indication = BashOperator(task_id="task3", bash_command='echo "Completely successful"')

    get_data_fromDb >> add_dataToElastic >> bash_indication

