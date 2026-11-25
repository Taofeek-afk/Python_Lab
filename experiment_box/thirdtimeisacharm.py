def third_time_is_a_charm(string: str):
    if string == "":
        return "\n"
    
    count = 2
    container = ""
    
    while count < len(string):
        container += string[count]
        count += 3
        
    return container+"\n"  

# if i+1 % 3 == 0

print(third_time_is_a_charm("123456789"))
