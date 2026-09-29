# main.py

from tasks import (
    add_task,
    view_all_tasks,
    view_today,
    mark_completed,
    edit_task,
    delete_task
)

from utils import pause

def show_menu():

    print("\n")
    print("=" * 45)
    print("       STUDY PLANNER & TASK SCHEDULER")
    print("=" * 45)
    print("1. Add Study/Personal Task")
    print("2. View All Tasks")
    print("3. View Today's Schedule")
    print("4. Mark Task as Completed")
    print("5. Edit Task")
    print("6. Delete Task")
    print("7. Exit")

    print("=" * 45)


def main():

    while True:

        show_menu()

        choice = input("Enter your choice: ")

        if choice == "1":

            add_task()
            pause()

        elif choice == "2":

            view_all_tasks()
            pause()

        elif choice == "3":

            view_today()
            pause()

        elif choice == "4":

            mark_completed()
            pause()

        elif choice == "5":

            edit_task()
            pause()

        elif choice == "6":

            delete_task()
            pause()

        elif choice == "7":

            print("\nThank you for using Study Planner!")
            break

        else:

            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()