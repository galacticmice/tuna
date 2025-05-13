import os
from dotenv import load_dotenv
from appwrite.client import Client
from appwrite.services.databases import Databases
from .models import GEO_USA
from .database import add_entry
from .trends import trend_data

load_dotenv()

client = Client()
client.set_endpoint(os.getenv('APPWRITE_ENDPOINT'))
client.set_project(os.getenv('APPWRITE_PROJECT_ID'))
client.set_key(os.getenv('APPWRITE_TUNA_DB_API_KEY'))

databases = Databases(client)

"""
This file is only used for testing or initialization purposes.
                    DO NOT USE IN PRODUCTION
It wipes the entire trend data table and repopulates it with new data.
"""

def wipe_table():
    existing_entries = databases.list_documents(
        database_id=os.getenv('APPWRITE_DATABASE_ID'),
        collection_id=os.getenv('APPWRITE_TREND_DATA_TABLE'),
        queries=[]
    )['documents']
    for document in existing_entries:
        databases.delete_document(
            os.getenv('APPWRITE_DATABASE_ID'),
            os.getenv('APPWRITE_TREND_DATA_TABLE'),
            document['$id']
        )

def populate_table():
    for code in GEO_USA:
        for i in range(5):
            o = trend_data(code, i)
            add_entry(o)


wipe_table()
populate_table()