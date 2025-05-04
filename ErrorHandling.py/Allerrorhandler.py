# Make an error handler with the use of multiple except for all types of errors.
try:
    user_input = input("Enter a number: ")
    number = int(user_input)

    result = 100 / number
    sample_list = [1, 2, 3]
    print(sample_list[5])

    sample_dict = {"name": "Alice"}
    print(sample_dict["age"]) 

    with open("missing_file.txt", "r") as f:
        content = f.read()

    text = "hello"
    text.fake_method()

    import nonexistent_module

    print(undefined_variable)

except ValueError:
    print("ValueError: Please enter a valid integer.")

except ZeroDivisionError:
    print("ZeroDivisionError: Cannot divide by zero.")

except IndexError:
    print("IndexError: That list index does not exist.")

except KeyError:
    print("KeyError: That key was not found in the dictionary.")

except FileNotFoundError:
    print("FileNotFoundError: The file you tried to open does not exist.")

except AttributeError:
    print("AttributeError: That method or attribute does not exist for this object.")

except ModuleNotFoundError:
    print("ModuleNotFoundError: The module you tried to import does not exist.")

except NameError:
    print("NameError: You are trying to use a variable or function that hasn't been defined.")

except Exception as e:
    print(f"An unexpected error occurred: {e}")
