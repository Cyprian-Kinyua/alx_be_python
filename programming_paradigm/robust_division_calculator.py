def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        numerator / denominator
        print(f"The result of the division is: {numerator / denominator:.1f}")
        return False

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")
        return False

    except ValueError:
        print("Error: Please enter numeric values only.")
        exit
