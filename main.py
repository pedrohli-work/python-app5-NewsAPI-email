# Used to send HTTP requests to external APIs
import requests
# Import the custom function to send emails
from send_email import send_email

# The keyword to search for in the news API
topic = "tesla"

# API key for authenticating requests to the NewsAPI
api_key = "646580a89c1043788d176b35058ffe8f"

# Construct the URL with query parameters
url = "https://newsapi.org/v2/everything?" \
f"q={topic}&" \
"from=2025-07-20&" \
"sortBy=publishedAt&" \
"apiKey=646580a89c1043788d176b35058ffe8f&" \
"language=en"

# Send a GET request to the API and wait up to 10 seconds
request = requests.get(url, timeout=10)
# Convert the JSON response to a Python dictionary
content = request.json()

# Start composing the email body. "Subject" will be the email subject line.
body = "Subject: Today's News\n\n"

# Loop through the first 20 articles in the API response
for article in content["articles"][0:20]:
     # Check if both title and description are available
    if article["title"] is not None and article["description"] is not None:
        # Add the title, description, and URL of the article to the email body
        body = body + article["title"] + "\n" \
            + article["description"] \
            + "\n" + article["url"] + 2*"\n"

# Convert the email body to UTF-8 encoded bytes
body = body.encode("utf-8")

# Call the custom function to send the email with the news content
send_email(message=body)
