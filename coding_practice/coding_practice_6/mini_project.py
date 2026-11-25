tasks = []

while True:
    print("\nMenu: add | view | remove | done | quit\n")
    
    prompt = input("Input a choice: ") # Not validating input
    
    if prompt == "view":

        if not tasks:
            print("Nothing to view")
            continue
        
        n = 1
        for task in tasks:
            print(f"{n} {task}")
            n += 1
    
    elif prompt == "add":
        value = input("\n> ")
        tasks.append(([], value))
        print("\nTask added successfully")
        
    
    elif prompt == "done":

        index = input("Input a number: ")
    
        if not index.isdigit():
            print("Invalid Input")
            continue

        if int(index) <= 0 or int(index) > len(tasks):
            print("Invalid input")
            continue

        tasks[int(index)-1][0].append("x")
    
    elif prompt == "remove":
        
        index = input("\nInput a number: ")
        
        if not index.isdigit():
            print("Invalid Input")
            continue

        if int(index) <= 0 or int(index) > len(tasks):
            print("Invalid input")
            continue
        
        tasks.pop(int(index)-1)
    
    elif prompt == "quit":
        break
    
    else:
        print("\nInvalid input")
    