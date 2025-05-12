import os
from dotenv import load_dotenv
from appwrite.client import Client
from appwrite.services.databases import Databases
from appwrite.id import ID
from appwrite.query import Query
from models import SummarizedData

load_dotenv()

client = Client()
client.set_endpoint(os.getenv('APPWRITE_API_URL'))
client.set_project(os.getenv('APPWRITE_PROJECT_ID'))
client.set_key(os.getenv('APPWRITE_TUNA_DB_API_KEY'))

databases = Databases(client)

def add_entry(result: SummarizedData):
    """add entry (for initialization only)

    Args:
        result (RegionData): Object containing region code, rank, keyword, and links to articles
    """
    try:
        databases.create_document(
            database_id=os.getenv('APPWRITE_DATABASE_ID'),
            collection_id=os.getenv('APPWRITE_TREND_DATA_TABLE'),
            document_id=ID.unique(),
            data={
                'region_code': result.region_code,
                'summaries': result.summ
            }
        )
    except Exception as e:
        print(f"Error adding document: {e}")

def get_entry(region: str):
    """Get single unique entry with specific region+rank key

    Args:
        region (str): Region code (e.g., 'US-CA')
        rank (int): Rank of the result (1-5)

    Returns:
        dict: Document containing region code, rank, keyword, and links to articles
    """
    try:
        result = databases.list_documents(
            database_id=os.getenv('APPWRITE_DATABASE_ID'),
            collection_id=os.getenv('APPWRITE_TREND_DATA_TABLE'),
            queries=[
                Query.equal("region_code", region)
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