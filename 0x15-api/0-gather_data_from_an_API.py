#!/usr/bin/python3
"""The module: 0-gather_data_from_an_API"""


import requests
import sys
from json import loads


ur = "https://jsonplaceholder.typicode.com/todos/"
r = requests.get(ur)
j = 0
st = ""
name = ""
i = 0

for user in r.json():
    if user["userId"] == int(sys.argv[1]):
        name = user.get("name")
        if user["completed"]:
            j += 1
            st += user["title"] + "$"
        i += 1

print("Employee {} is done with tasks({}/{}):".format(name, j, i))
for task in st.split("$")[:-1]:
    print("\t{}".format(task))
