#!/usr/bin/python3
"""
Script to export data in the CSV format
"""
import csv
import requests
import sys
if __name__ == "__main__":

    user = requests.get('https://jsonplaceholder.typicode.com/users/{}'
                        .format(sys.argv[1])).json()
    todos = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    user_todos = 0
    completed = 0
    todos_list = []
    tasks_list = []

    for i in todos:
        if i.get('userId') == user.get('id'):
            user_todos = user_todos + 1
            tasks_list.append(i)
            if i.get('completed') is True:
                completed = completed + 1
                todos_list.append(i)

    username = user.get('username')
    f = open('{}.csv'.format(sys.argv[1]), 'w')
    try:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)
        for k in tasks_list:
            writer.writerow((k.get('userId'), username,
                            k.get('completed'), k.get('title')))
    finally:
        f.close()
