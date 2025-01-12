# explore_datetime.py

from datetime import datetime, timedelta

def display_current_datetime():
    """Display the current date and time in a readable format."""
    current_date = datetime.now()
    print("Current Date and Time:", current_date.strftime("%Y-%m-%d %H:%M:%S"))

def calculate_future_date():
    """Calculate and display the date after a specified number of days."""
    try:
        days = int(input("Enter the number of days to add: "))
        current_date = datetime.now()
        future_date = current_date + timedelta(days=days)
        print(f"The date after {days} days will be: {future_date.strftime('%Y-%m-%d')}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
