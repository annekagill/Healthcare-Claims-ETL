from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
from extract import extract
from transform import transform
from load import load

default_args = {
    "owner": "anneka",
    "retries": 1,
    "retry_delay": timedelta(minutes=5)
}

# Define the DAG
with DAG(
    dag_id="cms_medicare_etl",
    description="Daily ETL pipeline for CMS Medicare data",
    default_args=default_args,
    start_date=datetime(2024, 1, 1),
    schedule="@daily",
    catchup=False
) as dag:

    # Extract
    extract_task = PythonOperator(
        task_id="extract",
        python_callable=extract
    )

    # Transform
    transform_task = PythonOperator(
        task_id="transform",
        python_callable=transform
    )

    # Load
    load_task = PythonOperator(
        task_id="load",
        python_callable=load
    )

    extract_task >> transform_task >> load_task