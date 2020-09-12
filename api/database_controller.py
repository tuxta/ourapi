import json
import sqlite3


class DatabaseController:
    def __init__(self):
        self.db = None
        self.cursor = None
        self.db = sqlite3.connect('api_db.sqlite')
        self.db.row_factory = sqlite3.Row
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def run_query(self, query_string, arguments):
        self.cursor.execute(query_string, arguments)
        query_result = self.cursor.fetchall()
        rows = []
        results = {'results': rows}
        for row in query_result:
            results['results'].append(dict(row))

        return json.dumps(results)
