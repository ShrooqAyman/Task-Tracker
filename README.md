# 📝 Task Tracker CLI

A simple and lightweight command-line interface (CLI) tool to help you manage your tasks. Easily add, update, delete, and track the progress of your tasks directly from the terminal.

## 🚀 Features

- Add new tasks  
- Update task descriptions  
- Delete tasks  
- Mark tasks as `in-progress` or `done`  
- List all tasks  
- Filter tasks by status (`todo`, `in-progress`, or `done`)  
- Data is persisted in a local JSON file  
- No external libraries required  

## 📁 File Structure

```bash
.
├── TaskTracker.py       # Core task management logic
├── helper.py            # Custom exceptions and helpers
├── main.py              # CLI entry point
├── tasks.json           # JSON file to store task data (auto-created)
└── README.md            # This file
```

## ⚙️ Requirements
- Python 3.x

- No external dependencies

## 📦 Installation
Clone this repository and navigate to the project directory:
```bash
git clone https://github.com/ShrooqAyman/Task-Tracker.git
```
```bash
cd Task-Tracker
```
## 📌 Commands
### ➕ Add a new task
```bash
python main.py add "Buy groceries"
```
### 📝 Update an existing task
```bash
python main.py update <task_id> "New task description"
```

### ❌ Delete a task
```bash
python main.py delete <task_id>
```

### 📃 List all tasks (or filter by status)
```bash
python main.py list                # List all tasks
python main.py list todo          # List only tasks that are 'todo'
python main.py list done          # List only tasks that are 'done'
python main.py list in-progress   # List only tasks that are 'in-progress'
```

### 🚧 Mark a task as in-progress
```bash
python main.py mark-in-progress <task_id>
```

### ✅ Mark a task as done
```bash
python main.py mark-done <task_id>
```

## 🧠 How It Works
- All task data is stored in a tasks.json file in the same directory.

- The file is automatically created if it doesn't exist.

- Each task includes an ID, description, and status (todo, in-progress, done).

- The CLI uses Python’s built-in argparse module to handle command-line arguments.

## 🛠 Error Handling
- Gracefully handles missing files, invalid task IDs, and invalid inputs.

- Provides meaningful error messages for better user experience.

📄 Example JSON Structure
```json
[
  {
    "id": 1,
    "description": "Buy groceries",
    "status": "todo"
  },
  {
    "id": 2,
    "description": "Finish CLI project",
    "status": "in-progress"
  }
]
```
