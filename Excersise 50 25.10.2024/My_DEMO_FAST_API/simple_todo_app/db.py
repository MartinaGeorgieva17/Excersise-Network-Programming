tasks = [
    {"id": 1, "title": "Buy groceries", "completed": False},
    {"id": 2, "title": "Read Fast API Tutoria", "completed": False}
]

def get_tasks():
    return tasks

def add_task(task):
    task["id"] = len(tasks) + 1
    tasks.append(task)
    return task

def delete_task(task_id):
    global tasks
    tasks = [task for task in tasks if task["id"] !=task_id]
    return len(tasks) < len(tasks)