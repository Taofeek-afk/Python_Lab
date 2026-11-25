def student_grade(arr):
    
    for data in arr:
        student, *grades = data
        
        total = 0
        for x in grades:
            total += x
       
        average = round(total / len(grades), 2)

        if average >= 70:
            grade = "A"
        elif average >= 60:
            grade = "B"
        elif average >= 50:
            grade = "C"
        elif average >= 45:
            grade = "D"
        elif average >= 40:
            grade = "E"
        else:
            grade = "F"
            
        print(f"{student} -> Average: {average} -> Grade: {grade}")
        
students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["Taofeek", 23, 98, 74],
]

student_grade(students)
