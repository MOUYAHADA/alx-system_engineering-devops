#!/usr/bin/python3
"""Export to JSON"""
import json
import requests
from sys import argv


if __name__ == "__main__":
    """Gather data from an API"""
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users").json()
    todo = requests.get(url + "todos").json()

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(
            {
                user[i].get("id"): [
                    {
                        "task": task.get("title"),
                        "completed": task.get("completed"),
                        "username": user[i].get("username"),
                    }
                    for task in todo
                    if task.get("userId") == user[i].get("id")
                ]
                for i in range(len(user))
            },
            jsonfile,
        )
