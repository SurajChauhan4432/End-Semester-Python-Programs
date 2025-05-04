# Make index error handler with built in exceptions. 
my_list = [10, 20, 30, 40, 50]

index = 10

try:
    value = my_list[index]
    print(f"Value at index {index}: {value}")
except IndexError:
    print(f"IndexError: Index {index} is out of range for the list.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
