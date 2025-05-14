from trendspy import Trends
from .models import RegionData

tr = Trends()


def trend_data(region: str, i: int, categoryID: int):
    """
    get trending data for region+rank and return as RegionData object for database
        Args:
            region (str): Region code (e.g., 'US-CA')
            i (int): Rank of the trend (0-4)
            categoryID: Category ID (politics category = 396)
        Returns:
            RegionData: Object containing region code, rank, keyword, and links to articles
    """
    # Wrapped the trend_data function in a try block to catch all errors. Previously had to catch for diff errors in diff places
    try:
        # trends = tr.trending_now(geo=region).filter_by_topic(topic=categoryID)
        trends = tr.trending_now(geo=region)

        # Added a check if no data is returned
        if not trends or i >= len(trends):
            print(
                f"No trending data for region {region} at category [].")
            return None

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
    # The except block catches any kind of error and returns None, which allows for displaying the error in the dialog box (check is in llm.py)
    except Exception as e:
        print(f"Error retrieving document for region {region}, rank {i}: {e}")
        return None
