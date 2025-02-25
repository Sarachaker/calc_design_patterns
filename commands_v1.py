class AdditionCommand:
    def execute(self, num1, num2):
        return num1 + num2

class SubtractionCommand:
    def execute(self, num1, num2):
        return num1 - num2

class MultiplicationCommand:
    def execute(self, num1, num2):
        return num1 * num2

class DivisionCommand:
    def execute(self, num1, num2):
        if num2 == 0:
            raise ValueError("Division by zero is not allowed")
        return num1 / num2

class HelpCommand:
    def execute(self):
        print("Available commands: add, subtract, multiply, divide")
