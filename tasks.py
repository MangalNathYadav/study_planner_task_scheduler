# tasks.py

from data import tasks, PRIORITIES, STATUSES, TASK_TYPES
from utils import get_non_empty_input, get_date, get_time, get_integer


def add_task():

    print("\n===== ADD TASK =====")

    name = get_non_empty_input("Task name: ")

    print("\nTask Type:")
    print("1. Study")
    print("2. Personal")

    while True:
        choice = input("Choose type: ")

        if choice == "1":
            task_type = "Study"
            break

        elif choice == "2":
            task_type = "Personal"
            break

        else:
            print("Invalid choice. Try again.")

    date = get_date()
    time = get_time()

    print("\nPriority:")
    print("1. High")
    print("2. Medium")
    print("3. Low")

    while True:
        choice = input("Choose priority: ")

        if choice == "1":
            priority = "High"
            break

        elif choice == "2":
            priority = "Medium"
            break

        elif choice == "3":
            priority = "Low"
            break

        else:
            print("Invalid choice.")

    task_id = len(tasks) + 1

    task = {
        "id": task_id,
        "name": name,
        "type": task_type,
        "date": date,
        "time": time,
        "priority": priority,
        "status": "Pending"
    }

    tasks.append(task)

    print("\nTask added successfully!")


def view_all_tasks():

    print("\n===== ALL TASKS =====")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    for task in tasks:

        print("-" * 40)

        print("ID       :", task["id"])
        print("Name     :", task["name"])
        print("Type     :", task["type"])
        print("Date     :", task["date"])
        print("Time     :", task["time"])
        print("Priority :", task["priority"])
        print("Status   :", task["status"])

    print("-" * 40)


def view_today():

    print("\n===== TODAY'S SCHEDULE =====")

    today = input("Enter today's date (YYYY-MM-DD): ")

    found = False

    for task in tasks:

        if task["date"] == today:

            found = True

            print("-" * 40)
            print(
                task["time"],
                "|",
                task["name"],
                "|",
                task["priority"],
                "|",
                task["status"]
            )

    if found == False:
        print("No tasks scheduled for this date.")


def mark_completed():

    print("\n===== MARK TASK COMPLETED =====")

    if len(tasks) == 0:
        print("No tasks available.")
        return

    task_id = get_integer("Enter task ID: ")

    for task in tasks:

        if task["id"] == task_id:

            task["status"] = "Completed"

            print("Task marked as completed.")
            return

    print("Task not found.")


def edit_task():

    print("\n===== EDIT TASK =====")

    task_id = get_integer("Enter task ID: ")

    for task in tasks:

        if task["id"] == task_id:

            print("\nCurrent task:", task["name"])

            new_name = input("New name (press Enter to keep old): ")

            if new_name != "":
                task["name"] = new_name

            new_priority = input(
                "New priority (High/Medium/Low, Enter to skip): "
            )

            if new_priority in PRIORITIES:
                task["priority"] = new_priority

            print("Task updated.")
            return

    print("Task not found.")


def delete_task():

    print("\n===== DELETE TASK =====")

    task_id = get_integer("Enter task ID: ")
    
    for task in tasks:

        if task["id"] == task_id:

            tasks.remove(task)

            print("Task deleted.")
            return

    print("Task not found.")