# utils.py

from datetime import datetime


def get_non_empty_input(message):
    while True:
        value = input(message).strip()

        if value == "":
            print("Input cannot be empty.")
            continue

        return value


def get_integer(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_date():
    while True:
        date = input("Enter date (YYYY-MM-DD): ")

        try:
            datetime.strptime(date, "%Y-%m-%d")
            return date
        except ValueError:
            print("Invalid date format.")


def get_time():
    while True:
        time = input("Enter time (HH:MM): ")

        try:
            datetime.strptime(time, "%H:%M")
            return time
        except ValueError:
            print("Invalid time format.")


def pause():
    input("\nPress Enter to continue...")