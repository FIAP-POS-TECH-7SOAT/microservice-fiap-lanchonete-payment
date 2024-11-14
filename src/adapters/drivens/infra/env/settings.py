from dotenv import load_dotenv
import os

class ENV:

    def __init__(self):
        load_dotenv()
        self.TOKEN_MELI = os.getenv("TOKEN_MELI")
        self.URL_DB = os.getenv("URL_DB")