import requests
import datetime as dt
from datetime import timedelta
from news import News
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

# Alpha Vantage
STOCK_API_KEY = "APIKEY"
STOCK_ENDPOINT = "https://www.alphavantage.co/query"

# Twilio creds:
account_sid = "ACCOUNT_SID"
auth_token = "AUTH_TOKEN"
TWILIO_NUMBER = "TWILIO PHONE NUM"
MY_NUMBER = "PHONE NUMBER"

# Newsapi.org
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "API KEY"

# Getting the Dates (TEST TIME)
date = dt.datetime(year=2024, month=2, day=21).date()
yesterday_date = date - timedelta(days=1)

news_list = []
def get_closing_differance():
    stock_params = {
        "function": "TIME_SERIES_DAILY",
        "symbol": STOCK,
        "apikey": STOCK_API_KEY,
    }
    response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
    response.raise_for_status()
    stock_data = response.json()
    yesterday_closing = float(stock_data["Time Series (Daily)"][str(yesterday_date)]['4. close'])
    today_closing = float(stock_data["Time Series (Daily)"][str(date)]['4. close'])
    # print(yesterday_closing, today_closing)
    percent = round(((today_closing - yesterday_closing) / yesterday_closing) * 100, 2)
    # positive_percent = abs(percent)

    if percent > 0:
        return f"TESLA:🔺{percent}%"
    else:
        return f"TESLA:🔻{percent}%"


# Fetch then first 3 News Articles for the company name
def fetch_news():
    news_params = {
        "q": "Tesla",
        "from": str(yesterday_date),
        "sortBy": "popularity",
        "apiKey": NEWS_API_KEY
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_params)
    response.raise_for_status()
    news_data = response.json()
    for i in range(3):
        news = News(title=news_data["articles"][i]["title"], url=news_data["articles"][i]["url"])
        # print(news.title)
        news_list.append(news)


def create_msg_body(index:int):
    fetch_news()
    msg_body = (f"{get_closing_differance()}\n"
                f"{news_list[index].title}\n"
                f"{news_list[index].url}")
    return msg_body
print(create_msg_body(0))

def send_sms_alert():
    client = Client(account_sid, auth_token)
    for i in range(3):
        message = client.messages \
            .create(
            body=create_msg_body(i),
            from_=TWILIO_NUMBER,
            to=MY_NUMBER,
        )
        print(message.status)

send_sms_alert()
