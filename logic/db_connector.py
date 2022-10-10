import mongodb
from pymongo import MongoClient
from dataclasses import dataclass
from typing import List, Dict

@dataclass()
class MongoConnection:
    connection_string: str

    def __post_init__(self):
        self.client = MongoClient(self.connection_string)

    def __enter__(self):
        return self.client

    def __exit__(self):
        self.client.close()

    # region DB functions
    def create_user(self, user):
        # TODO
        return
    def get_config_from_user(self, user: str) -> List[Dict]:
        # TODO
        return

    def create_new_config(self, user: str, config: Dict) -> bool:
        # TODO
        return
    # endregion
