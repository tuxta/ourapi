#!/usr/bin/env python3

from random import randint
import json

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

return_json = json.dumps(data)
print(return_json)
# print(json.dumps(data))
print("""
<html>
  <head>
      <title>Our API</title>
  </head>
  <body>
    <p style="font-weight:bold; text-align:center;">
      Our API - now dynamic :-)
    </p>
    <p style="text-align:center">
      Our random number is: {}
    </p>
  </body>
</html>
""".format(ran_num)
      )