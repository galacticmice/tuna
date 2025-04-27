from trendspy import Trends
from pydantic import BaseModel, Field

tr = Trends()

class Trends(BaseModel):
    region_code: str
    rank: int = Field(ge=1, le=5) # popularity ranking 1 of 5
    keyword: str
    link1: str
    link2: str
    link3: str

GEO_USA = ['US-AL', 'US-AK', 'US-AZ', 'US-AR', 'US-CA', 'US-CO', 'US-CT', 'US-DE', 'US-FL', 'US-GA',
           'US-HI', 'US-ID', 'US-IL', 'US-IN', 'US-IA', 'US-KS', 'US-KY', 'US-LA', 'US-ME', 'US-MD',
           'US-MA', 'US-MI', 'US-MN', 'US-MS', 'US-MO', 'US-MT', 'US-NE', 'US-NV', 'US-NH', 'US-NJ',
           'US-NM', 'US-NY', 'US-NC', 'US-ND', 'US-OH', 'US-OK', 'US-OR', 'US-PA', 'US-RI', 'US-SC',
           'US-SD', 'US-TN', 'US-TX', 'US-UT', 'US-VT', 'US-VA', 'US-WA', 'US-WV', 'US-WI', 'US-WY']

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