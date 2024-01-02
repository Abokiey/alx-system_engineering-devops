#!/usr/bin/python3

""" request data from an api"""

import requests
from sys import argv


def main():
    """check user id passed in agv"""

    url = "https://jsonplaceholder.typicode.com/todos"
    resp = requests.get(url)
    data = resp.json()
    completed_tasks = 0
    total_tasks = 0
    tasks = []
    employee_id = argv[1]

    for task in data:
        if task.get('userId') == int(employee_id):
            total_tasks += 1
            if task.get('completed'):
                completed_tasks += 1
                tasks.append(task.get('title'))

    url = "https://jsonplaceholder.typicode.com/users/{}".format(employee_id)
    name = requests.get(url).json().get('name')

    print("Employee {} is done with tasks({}/{}):".format(
        name, completed_tasks, total_tasks))
    for task in tasks:
        print("\t {}".format(task))


if __name__ == "__main__":
    main()
