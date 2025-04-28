import os
from dotenv import load_dotenv
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from appwrite.query import Query
from models import RegionData, GEO_USA

load_dotenv()

client = Client()
client.set_endpoint(os.getenv('APPWRITE_ENDPOINT'))
client.set_project(os.getenv('APPWRITE_PROJECT_ID'))
client.set_key(os.getenv('APPWRITE_TUNA_DB_API_KEY'))

databases = Databases(client)

async def add_entry(trend: RegionData):
    """add entry (for initialization only)

    Args:
        trend (RegionData): Object containing region code, rank, keyword, and links to articles
    """
    try:
        databases.create_document(
            database_id=os.getenv('APPWRITE_DATABASE_ID'),
            collection_id=os.getenv('APPWRITE_TREND_DATA_TABLE'),
            document_id=ID.unique(),
            data={
                'region_code': trend.region_code,
                'rank': trend.rank,
                'keyword': trend.keyword,
                'link1': trend.link1,
                'link2': trend.link2,
                'link3': trend.link3
            }
        )
    except Exception as e:
        print(f"Error adding document: {e}")

async def get_entry(region: str, rank: int):
    """Get single unique entry with specific region+rank key

    Args:
        region (str): Region code (e.g., 'US-CA')
        rank (int): Rank of the trend (1-5)

    Returns:
        dict: Document containing region code, rank, keyword, and links to articles
    """
    try:
        result = databases.list_documents(
            database_id=os.getenv('APPWRITE_DATABASE_ID'),
            collection_id=os.getenv('APPWRITE_TREND_DATA_TABLE'),
            queries=[
                Query.and_queries([
                    Query.equal("region_code", region),
                    Query.equal("rank", rank)
                ])
            ]
        )
        return result['documents'][0] # return only first document, result should only contain 1 anyways
    except Exception as e:
        print(f"Error retrieving document: {e}")
        return None

# example result of get_entry, in JSON
# {
#     "total": 5,
#     "documents": [
#         {
#             "$id": "5e5ea5c16897e", ## ID HERE
#             "$collectionId": "5e5ea5c15117e",
#             "$databaseId": "5e5ea5c15117e",
#             "$createdAt": "2020-10-15T06:38:00.000+00:00",
#             "$updatedAt": "2020-10-15T06:38:00.000+00:00",
#             "$permissions": [
#                 "read(\"any\")"
#             ]
#         }
#     ]
# }

async def update_entry(trend: RegionData):
    """update entry based on region+rank

    Args:
        trend (RegionData): Object containing region code, rank, keyword, and links to articles
    """
    entry = get_entry(trend.region_code, trend.rank)
    if entry is not None:
        document_id = entry['$id'] # document ID from resultset
        try:
            databases.update_document(
                database_id=os.getenv('APPWRITE_DATABASE_ID'),
                collection_id=os.getenv('APPWRITE_TREND_DATA_TABLE'),
                document_id=document_id,
                data={
                    'keyword': trend.keyword,
                    'link1': trend.link1,
                    'link2': trend.link2,
                    'link3': trend.link3
                }
            )
            print(f"Successfully updated document {document_id}")
        except Exception as e:
            print(f"Error updating document {document_id}: {e}")
    else:
        print(f"No document found for region {trend.region_code} and rank {trend.rank}. Cannot update.")
