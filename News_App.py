import requests
from config import API_KEY

class NewsAPI:
    def __init__(self, api_key):
        self.base_url = "https://newsapi.org/v2/everything"
        self.api_key = api_key

    def get_latest_news(self, company_name, page_size=5):
        """
        Fetch the latest news articles based on the company name.

        Args:
        - company_name (str): The name of the company to fetch news for.
        - page_size (int): The number of articles to fetch. Default is 5.

        Returns:
        - List[dict]: A list of dictionaries containing article data.
        """
        params = {
            "q": company_name,
            "pageSize": page_size,
            "apiKey": self.api_key
        }

        response = requests.get(self.base_url, params=params)
        data = response.json()

        if data["status"] == "ok":
            return data["articles"]
        else:
            return []

def main():
    news_api = NewsAPI(API_KEY)
    
    company_name = input("Enter the stock company name: ")
    articles = news_api.get_latest_news(company_name)
    
    if not articles:
        print(f"No news articles found for {company_name}.")
        return

    print(f"Latest news articles for {company_name}:\n")
    for article in articles:
        print(article["title"])
        print(article["description"])
        print(article["url"])
        print("-" * 50)

if __name__ == "__main__":
    main()
