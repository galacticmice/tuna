import os
from dotenv import load_dotenv

load_dotenv()

URL = os.getenv('POSTGRESURL')
KEY = os.getenv('POSTGRESAPI')

