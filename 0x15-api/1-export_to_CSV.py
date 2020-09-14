#!/usr/bin/python3
"""extend Python from tasl 0 script to export data in the CSV format."""

import csv
import requests
from sys import argv

if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(argv[1])).json()
    todos_list = requests.get(url + "todos",
                              params={"userId": argv[1]}).json()

    with open('{}.csv'.format(user_id), mode='w', newline="") as f:
        progress_writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for t in todos_list:
            progress_writer.writerow([int(user_id), user.get('username'),
                                      t.get('completed'), t.get('title')])
