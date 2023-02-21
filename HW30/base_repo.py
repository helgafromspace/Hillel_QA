import sqlite3

from helper_config import get_db_path


class BaseRepository:

    def __init__(self,db_path):
        path = get_db_path()
        self._connection = sqlite3.connect(f'{path}book.db', isolation_level=None)
        self._cursor = self._connection.cursor()
