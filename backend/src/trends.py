from trendspy import Trends
from .models import RegionData

tr = Trends()

def trend_data(region: str, i: int):
    """get trending data for region+rank and return as RegionData object for database

        Args:
            region (str): Region code (e.g., 'US-CA')
            i (int): Rank of the trend (0-4)
        Returns:
            RegionData: Object containing region code, rank, keyword, and links to articles
    """
    trends = tr.trending_now(geo=region)
    news = tr.trending_now_news_by_ids(
        trends[i].news_tokens,  # News tokens from trending topic
        max_news=3  # Number of articles to retrieve
    )
    obj = RegionData(
        region_code=region,
        rank=i,
        keyword=trends[i].keyword,
        link1=news[0].url,
        link2=news[1].url,
        link3=news[2].url
    )
    return obj


