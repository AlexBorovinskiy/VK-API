from airflow.models import DAG
from airflow.operators import PythonOperator
from datetime import datetime

default_args = {
    'owner': 'aborovinskiy',
    'depends_on_past': False,
    'retries': 0
}


dag = DAG('aborovinskiy_report_to_vk',
          default_args=default_args,
          schedule_interval='00 12 * * 1',
          start_date = datetime(2021, 2, 10))


task = PythonOperator(task_id='report_to_vk',
                      python_callable=send_report_to_vk,
                      dag=dag)


