import json
import time
import threading
from configs.settings import mined_coin
from websocket._app import WebSocketApp


current_price = None
last_update = None
# Configurações
STREAM_URL = f"wss://stream.binance.com:9443/ws/{mined_coin}@ticker"

def on_message(ws, message):
    global current_price, last_update
    try:
        datas = json.loads(message)
        current_price = float(datas['c'])
        last_update = time.strftime('%Y-%m-%d %H:%M:%S')
        print(f"Preço atual: {current_price}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

def on_error(ws, error):
    print(f"Erro: {error}")

def on_close(ws, close_status_code, close_msg):
    print(f"Conexão encerrada. Código: {close_status_code}, Mensagem: {close_msg}")
    time.sleep(5)
    start_websocket_thread()

def on_open(ws):
    print(f"Conectado ao stream {mined_coin.upper()}@ticker")

def get_current_price():
    return {
        "price": current_price,
        "last_update": last_update,
        "coin": mined_coin.upper()
    }

def websocket_thread():
    print("Iniciando conexão WebSocket...")
    # Configuração do WebSocket
    ws = WebSocketApp(
        STREAM_URL,
        on_open=on_open,
        on_message=on_message,
        on_error=on_error,
        on_close=on_close
    )
    ws.run_forever()

def start_websocket_thread():
    thread = threading.Thread(target=websocket_thread)
    thread.daemon = True
    thread.start()
    return thread

print(f"Iniciando o monitoramento do preço de {mined_coin.upper()}")
ws_thread = start_websocket_thread()

if __name__ == "__main__":
    # Inicia o WebSocket
    print(get_current_price())
    start_websocket_thread()
    print(get_current_price())

'''
from configs.settings import mined_coin
from binance.client import Client

client = Client()
# obtém preço médio
def get_avg_price(coin_id=mined_coin.upper()):
    return client.get_avg_price(symbol=coin_id)


# obtém preço atual
def get_ticker_price(coin_id=mined_coin.upper()):
    return client.get_symbol_ticker(symbol=coin_id)


if __name__ == "__main__":
    print(get_avg_price())
    print(get_ticker_price())
'''
