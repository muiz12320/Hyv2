# (c) @abbu_yt7
import os
from os import getenv, environ



class Config:
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    TOKEN = os.environ.get("TOKEN")
    START_PIC = os.environ.get("START_PIC")
    CHAT = os.environ.get("CHAT")
