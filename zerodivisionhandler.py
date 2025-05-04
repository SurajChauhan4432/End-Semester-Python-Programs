# Make a zero division error handler with built in exceptions.
try:
    numerator = float(input("Enter the numerator: "))
    denominator = float(input("Enter the denominator: "))
    result = numerator / denominator
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
except ValueError:
    print("Error: Please enter valid numbers.")
else:
    print(f"Result: {result}")
finally:
    print("Division attempt completed.")
