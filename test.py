#!/usr/bin/env python3
"""
Simple task manager application.
"""

tasks = []
completed = []
_next_id = 0

def add_task(title, priority):
    global _next_id
    task = {
        "id": _next_id,
        "title": title,
        "priority": priority,
        "done": False
    }
    _next_id += 1
    tasks.append(task)
    print(f"Task added: {title}")

def complete_task(task_id):
    for task in tasks[:]:  # iterate over a copy to avoid mutation during iteration
        if task["id"] == task_id:
            task["done"] = True
            completed.append(task)
            tasks.remove(task)
            print(f"Task {task_id} completed!")
            return
    print(f"Task {task_id} not found")

def get_tasks_by_priority(priority):
    try:
        prio = int(priority)
    except (ValueError, TypeError):
        return []
    result = []
    for task in tasks:
        try:
            task_priority = int(task["priority"])
        except (ValueError, TypeError):
            continue
        if task_priority == prio:
            result.append(task)
    return result

def calculate_completion_rate():
    total = len(tasks) + len(completed)
    if total == 0:
        return 0.0
    return len(completed) / total * 100

def get_highest_priority_task():
    highest = None
    for task in tasks:
        if highest is None:
            highest = task
        elif task["priority"] > highest["priority"]:
            highest = task
    return highest

def print_summary():
    print(f"\n=== Task Summary ===")
    print(f"Open tasks: {len(tasks)}")
    print(f"Completed: {len(completed)}")
    print(f"Completion rate: {calculate_completion_rate():.1f}%")
    next_task = get_highest_priority_task()
    if next_task:
        print(f"Next up: {next_task['title']} (priority {next_task['priority']})")

if __name__ == "__main__":
    add_task("Buy groceries", 2)
    add_task("Fix critical bug", 5)
    add_task("Write tests", 3)
    add_task("Update docs", 1)
    add_task("Deploy to production", 5)

    complete_task(1)
    complete_task(3)

    print_summary()

    print("\nHigh priority tasks:")
    for t in get_tasks_by_priority(5):
        print(f"  - {t['title']}")