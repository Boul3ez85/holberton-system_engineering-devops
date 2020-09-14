#!/usr/bin/python3
"""extend Python script from tasl 0 to export data in the json format."""

import json
import requests

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open('todos_all_employees.json', 'w') as f:
        json.dump({i.get('id'): [{
                "username": i.get('username'),
                "task": task.get("title"),
                "completed": task.get("completed")
            } for task in requests.get(url + "todos",
                                       params={"userId": i.get('id')}).json()]
            for i in users}, f)
