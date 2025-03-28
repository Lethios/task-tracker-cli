# Task Tracker CLI  

Task Tracker CLI is a simple command-line tool for managing tasks efficiently.  
Users can add, update, delete, list, and track the status of tasks.  
Tasks are stored in a JSON file (`data.json`) to ensure persistence between runs.  

## Features  
✔ Add new tasks  
✏ Update existing tasks  
❌ Delete tasks  
📋 List all tasks (with optional filtering by status)  
🚀 Mark tasks as "in progress"  
✅ Mark tasks as "done"  
💾 Tasks persist using JSON storage  

---

## Installation  

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Lethios/task-tracker-cli.git
   cd task-tracker-cli
2. **Ensure Python is installed (Python 3.x recommended).**
 
---

## Usage
Run the program using Python:
```bash
python task-cli.py <command> [arguments]
```

## Available Commands

| Command                         | Description                                | Example Usage                                      |
|---------------------------------|--------------------------------------------|----------------------------------------------------|
| `add "<task>"`                  | Add a new task                             | `python task-cli.py add "Complete report"`    |
| `update <task_id> "<task>"`     | Update an existing task                    | `python task-cli.py update 1 "Submit report"` |
| `delete <task_id>`              | Delete a task                              | `python task-cli.py delete 2`                 |
| `list`                          | List all tasks                             | `python task-cli.py list`                     |
| `list <status>`                 | List tasks by status (`todo`, `in-progress`, `done`)      | `python task-cli.py list done` |
| `mark-in-progress <task_id>`    | Mark a task as "in progress"               | `python task-cli.py mark-in-progress 3`       |
| `mark-done <task_id>`           | Mark a task as "done"                      | `python task-cli.py mark-done 3`              |
| `help`                          | Display the help message                   | `python task-cli.py help`                     |

## Author

**Lethios**
- Github: [@Lethios](https://github.com/Lethios)
- Twitter: [@LethiosDev](https://x.com/LethiosDev)

## License

Copyright © 2025 [Lethios](https://github.com/Lethios).  
This project is licensed under the [MIT License](LICENSE).
