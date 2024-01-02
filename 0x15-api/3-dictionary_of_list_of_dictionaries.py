#!/usr/bin/python3

"""export data in the JSON format."""

import json
import requests


def main():
    """export data in the JSON format."""
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()

    with open("todo_all_employees.json", "w") as file:
        json.dump({
            u.get("id"): [{
                "task": t.get("title"),
                "completed": t.get("completed"),
                "username": u.get("username")
            } for t in requests.get(url + "todos",
                                    params={"userId": u.get("id")}).json()]
            for u in users}, file)


if __name__ == "__main__":
    main()
