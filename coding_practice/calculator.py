def calculator():
    
    print("This is a simple calculator program, you are to perform an operation on two numbers, the operators allowed include '+, -, * and /' only. Your inputs should be numeric only\n")
    
    num_1 = input("Provide the first digit: ")
    operator = input("Provide one of the accepted operators: ")
    num_2 = input("Provide the second digit: ")
    
    try:
        num_1, num_2 = int(num_1), int(num_2)
    except ValueError as err:
        return err
        
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        if num_2 == 0:
            return "Cannot divide by zero"
        return num_1 / num_2
    
    return "Invalid operator"


# print(calculator())

def smart_calculator():
    
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b,
    }
    
    try:
        num_1 = float(input("Provide the first digit: "))
        operator = input("Provide an operator: ")
        num_2 = float(input("Provide the second digit: "))
        
        if operator not in operations:
            return "Invalid operator"
        
        if operator == "/" and num_2 == 0:
            return "Cannot divide by zero"
        
        return operations[operator](num_1, num_2)

    except ValueError:
        return "Please provide valid numbers"


print(smart_calculator())


# For this exercise, a 10/10 solution isn't about making it unnecessarily complicated.
# It's about making the code correct, clean, extensible, and robust.
