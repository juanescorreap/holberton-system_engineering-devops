#!/usr/bin/python3
"""
Script to export data in the CSV format
"""
import json
import requests
import sys
if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todos_list = []
    tasks_dict = {}
    user_dict = {}
    username = user.get('username')

    for i in todos:
        if i.get('userId') == user.get('id'):
            tasks_dict = {"task": i.get('title'),
                          "completed": i.get('completed'),
                          "username": username},
            todos_list.append(tasks_dict)
    user_dict[sys.argv[1]] = todos_list

    with open('{}.json'.format(sys.argv[1]), 'w') as f:
        json.dump(user_dict, f)
