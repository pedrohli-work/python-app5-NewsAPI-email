# Daily News Email 📰✉️

This Python project fetches the latest news articles based on a keyword using the NewsAPI and sends a daily summary email using Gmail's SMTP server.

## 🔍 What it does

- Searches for news related to a specific topic (e.g., "Tesla")
- Filters and formats the 20 most recent articles
- Sends the news summary to your email inbox

## 📦 Tech Stack

- Python 3.x
- [NewsAPI](https://newsapi.org)
- `requests` for API calls
- `smtplib` and `ssl` for sending emails
- Gmail SMTP for delivery
- (Optional) Can be scheduled using cron or Task Scheduler

## 🚀 How to Run

1. Clone the repo:
    ```bash
    git clone https://github.com/pedrohli-work/python-app5-NewsAPI-email
    cd daily-news-email
    ```

2. Run the bot:
    ```bash
    python main.py
    ```

## ⚠️ Security Note

Never hardcode your email/password. Use environment variables or a `.env` file and keep them out of version control.

## 📧 Output Example

