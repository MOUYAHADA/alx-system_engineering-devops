#!/usr/bin/python3
"""python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """get data from API"""
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

    with open("{}.json".format(user_id), "w") as jsonfile:
        jsonfile.write(
            json.dumps(
                {
                    user_id: [
                        {
                            "task": task.get("title"),
                            "completed": task.get("completed"),
                            "username": user.get("username"),
                        }
                        for task in todo
                    ]
                }
            )
        )
