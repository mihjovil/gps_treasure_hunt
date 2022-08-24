import mongodb
from dataclasses import dataclass

@dataclass
class MongoConnection:
    connection_string: str

    def __post_init__(self):
        # TODO
        return
