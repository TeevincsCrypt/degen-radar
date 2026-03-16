import requests
import time

BOT_TOKEN = "8620436807:AAFki28rQ4gGsx8EXVgvon7AVJZRdU-mMmI"
CHAT_ID = "7939533113"

keywords = ["AI dog", "Trump coin", "Elon pet"]

def send_alert(msg):

    url = f"https://api.telegram.org/bot8620436807:AAFki28rQ4gGsx8EXVgvon7AVJZRdU-mMmI/sendMessage"

    payload = {
        "chat_id": 7939533113,
        "text": msg
    }

    requests.post(url, json=payload)


def scan():

    for keyword in keywords:

        url = f"https://api.dexscreener.com/latest/dex/search?q={keyword}"

        r = requests.get(url).json()

        for pair in r.get("pairs", []):

            if pair["chainId"] != "solana":
                continue

            name = pair["baseToken"]["name"]
            symbol = pair["baseToken"]["symbol"]
            link = pair["url"]

            message = f"""
🚨 SOLANA MEME FOUND

Narrative: {keyword}

Token: {name} ({symbol})

DEX:
{link}
"""

            send_alert(message)

            return


while True:

    scan()

    time.sleep(60)