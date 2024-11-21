from datetime import datetime
import json
import itertools
import shlex
import os

cur_id = 0

class Task:
    id_iter = itertools.count(start=1)
    date_time = datetime.now()
    format = '%d-%m-%Y %H:%M'
    
    def __init__(self, description, status="NEW"):
        self.id = next(self.id_iter)
        self.description = description
        self.status = status
        self.createdAt = self.date_time.strftime(self.format)
        self.updatedAt = self.date_time.strftime(self.format)


def create_task(task):
    task_string = task.strip('"')
    new_task = Task(task_string).__dict__
    try:
        with open("task_list.json", "r") as infile:
            tasks = json.load(infile)
    except (FileNotFoundError, json.JSONDecodeError):
        tasks = []
    tasks.append(new_task)
    
    with open("task_list.json", "w") as outfile:
        json.dump(tasks,outfile, indent=4)

def update_task(id, update):
    with open('task_list.json', 'r') as f:
        tasks = json.load(f)

    field_key = int(id)
    task_found = False

    for task in tasks:
        if task["id"] == field_key:
            task["description"] = update
            task["updatedAt"] = datetime.now().strftime(Task.format)
            task_found = True
            break
    
    if not task_found:
        print(f'Task with ID {id} does not exist.')
        return
    
    with open("task_list.json", "w") as f:
        json.dump(tasks, f, indent=4)

def delete_task(id):
    new_data = []
    with open('task_list.json', 'r') as f:
        tasks = json.load(f)
    
    field_key = int(id)
    
    for task in tasks:
        if task['id'] == field_key:
            pass
        else:
            new_data.append(task)
    
    with open("task_list.json", "w") as f:
        json.dump(new_data, f, indent=4)
            
def mark_task(status, id):
    if status == 'mark-in-progress':
        status = 'in-progress'
    elif status == 'mark-done':
        status = 'done'
    with open('task_list.json', 'r') as f:
        tasks = json.load(f)
    
    field_key = int(id)
    task_found = False

    for task in tasks:
        if task["id"] == field_key:
            task["status"] = status
            task_found = True
            break
    
    if not task_found:
        print(f'Task with ID {id} does not exist.')
        return
    
    with open("task_list.json", "w") as f:
        json.dump(tasks, f, indent=4)

while(True):
    user_input = input()
    command, *task = user_input.split()
    
    if(command == 'add'):
        task_description = " ".join(task)
        create_task(task_description)
    elif(command == 'update'):
        task_description = " ".join(task)
        parsed = shlex.split(task_description)
        task_id, task_update = parsed
        update_task(task_id, task_update)
    elif(command == 'delete'):
        task_description = " ".join(task)
        delete_task(task_description)
    elif(command in ['mark-in-progress', 'mark-done']):
        task_description = " ".join(task)
        mark_task(command, task_description)
    elif(command in ['Exit', 'exit', 'Quit', 'quit', 'q']):
        os.remove("task_list.json")
        exit(1)
        