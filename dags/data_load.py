from datetime import datetime, timedelta

from airflow import DAG
from airflow.providers.postgres.operators.postgres import PostgresOperator
from airflow.utils.dates import days_ago

default_args = {
    "owner": "jedisam",
    #'start_date': airflow.utils.dates.days_ago(2),
    # 'end_date': datetime(),
    # 'depends_on_past': False,
    "email": ["yidisam18@gmail.com"],
    "email_on_failaure": True,
    #'email_on_retry': False,
    # If a task fails, retry it once after waiting
    # at least 5 minutes
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag_exec_scripts = DAG(
    dag_id="create_table_and_load_data",
    default_args=default_args,
    # schedule_interval='0 0 * * *',
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description="executing the sql scripts",
)

create_table = PostgresOperator(
    sql="sql/create_table.sql",
    task_id="createtable_task",
    postgres_conn_id="postgres_dwh",
    dag=dag_exec_scripts,
)

load_data = PostgresOperator(
    sql="sql/load_data.sql",
    task_id="load_data_task",
    postgres_conn_id="postgres_dwh",
    dag=dag_exec_scripts,
)

create_table >> load_data