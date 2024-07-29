#!/usr/bin/python3
"""python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress."""
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

    # export data to CSV
    with open("{}.csv".format(user_id), "w") as csvfile:
        for task in todo:
            csvfile.write(
                '"{}","{}","{}","{}"\n'.format(
                    user_id,
                    user.get("username"),
                    task.get("completed"),
                    task.get("title"),
                )
            )
