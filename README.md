# News API Email Notifier

A Python application that fetches the latest news articles on a given topic
and sends them via email.

## Features
- Uses NewsAPI to fetch recent articles
- Sends formatted email notifications
- Handles API errors gracefully
- Uses environment variables for security

## Setup

Install dependencies:
```bash
pip install -r requirements.txt
Set environment variables:

set NEWS_API_KEY=your_api_key
set EMAIL_USER=your@gmail.com
set EMAIL_PASS=your_app_password

Run:

python main.py 
```

Technologies:
- Python
- Requests
- SMTP (Gmail)