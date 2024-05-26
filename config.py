import os
from dotenv import load_dotenv
load_dotenv()
BOT_TOKEN = os.getenv("API_KEY_TG")
CMC_TOKEN = os.getenv("CMC_API_KEY")
CryptoAPI_TOKEN = os.getenv("")