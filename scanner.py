import requests
import time

BOT_TOKEN = "8620436807:AAFki28rQ4gGsx8EXVgvon7AVJZRdU-mMmI"
CHAT_ID = "7939533113"

def send(msg):

    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"

    payload = {
        "chat_id": CHAT_ID,
        "text": msg
    }

    requests.post(url, json=payload)


def scan():

    url = "https://api.dexscreener.com/latest/dex/pairs/solana"

    r = requests.get(url).json()

    for pair in r["pairs"][:10]:

        name = pair["baseToken"]["name"]
        symbol = pair["baseToken"]["symbol"]
        link = pair["url"]

        message = f"""
🚨 NEW SOLANA TOKEN

{name} ({symbol})

{link}
"""

        send(message)

        break


while True:

    scan()
    time.sleep(60)