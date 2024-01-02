#!/usr/bin/python3

""" extend Python script to export data in the CSV format."""

import requests
from sys import argv


def main(id):
    """check user details passed in argv"""
    url = "https://jsonplaceholder.typicode.com/todos"
    response = requests.get(url)
    data = response.json()
    employee_id = argv[1]

    employee_name = requests.get(
        "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    ).json().get('username')

    with open("{}.csv".format(employee_id), "w") as f:
        for task in data:
            if task.get('userId') == int(employee_id):
                f.write('"{}","{}","{}","{}"\n'.format(
                    task.get('userId'),
                    employee_name,
                    task.get('completed'),
                    task.get('title')
                ))


if __name__ == "__main__":
    main()
