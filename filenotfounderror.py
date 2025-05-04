# Make file not found error handler with built in exceptions.
file_name = "non_existing_file.txt"

try:
    with open(file_name, "r") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print(f"FileNotFoundError: The file '{file_name}' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
