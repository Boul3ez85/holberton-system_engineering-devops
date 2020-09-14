#!/usr/bin/python3
"""extend Python script from tasl 0 to export data in the json format."""

import json
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos_list = requests.get(url + "todos",
                              params={"userId": argv[1]}).json()

    with open('{}.json'.format(user_id), 'w') as f:
        json.dump({user_id: [{
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": task.get("username")
            } for task in todos_list]}, f)
