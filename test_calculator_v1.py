from commands_v1 import AdditionCommand, SubtractionCommand, MultiplicationCommand, DivisionCommand

def test_addition():
    add = AdditionCommand()
    assert add.execute(2, 3) == 5

def test_subtraction():
    subtract = SubtractionCommand()
    assert subtract.execute(5, 3) == 2

def test_multiplication():
    multiply = MultiplicationCommand()
    assert multiply.execute(2, 3) == 6

def test_division():
    divide = DivisionCommand()
    assert divide.execute(6, 3) == 2
    try:
        divide.execute(1, 0)
    except ValueError as e:
        assert str(e) == "Division by zero is not allowed"
