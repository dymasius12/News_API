from newsapi import NewsApiClient
from config import API_KEY

# Initialize the client
newsapi = NewsApiClient(api_key=API_KEY)

# Ask the input
company_name = input("Enter the stock company name: ")

# Get top headlines for a specific query (e.g., a company name)
top_headlines = newsapi.get_top_headlines(q=company_name,
                                          language='en',
                                          country='us')

articles = top_headlines['articles']

# Display the news articles
for article in articles:
    print("Title:", article['title'])
    print("Description:", article['description'])
    print("URL:", article['url'])
    print("Published At:", article['publishedAt'])
    print("-" * 50)  # Separator
