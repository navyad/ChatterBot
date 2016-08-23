import os
import sqlite3
from chatterbot.adapters.storage import StorageAdapter


class SqliteDatabaseAdapter(StorageAdapter):

    def __init__(self, **kwargs):
        super(SqliteDatabaseAdapter, self).__init__(**kwargs)
        self.database_file = self.kwargs.get(
            "database_file", "sqlite.db"
        )
        sqlite3.connect(self.database_file)

    def count(self):
        """
        Return the number of entries in the database.
        """
        pass

    def drop(self):
        """
        Drop the database
        """
        if os.path.exists(self.database_file):
            os.remove(self.database_file)
