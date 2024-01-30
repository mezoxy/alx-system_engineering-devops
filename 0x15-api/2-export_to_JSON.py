#!/usr/bin/python3
"""The module: 1-export_to_CSV"""


import csv
import json
import requests
import sys


if __name__ == "__main__":
    """
        A  Python script that, using this REST API, for a given
        employee ID, returns information about his/her TODO list progress.
    """
    ur = "https://jsonplaceholder.typicode.com/todos/"
    ur1 = "https://jsonplaceholder.typicode.com/users/" + sys.argv[1]
    r = requests.get(ur)
    r2 = requests.get(ur1)
    name = r2.json().get("username")
    ls = []
    dic = {}

    for user in r.json():
        if user["userId"] == int(sys.argv[1]):
            ls.append(
                    {"task": user["title"],
                        "completed": user["completed"],
                        "username": name}
                    )

    dic[sys.argv[1]] = ls
    with open(f'{sys.argv[1]}.json', 'w') as f:
        json.dump(dic, f)
