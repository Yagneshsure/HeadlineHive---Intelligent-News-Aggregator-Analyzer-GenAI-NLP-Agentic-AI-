from gnews import GNews

google_news = GNews(language='en', country='IN')

# Search for "Artificial Intelligence"
news = google_news.get_news('Artificial Intelligence')

for item in news[:5]:
    print(item['title'])
    print(item['url'])
    print(item['published date'])
    print("-" * 80)
