#!/usr/bin/python3
"""export data to jsonfile"""

import json
import requests
from sys import argv

def main():
    """export data to jsonfile"""
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(user_id)).json()
    username = user.get("username")
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    with open("{}.json".format(user_id), "w") as file:
        json.dump({user_id: [{
            "task": t.get("title"),
            "completed": t.get("completed"),
            "username": username
        } for t in todos]}, file)


if __name__ == "__main__":
    main()
