#!/usr/bin/python3
"""
Script to export data in the  JSON format
"""
import json
import requests
if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users').json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todos_list = []
    user_dict = {}
    tasks_dict = {}

for j in user:
    for i in todos:
        if i.get('userId') == j.get('id'):
            tasks_dict = {"username": j.get('username'),
                          "task": i.get('title'),
                          "completed": i.get('completed')}
            todos_list.append(tasks_dict)
    user_dict[j.get('id')] = todos_list

    with open('todo_all_employees.json', 'w') as f:
        json.dump(user_dict, f)
