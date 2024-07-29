#!/usr/bin/python3
"""Script that returns employee information using their ID"""
from sys import argv
import requests


if __name__ == "__main__":
    """fetch data"""

    url = "https://jsonplaceholder.typicode.com/"
    user_id = argv[1]
    user = requests.get(url + "users/{}".format(user_id)).json()
    todo = requests.get(url + "todos?userId={}".format(user_id)).json()
    completed = []
    for task in todo:
        if task.get("completed") is True:
            completed.append(task.get("title"))
    print(
        "Employee {} is done with tasks({}/{}):".format(
            user.get("name"), len(completed), len(todo)
        )
    )

    for task in completed:
        print("\t {}".format(task))
