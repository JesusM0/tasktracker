from datetime import datetime
import json
import itertools

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
    new_task = Task(task_string)
    json_object = json.dumps(new_task.__dict__, indent=4)
    
    with open("task_list.json", "w") as outfile:
        outfile.write(json_object)

while(True):
    user_input = input()
    command, *task = user_input.split()
    task_description = " ".join(task)
    
    if(command == 'add'):
        create_task(task_description)
    elif(command in ['Exit', 'exit', 'Quit', 'quit', 'q']):
        exit(1)
        