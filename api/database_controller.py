import json
import sqlite3


class DatabaseController:
    def __init__(self):
        self.db = None
        self.cursor = None
        self.db = sqlite3.connect('api_db.sqlite')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def run_query(self, query_string, arguments):
        self.cursor.execute(query_string, arguments)
        questions_list = self.cursor.fetchall()
        results = json.dumps(questions_list)

        return results
