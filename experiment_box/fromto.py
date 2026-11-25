#  Write a function that takes two integers and returns a string showing the range of numbers from the first to the second. 
def from_to(integer_1: int, integer_2: int) -> str|int:
    
    if (integer_1 > 99 or integer_1 < 0) or  (integer_2 > 99 or integer_2 < 0):
        return "Invalid\n"

    if integer_1 == integer_2:
        return integer_1
    
    container = ""

    if integer_2 > integer_1:
        for num in range(integer_1, (integer_2+1)):
            if len(container) != 0 and num != (integer_2+1):
                container += ", "
            if num >= 9 and num <= 1:
                container += f"0{num}"
                continue
            container += f"{num}"
    
    if integer_1 > integer_2:
        n = integer_1
        while n >= integer_2:
            if len(container) != 0 and n != integer_1+1:
                container += " "
            if n >= 9 and n <=1:
                container += f"0{n}"
                continue
            container += str(n)
            n -= 1
        
    return container


print(from_to(100, 99))
