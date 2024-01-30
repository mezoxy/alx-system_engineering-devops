#!/usr/bin/python3
"""The module: 1-export_to_CSV"""


import csv
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

    for user in r.json():
        if user["userId"] == int(sys.argv[1]):
            ls.append([sys.argv[1], name, str(
                user["completed"]), user["title"]])
    with open(f'{sys.argv[1]}.csv', 'w') as f:
        cf = csv.writer(f, quotechar='"', quoting=csv.QUOTE_NONNUMERIC)
        for lis in ls:
            cf.writerow(lis)
