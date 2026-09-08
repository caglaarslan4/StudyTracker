def get_integer(prompt):
    while True:
        try:
            value =int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")