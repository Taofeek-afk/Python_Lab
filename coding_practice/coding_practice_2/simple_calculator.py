def calc():
    num_1 = input("Enter a number: ")
    operator = input("Provide an operator: ")
    num_2 = input("Enter a number: ")
    
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "*": lambda a, b: a * b,
        "/": lambda a, b: a / b
    }
    
    try:
        if operator not in operators:
            return "Invalid operator: try using (+, -, *, /)"
        
        if operator == "/" and num_2 == str(0):
            return "Invalid operator, cannot divide by zero"
        
        result = operators[operator](int(num_1), int(num_2))
    
    except ValueError:
        return "only integer inputs are allowed!"
    
    return result


print(calc())
