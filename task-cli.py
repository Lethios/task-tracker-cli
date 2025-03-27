import sys
import json
from datetime import datetime

if len(sys.argv) == 1:
    print("Welcome to Task Tracker CLI!")
    print("Usage: python task.py <command> [arguments]")
    print("Commands: add")
    sys.exit(1)

action = str(sys.argv[1])

if len(sys.argv) > 2:
    task = str(sys.argv[2])
else:
    task = None    

if action == "help":
    print("Welcome to Task Tracker CLI!")
    print("Usage: python task.py <command> [arguments]")
    print("Commands: add")

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

        tasks.append({"task_id": new_id, "task": task, "created_at": datetime.now().strftime("%H:%M on %d-%m-%Y")})
        file.seek(0)
        json.dump(tasks, file, indent=4)
        file.truncate()

    print(f"Task added successfully. (Task ID: {new_id})")
