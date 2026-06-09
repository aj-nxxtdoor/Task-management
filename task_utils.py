from datetime import datetime

# Import validation functions
from task_manager.validation import validate_task_title, validate_task_description, validate_due_date

# Define tasks list
tasks = []

# Implement add_task function
def add_task(title, description, due_date):
    validate_task_title(title)
    validate_task_description(description)
    validate_due_date(due_date)
    task = {
        "title": title,
        "description": description,
        "due_date": due_date,
        "completed": False
    }
    tasks.append(task)
    print("Task added successfully!")

# Implement mark_task_as_complete function
def mark_task_as_complete(index, tasks=tasks):
    tasks[index]["completed"] = True
    print("Task marked as complete!")

# Implement view_pending_tasks function
def view_pending_tasks(tasks=tasks):
    pending = [task for task in tasks if not task["completed"]]
    if len(pending) == 0:
        print("No pending tasks.")
    else:
        for i, task in enumerate(pending):
            print(f"{i + 1}. {task['title']} - Due: {task['due_date']}")
            print(f"   {task['description']}")

# Implement calculate_progress function
def calculate_progress(tasks=tasks):
    if len(tasks) == 0:
        progress = 0
    else:
        completed = len([task for task in tasks if task["completed"]])
        progress = (completed / len(tasks)) * 100
    return progress
