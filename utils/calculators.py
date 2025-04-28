import json
import time

from crawlers.prices import get_current_price
from configs.settings import eletric_cost
from configs.settings import mined_coin

def calc_profit(hashrate, power_consumtion):
    coin_price = get_current_price()
    while coin_price is None:
        print("Preço ainda não encontrado, esperando retorno do WebSocket")
        time.sleep(1)

    daily_revenue = hashrate * coin_price
    daily_consumption = (power_consumtion * 24) * eletric_cost

    return {
        "coin": f"{mined_coin}",
        "receita_diária_USD": daily_revenue,
        "custo_diário_BRL": daily_consumption,
        "lucro_diário": daily_revenue - daily_consumption
    }

if __name__ == "__main__":
    print(calc_profit(50, 200))  # Exemplo: 50MH/s, 200W