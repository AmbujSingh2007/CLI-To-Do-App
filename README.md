# CLI To-Do App

A simple command-line based To-Do List application built with Python.

This project allows users to:

- Add tasks
- View tasks
- Update task status
- Clear all tasks
- Store tasks permanently using JSON

---

## Features

### Add Tasks
Users can add multiple tasks at once.

### View Tasks
Displays all tasks with:

- Task ID
- Task Name
- Task Status

### Update Task Status
Mark tasks as **Completed**

### Clear All Tasks
Deletes all saved tasks

### Persistent Storage
Tasks are saved in a `tasks.json` file using JSON

---

## Tech Stack

- **Python 3**
- **JSON**
- **OS Module**

---

## Project Structure

```bash
cli-to-do-app/
│
├── main.py
├── tasks.json
└── README.md
```

---

## How to Run

### Clone Repository

```bash
git clone https://github.com/yourusername/cli-to-do-app.git
```

### Move Into Project Directory

```bash
cd cli-to-do-app
```

### Run Application

```bash
python main.py
```

---

## Menu Interface

```text
---------- To-Do Menu ----------
(1) Add Task
(2) Flush All Tasks
(3) View Tasks
(4) Update Task Status
(5) Exit
--------------------------------
```

---

## Example Output

### Adding Tasks

```text
Number of tasks you want to add: 2
Enter Name for Task 1: Learn Python
Enter Name for Task 2: Build Project
```

### Viewing Tasks

```text
ID: 1 | Name: Learn Python | Status: Pending
ID: 2 | Name: Build Project | Status: Pending
```

### Updating Task

```text
Enter Task ID for which you want to update Status: 1
```

Updated:

```text
ID: 1 | Name: Learn Python | Status: Completed
```

---

# Problems Faced During Development

## 1. File Not Found Error

### Problem
When running for the first time, `tasks.json` did not exist.

### Solution
Used:

```python
try:
    with open(FILENAME, 'r') as f:
        return json.load(f)
except FileNotFoundError:
    return []
```

This ensures the program starts with an empty task list.

---

## 2. JSON Decode Error

### Problem
If `tasks.json` was corrupted or empty, program crashed.

### Solution

Handled:

```python
json.JSONDecodeError
```

Now invalid JSON returns an empty list safely.

---

## 3. Managing Unique Task IDs

### Problem
New tasks needed unique IDs.

### Solution

Tracked last task ID:

```python
last_id = tasks[-1]['id'] if tasks else 0
```

Then incremented for new tasks.

---

## 4. Input Validation

### Problem
Users could enter invalid menu choices.

### Solution

Validated input:

```python
if choice in ["1", "2", "3", "4", "5"]:
```

---

## 5. Saving Data Permanently

### Problem
Tasks disappeared after program closed.

### Solution

Stored data in JSON using:

```python
json.dump(tasks, f, indent=4)
```

---

## 6. Updating Task Status

### Problem
Needed to locate task by ID.

### Solution

Looped through tasks and matched IDs:

```python
if int(i['id']) == int(tid):
```

Then updated:

```python
i['status'] = "Completed"
```

---

# What I Learned

Through this project I learned:

- File handling in Python
- JSON read/write operations
- Exception handling
- Functions and modular code
- Input validation
- CLI application structure
- Data persistence

---

## Future Improvements

Planned upgrades:

- Delete single task
- Edit task name
- Add task deadlines
- Priority levels
- Search tasks
- Colored terminal output
- Better input validation loops

---

## Author

Built by **Ambuj**

Learning by building practical Python projects.
