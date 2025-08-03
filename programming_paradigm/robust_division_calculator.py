def safe_divide(numerator, denominator):
    try:
        numerator = float(numerator)
        denominator = float(denominator)
        numerator / denominator
        result = f"The result of the division is {numerator / denominator:.1f}"
        return result

    except ZeroDivisionError:
        result = "Error: Cannot divide by zero."
        return result

    except ValueError:
        result = "Error: Please enter numeric values only."
        return result
