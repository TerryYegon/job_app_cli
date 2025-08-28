def exit_program():
    print("Goodbye!")
    exit()

def input_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid number.")
