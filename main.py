from linebot import LineBotApi
from linebot.models import TextSendMessage
import schedule
import time
import os

LINE_TOKEN = os.getenv("LINE_TOKEN")

GROUP_ID = os.getenv("GROUP_ID")

line_bot_api = LineBotApi(LINE_TOKEN)

MESSAGE = """thidua camera
thidua dh
thidua pkdh
thidua tainghe
thidua psdp"""

def send_message():
    try:
        line_bot_api.push_message(
            GROUP_ID,
            TextSendMessage(text=MESSAGE)
        )
        print("SEND SUCCESS")
    except Exception as e:
        print("ERROR:", e)

schedule.every().day.at("12:15").do(send_message)
schedule.every().day.at("15:15").do(send_message)
schedule.every().day.at("18:15").do(send_message)
schedule.every().day.at("23:15").do(send_message)

print("BOT RUNNING")

while True:
    schedule.run_pending()
    time.sleep(5)