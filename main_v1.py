from commands_v1 import AdditionCommand, SubtractionCommand, MultiplicationCommand, DivisionCommand, HelpCommand

# Command dictionary
operations = {
    "add": AdditionCommand(),
    "subtract": SubtractionCommand(),
    "multiply": MultiplicationCommand(),
    "divide": DivisionCommand(),
    "help": HelpCommand(),
}

def calculator():
    print("Welcome to Basic Calculator. Type 'help' for available commands.")
    while True:
        user_input = input("Enter command: ").strip().split()
        if user_input[0] == "quit":
            break
        try:
            command = operations[user_input[0]]
            if user_input[0] == "help":
                command.execute()
            else:
                result = command.execute(float(user_input[1]), float(user_input[2]))
                print(f"Result: {result}")
        except (KeyError, ValueError) as e:
            print(f"Error: {e}. Type 'help' for assistance.")

if __name__ == "__main__":
    calculator()
