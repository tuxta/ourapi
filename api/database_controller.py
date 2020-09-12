import json
import sqlite3
from random import randint


class DatabaseController:
    def __init__(self):
        self.db = None
        self.cursor = None

    def connect(self):
        self.db = sqlite3.connect('api_db.sqlite')
        self.cursor = self.db.cursor()

    def __del__(self):
        self.db.close()

    def run_query(self, query_string, arguments):
        return self.dummy_result()
        #self.cursor.execute(query_string, arguments)
        #questions_list = self.cursor.fetchall()
        #results = json.dumps(questions_list)

        #return results


    def dummy_result(self):
        ran_num = randint(1, 10)

        data = {'data':
                [
                    {
                        'name': 'Harry',
                        'age': 24,
                        'sex': 'Male'
                    },
                    {
                        'name': 'Sally',
                        'age': 22,
                        'sex': 'Female'
                    }
                ],
            'Random': ran_num
                }

        return data
