try:
    import magic
except ModuleNotFoundError:
    print("ModuleNotFoundError: The module you are trying to import does not exist.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
