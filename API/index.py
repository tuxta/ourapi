#!/usr/bin/env python3

from random import randint

ran_num = randint(1, 10)
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
