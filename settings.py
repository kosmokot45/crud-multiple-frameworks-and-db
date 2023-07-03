import os
from dotenv import load_dotenv

load_dotenv()

mongodb_host = os.getenv('MONGO_DB_HOST')
mongodb_port = os.getenv('MONGO_DB_PORT')

print(mongodb_host, mongodb_port)