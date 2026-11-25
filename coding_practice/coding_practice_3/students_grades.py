def students_grade(arr: list):
    for student in arr:
        total = 0
        
        for score in student["scores"]:
            total += score
            
        average = round(total / len(arr), 2)
        
        if average > 70:
            Grade = "A"
        elif average > 60:
            Grade = "B"
        elif average > 50:
            Grade = "C"
        elif average > 45:
            Grade = "D"
        else:
            Grade = "E"
            
        print(f"{student["name"]} --> Average: {average} --> Grade: {Grade}")
        

students_grade([{"name": "Sam", "scores": [80, 90]}, {"name": "David", "scores": [55, 60]}])
