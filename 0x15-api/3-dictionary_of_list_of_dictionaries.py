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
    ur1 = "https://jsonplaceholder.typicode.com/users/"
    r = requests.get(ur)
    r2 = requests.get(ur1)
    ls = []
    dic = {}

    for user in r2.json():
        for usr in r.json():
            if usr["userId"] == user['id']:
                ls.append(
                        {"task": usr["title"],
                            "completed": usr["completed"],
                            "username": user.get("username")}
                        )
        dic[str(user["id"])] = ls
        ls = []

    with open('todo_all_employees.json', 'w') as f:
        json.dump(dic, f)
