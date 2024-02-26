---

# Stock News Alert

This Python script fetches stock information and relevant news articles about a specific company and sends SMS alerts using Twilio.

## Features

- Retrieves daily stock data for a specified company from Alpha Vantage API.
- Fetches the latest news articles related to the company from News API.
- Sends SMS alerts containing stock performance and news headlines using Twilio.

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- `twilio` library (`pip install twilio`)

## Setup

1. Clone this repository:

```
git clone https://github.com/your-username/stock-news-alert.git
cd stock-news-alert
```

2. Install dependencies:

```
pip install -r requirements.txt
```

3. Obtain API keys:

    - Alpha Vantage: [Sign up](https://www.alphavantage.co/support/#api-key) to get your API key.
    - News API: [Sign up](https://newsapi.org/register) to get your API key.
    - Twilio: [Sign up](https://www.twilio.com/try-twilio) and obtain your Account SID, Auth Token, and Twilio phone number.

4. Configure the script:

    - Open `main.py` in a text editor.
    - Replace placeholders `APIKEY`, `ACCOUNT_SID`, `AUTH_TOKEN`, `TWILIO PHONE NUM`, `PHONE NUMBER` with your respective API keys and phone numbers.

## Usage

Run the script:

```
python main.py
```

This will fetch the latest stock data and news articles and send SMS alerts.

## Notes

- The script currently fetches data for Tesla Inc (TSLA). Modify the `STOCK` and `COMPANY_NAME` variables in the script to monitor a different company.
- By default, the script fetches news articles related to "Tesla". You can adjust the search query by modifying the `fetch_news()` function in the script.

## Contributors

- [Reza Enayati](https://github.com/rezEnayati)

---
