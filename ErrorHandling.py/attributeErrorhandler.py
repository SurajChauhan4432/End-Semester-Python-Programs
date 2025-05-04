# Make attribute errors handler with built in exceptions.
text = "Hello, world!"

try:
    result = text.false_method()
    print(result)
except AttributeError:
    print("AttributeError: The object does not have the attribute or method you tried to use.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
