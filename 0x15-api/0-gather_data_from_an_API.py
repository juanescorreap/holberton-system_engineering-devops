#!/usr/bin/python3
import requests
import sys
"""Python script that, using a REST API,
for a given employee ID, returns information
about his/her TODO list progress"""

if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_todos = 0
    completed = 0
    todos_list = []

    for i in todos:
        if i.get('userId') == user.get('id'):
            user_todos = user_todos + 1
            if i.get('completed') is True:
                completed = completed + 1
                todos_list.append(i)

    print("Employee {} is done with tasks({}/{}):".format(user.get('name'),
          completed, user_todos))
    for j in todos_list:
        print("\t{}".format(j.get('title')))
