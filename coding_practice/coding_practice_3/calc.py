def simple_calc():
    
    operators = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: a / b,
        "*": lambda a, b: a * b
    }
    
    try:
        num_1 = float(input("Proivde a num: "))
        operator = input("Choose an operator / + - *:")
        num_2 = float(input("Provide a num: "))
        
        if operator not in operators:
            return "Invalid operator"
        
        if (num_2 == 0.0 or 0) and operator == "/":
            raise ZeroDivisionError
    except ValueError:
        return "Input should be in integers or floats"
    except ZeroDivisionError:
        return "Cannot divide by zero"
    
    result = operators[operator](num_1, num_2)
    print(result)
            
    while True:
        prompt = input("\ninput break to end the progam, continue to update an operation or undo to reverse an operation: ")
        
        if prompt == "break":
            print(f"Operation completed! \nFinal output: {result}")
            break
        elif prompt == "continue":
            
            try:
                operator = input("Choose an operator / + - *: ")
                num = float(input("Provide a num: "))
                if operator not in operators:
                    return "Invalid operator. Program is breaking..."
            except ValueError:
                return "Input should be in integers or floats"
            
            global last_result
            last_result = result
            result_2 = operators[operator](result, num)
            print(result_2)
        elif prompt == "undo":
            result_2 = last_result
            print(result_2)


simple_calc()
