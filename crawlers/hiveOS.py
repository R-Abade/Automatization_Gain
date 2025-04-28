import requests
from configs.settings import hiveOS_API_key, farm_hiveOS_ID

def get_hiveOS_mining_datas():
    url = f"https://api.hiveos.farm/api/v2/farms/{FARM_ID}/workers"
    headers = {"Authorization": f"Bearer {HIVEOS_API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()  # Trate erros depois!