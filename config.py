import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY", "your_secret_key")
    GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", "your_client_id")
    GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", "your_client_secret")
