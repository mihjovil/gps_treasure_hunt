import mongodb
from dataclasses import dataclass

@dataclass
class MongoConnection:
    connection_string: str

    def __post_init__(self):
        self.conn = mongodb.MongoConnection(self.connection_string)
        # TODO add the connection

    def __enter__(self):
        return self

    def __exit__(self):
        self.conn.close()
