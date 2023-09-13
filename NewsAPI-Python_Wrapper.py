#!/opt/anaconda3/envs/motley_smart/bin/python
from newsapi import NewsApiClient
from config import API_KEY
import datetime

# Initialize the client
newsapi = NewsApiClient(api_key=API_KEY)

# Ask the input
company_name = input("Enter the stock company name: ")

# Current date
today = datetime.date.today()

# Date 30 days ago
thirty_days_ago = today - datetime.timedelta(days=30)

# Convert to string format
str_thirty_days_ago = thirty_days_ago.strftime('%Y-%m-%d')
str_today = today.strftime('%Y-%m-%d')

# Now, you can use str_thirty_days_ago and str_today with the NewsAPI
top_headlines = newsapi.get_everything(q=company_name,
                                       from_param=str_thirty_days_ago,
                                       to=str_today,
                                       language='en',
                                       sort_by='publishedAt',
                                       page_size=5)

articles = top_headlines['articles']

# Display the news articles
for article in articles:
    print("\n")
    print("TITLE :", article['title'])
    print("DESCRIPTION :", article['description'])
    print("URL :", article['url'])
    print("PUBLISHED AT :", article['publishedAt'])
    print("\n")
    print("-" * 50)  # Separator
