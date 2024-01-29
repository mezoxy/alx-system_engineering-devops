#!/usr/bin/python3
"""The module: 0-gather_data_from_an_API"""


from json import loads
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
    j = 0
    st = ""
    name = r2.json().get("name")
    i = 0

    for user in r.json():
        if user["userId"] == int(sys.argv[1]):
            if user["completed"]:
                j += 1
                st += user["title"] + "$"
            i += 1

    print("Employee {} is done with tasks({}/{}):".format(name, j, i))
    for task in st.split("$")[:-1]:
        print("\t {}".format(task))
