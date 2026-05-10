import os
import httpx
from dotenv import load_dotenv
from entity.news import Article, NewsResponse
from bs4 import BeautifulSoup

load_dotenv()
valid_keys = Article.__annotations__.keys()


def fetchNewsContent(searchText=""):
    apiKey = os.getenv("NEWS_DATA_API_KEY")
    url = "https://newsdata.io/api/1/news"

    params = {"apikey": apiKey, "q": searchText.lower()}

    response = httpx.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        articles = []

        results = data.get("results", [])
        for item in results:
            article = {k: v for k, v in item.items() if k in valid_keys}
            content_article = fetchArticleContent(article.get("link"))
            article["content"] = content_article
            article_obj = Article(**article)
            articles.append(article_obj)

        return NewsResponse(
            status=data["status"],
            totalResults=data["totalResults"],
            results=articles,
        )
    else:
        print(f"Error: {response.status_code}")
        return None


def fetchArticleContent(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    try:
        response = httpx.get(
            url,
            headers=headers,
            follow_redirects=True,
        )
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")

            paragraphs = soup.find_all("p")
            content = "\n".join([p.get_text() for p in paragraphs])
            return content
        else:
            return f"Could not fetch: Status: {response.status_code}"
    except Exception as e:
        return f"Error scraping: {str(e)}"
