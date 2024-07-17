import pendulum
from airflow import DAG
from airflow.sensors.filesystem import FileSensor

with DAG(
    dag_id='dags_file_sensor',
    start_date=pendulum.datetime(2024,4,1,tz='Asia/Seoul'),
    schedule='0 7 * * *',
    catchup=False
) as dag:
    
    tvCorona19VaccinestatNew_sensor=FileSensor(
        task_id='tvCorona19VaccinestatNew_sensor',
        fs_conn_id='conn_file_opt_airflow_files',
        filepath='tvCorona19VaccinestatNew/20240716/tvCorona19VaccinestatNew.csv',
        recursive=False,
        poke_interval=30,
        timeout=60,
        mode='reschedule'
    )