from trendspy import Trends

tr = Trends()


# this combination works
trends = tr.trending_now(geo='US-MA')
news = tr.trending_now_news_by_ids(
    trends[2].news_tokens,  # News tokens from trending topic
    max_news=3  # Number of articles to retrieve
)

print(news[0].url)
print(news[1].url)
print(news[2].url)

# if NULL, don't call summarize API

# test
print(trends[2].keyword)