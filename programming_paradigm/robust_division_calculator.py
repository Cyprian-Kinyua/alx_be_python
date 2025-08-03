def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        numerator / denominator
        return print(f"The result of the division is: {numerator / denominator:.1f}")

    except ZeroDivisionError:
        return print("Error: Cannot divide by zero.")

    except ValueError:
        return print("Error: Please enter numeric values only.")
