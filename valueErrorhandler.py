num = input("Enter a number: ")

try:
    number = int(num)
    print(f"You entered the number: {number}")
except ValueError:
    print(f"ValueError: '{num}' is not a valid integer.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
