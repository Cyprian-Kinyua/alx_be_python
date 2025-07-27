from datetime import datetime, date, time, timedelta


def display_current_datetime():
    current_date = datetime.now()
    print(
        f"Current date and time: {current_date.strftime('%Y-%m-%d %H:%M:%S')}")
    return current_date


def calculate_future_date():
    number_of_days = int(
        input("Enter the umber of days to add to the current date: "))
    current_date = date.today()
    future_date = current_date + timedelta(days=number_of_days)
    print(f"Future date: {future_date.strftime('%Y-%m-%d')}")
    return future_date


if __name__ == "__main__":
    display_current_datetime()
    calculate_future_date()
