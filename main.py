import os
import requests
from send_email import send_email

TOPIC = "tesla"

# Read API key from environment variable
API_KEY = os.getenv("NEWS_API_KEY")

if not API_KEY:
    raise RuntimeError("NEWS_API_KEY environment variable not set")

url = (
    f"https://newsapi.org/v2/everything"
    f"?q={TOPIC}&sortBy=publishedAt&language=en&apiKey={API_KEY}"
)

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)
content = response.json()

# Handle API errors
if content.get("status") != "ok":
    print("News API error:")
    print(content)
    exit()

articles = content.get("articles", [])[:20]

if not articles:
    print("No articles found.")
    exit()

body = ""

for article in articles:
    title = article.get("title") or ""
    description = article.get("description") or ""
    link = article.get("url") or ""

    if title or description:
        body += f"{title}\n{description}\n{link}\n\n"

if body:
    send_email(body)
    print("✅ Email sent successfully!")
else:
    print("No valid article content to send.")
