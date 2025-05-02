try:
    print(undefined_variable)
except NameError:
    print("Error: You tried to use a variable that hasn't been defined.")
else:
    print("Variable printed successfully.")
finally:
    print("Name error handling completed.")
