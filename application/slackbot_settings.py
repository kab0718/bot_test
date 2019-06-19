import os
from pathlib import  Path
from dotenv import load_dotenv
load_dotenv(verbose=True)
load_dotenv(dotenv_path = Path('.') / '.env')

API_TOKEN = os.getenv("API_KEY")

default_reply = "すいません。よくわかりませんでした"

PLUGINS = [
    'plugins'
]