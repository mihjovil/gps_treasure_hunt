import mongodb
from pymongo import MongoClient
from dataclasses import dataclass

@dataclass
class MongoConnection:
    connection_string: str

    def __post_init__(self):
        self.client = MongoClient(self.connection_string)

    def __enter__(self):
        return self.client

    def __exit__(self):
        self.client.close()
