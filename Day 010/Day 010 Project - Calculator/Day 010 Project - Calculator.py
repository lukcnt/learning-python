import art
import os

print(art.logo)

#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

#Dictionary with calculator functions
operations = {
    "+": add,
    "-": subtract, 
    "*": multiply, 
    "/": divide
}

def calculator():
    #First number input from user
    num1 = float(input("What's the first number?: "))

    #Shows the available math operations
    for symbols in operations:
        print(symbols)

    #Flag to keep doing the loop
    keep_calculating = True

    while keep_calculating: 
        #User choose what math operation he/she wants
        operation_symbol = input("Pick an operation from the line above: ")

        #Second number input from user
        num2 = float(input("What's the second number?: "))

        #Returns the result of the operation
        answer = operations[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        #Variable with the chose option.
        choice = input(f"Type 'y' to continue calculating with {answer}, type 'n' to start a new calculation or type 'end' to finish the program: ")

        #Pass value of variable answer to the variable num1 and keep calculating
        if choice == "y":
            num1 = answer
        #Finish the program.
        elif choice == "end":
            exit()
        #End the loop and start a new calculating
        else:
            keep_calculating = False
            calculator()

calculator()