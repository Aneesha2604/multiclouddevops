# Simple To-Do List using a Python dictionary

# Initialize an empty dictionary to store tasks
todo_list = {}

# Function to display the to-do list
def show_tasks():
    if not todo_list:
        print("Your to-do list is empty!")
    else:
        print("Your To-Do List:")
        for task_id, task in todo_list.items():
            print(f"{task_id}. {task}")

# Function to add a task
def add_task(task):
    task_id = len(todo_list) + 1
    todo_list[task_id] = task
    print(f"Added task: {task}")

# Function to remove a task
def remove_task(task_id):
    if task_id in todo_list:
        removed = todo_list.pop(task_id)
        print(f"Removed task: {removed}")
    else:
        print("Task ID not found.")

# Sample usage
add_task("Learn Python")
add_task("Push code to GitHub")
show_tasks()
remove_task(1)
show_tasks()
