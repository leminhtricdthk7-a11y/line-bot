from linebot import LineBotApi
from linebot.models import TextSendMessage
import os
from datetime import datetime

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

        print("===================================")
        print("SEND SUCCESS")
        print(datetime.now())
        print("===================================")

    except Exception as e:
        print("===================================")
        print("SEND ERROR")
        print(e)
        print("===================================")

if __name__ == "__main__":
    send_message()