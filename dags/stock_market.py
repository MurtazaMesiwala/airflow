from airflow.decorators import dag, task
from airflow.hooks.base import BaseHook
from datetime import datetime
import requests

@dag(
    start_date=datetime(2023, 1, 1),
    #default_args=default_args,
    schedule='@daily',
    catchup=False,
    tags=['stock_market']
)
def stock_market():
    
    @task.sensor(poke_interval=30, timeout=300, mode='poke')
    def is_api_available() -> PokeReturnValue:
        api = BaseHook.get_connection('stock_api')
        url = f"{api.host}{api.extra_dejson['endpoint']}"
        response = requests.get(url, header=api.extra_dejson['endpoint'])
        condition = response

stock_market()