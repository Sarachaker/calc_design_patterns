class StudentCommand:
    def execute(self):
        raise NotImplementedError

class MultiplyCommand(StudentCommand):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x * self.y

class DivideCommand(StudentCommand):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def execute(self):
        return self.x / self.y

def student_repl():
    while True:
        try:
            command = input("Enter student command (multiply/divide): ").strip().lower()
            if command == "exit":
                break
            x = float(input("Enter first number: "))
            y = float(input("Enter second number: "))

            if command == "multiply":
                cmd = MultiplyCommand(x, y)
            elif command == "divide":
                cmd = DivideCommand(x, y)
            else:
                print("Invalid student command")
                continue

            result = cmd.execute()
            print(f"Student Result: {result}")

        except ValueError:
            print("Invalid input. Please enter numbers.")

if __name__ == "__main__":
    student_repl()
