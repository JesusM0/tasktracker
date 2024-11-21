import shlex

str = 'update 1 "Buy groceries and cook dinner"'
parsed = shlex.split(str)

command, task_id, task_update = parsed

print(command)
print(task_id)
print(task_update)