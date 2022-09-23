from datetime import timedelta

from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.utils.dates import datetime
from airflow.utils.dates import timedelta
from airflow.utils.dates import days_ago

default_args = {
    "owner": "Michael Getachew",
    "email": ["mikygetyos@gmail.com"],
    "email_on_failaure": False,
    "retries": 1,
    "retry_delay": timedelta(minutes=5),
}

dag_exec_scripts = DAG(
    dag_id="create_table_and_load_data",
    default_args=default_args,
    schedule_interval="@daily",
    start_date=days_ago(1),
    dagrun_timeout=timedelta(minutes=60),
    description="executing dag scripts",
)


dbt_run = BashOperator(task_id="dbt_run", bash_command="dbt run", dag=dag_exec_scripts)

dbt_test = BashOperator(
    task_id="dbt_test", bash_command="dbt test", dag=dag_exec_scripts
)

dbt_run >> dbt_test