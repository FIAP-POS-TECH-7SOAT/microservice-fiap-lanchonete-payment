from flask_sqlalchemy import SQLAlchemy

class Config:
    def __init__(self):
        self.db = SQLAlchemy()
        
    def load(self):
        pass