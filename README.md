This is a simple command-line calculator implemented using the **Command Pattern** and **REPL** (Read, Evaluate, Print, Loop). It supports basic arithmetic operations: addition, subtraction, multiplication, and division.

## Features
- **Interactive REPL:** Continuously takes user input and executes commands.
- **Command Pattern:** Each operation is encapsulated in a separate command class.
- **Error Handling:** Handles invalid inputs and division by zero gracefully.
- **Help Command:** Displays available commands when the user types `help`.

## Commands
- `add <num1> <num2>`: Adds two numbers.
- `subtract <num1> <num2>`: Subtracts the second number from the first.
- `multiply <num1> <num2>`: Multiplies two numbers.
- `divide <num1> <num2>`: Divides the first number by the second.
- `help`: Displays available commands.
- `quit`: Exits the calculator.

## How to Run
1. Clone the repository:
   ```bash
   git clone https://github.com/Sarachaker/calc_design_patterns.git
   cd calc_design_patterns

# Student Log and Environment Setup

This project demonstrates the use of:
- GitHub Actions for CI/CD
- Environment Variables for secure configuration
- Logging for application monitoring

## Setup

1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
