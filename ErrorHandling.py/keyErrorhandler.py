# Make a key error handler with built in exceptions. 
data = {
    "name": "Ben",
    "age": 30,
    "city": "New York"
}

key = "country"

try:
    value = data[key]
    print(f"Value for '{key}': {value}")
except KeyError:
    print(f"KeyError: The key '{key}' does not exist in the dictionary.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
