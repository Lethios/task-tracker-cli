import sys
import os
import json
from datetime import datetime

data_file = "data.json"
if not os.path.exists(data_file):
    with open(data_file, "w") as file:
        json.dump([], file)

if len(sys.argv) == 1:
    print("Welcome to Task Tracker CLI!")
    print("Usage: python task.py <command> [args]")
    print("Commands: add, update.")
    sys.exit(1)

action = str(sys.argv[1])

if len(sys.argv) > 2:
    if len(sys.argv) == 3:
        if sys.argv[2].isdigit():            
            task_id = int(sys.argv[2])
        else:
            task = str(sys.argv[2])
    else:
        task = str(sys.argv[3])
        task_id = int(sys.argv[2])
else:
    task = None

if action == "help":
    print("Welcome to Task Tracker CLI!")
    print("Usage: python task.py <command> [args]")
    print("Commands: add, update.")

if action == "add":
    with open("data.json", "r+") as file:
        data = file.read()

        if data:
            tasks = json.loads(data)
        else:
            tasks = []

        if len(tasks) > 0:
            new_id = tasks[-1]["task_id"] + 1
        else:
            new_id = 1

        tasks.append({"task_id": new_id, "task": task, "created_on": datetime.now().strftime("%d-%m-%Y")})
        file.seek(0)
        json.dump(tasks, file, indent=4)
        file.truncate()

    print(f"Task added successfully. (Task ID: {new_id})")

if action == "update":
    with open("data.json", "r+") as file:
        data = file.read()

        if data:
            tasks = json.loads(data)            
        else:            
            print("No tasks found. Add a task before updating.")
            sys.exit(1)

        task_found = False

        for task in tasks:
            if task["task_id"] == task_id:
                task["task"] = str(sys.argv[3])
                task["updated_on"] = datetime.now().strftime("%d-%m-%Y")
                task_found = True
                break

        if not task_found:
            print(f"No tasks found with ID {task_id}.")
            sys.exit(1)

        file.seek(0)
        json.dump(tasks, file, indent=4)
        file.truncate()

    print(f"Task {task_id} updated successfully.")

if action == "delete":
    with open("data.json", "r+") as file:
        data = file.read()

        if data:
            tasks = json.loads(data)            
        else:            
            print("No tasks found. Add a task before deleting.")
            sys.exit(1)        

        task_found = False

        for task in tasks:
            if task["task_id"] == int(task_id):
                tasks.remove(task)
                task_found = True
                break

        if not task_found:
            print(f"No tasks found with ID {task_id}")
            sys.exit(1)

        file.seek(0)
        json.dump(tasks, file, indent=4)
        file.truncate()

    print(f"Task {task_id} deleted successfully.")
