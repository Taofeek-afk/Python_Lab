
def grading_system(students: list[list[str | int]]): # 8.0
    A, B, C, D, E = 70, 60, 50, 45, 40,
    
    for student in students:
        name, *scores = student
        
        average = avg(scores)

        if average >= A:
            grade = "A"
        elif average >= B:
            grade = "B"
        elif average >= C:
            grade = "C"
        elif average >= D:
            grade = "D"
        elif average >= E:
            grade = "E"
        else:
            grade = "F"
        
        print(f"{name}  - Average: {average} - Grade: {grade}")
        
        
def avg(scores: list):
    if not scores:
        return 0.0
    
    num = 0
    
    for i in scores:
        num += i
    
    return round(num/len(scores), 2)


# print(avg([80, 75, 90]))


students = [
    ["Samuel", 80, 75, 90],
    ["David", 55, 60, 50],
    ["Mary", 35, 40, 30],
    ["John", 65, 70, 68],
    ["Taofeek", 23, 98, 74],
]

grading_system(students)
