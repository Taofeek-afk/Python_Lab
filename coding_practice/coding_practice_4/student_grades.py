students = [
    {"name": "Sam", "scores": [80, 90],},
    {"name": "David", "scores": [55, 60]},
    # {"name": "John", "scores": [23, 45]},
]


def grade_for(scores):
    total = 0
    for score in scores:
        total += score
                
    avg = round(total/len(students), 2)
                
    if avg > 70:
        grade = "A"
    elif avg > 60:
        grade = "B"
    elif avg > 50:
        grade = "C"
    elif avg > 45:
        grade = "D"
    elif avg > 40:
        grade = "E"
    else:
        grade = "F"
    
    return avg, grade


def students_grade(students: list[dict] = students):
    highest = 0
    top_student = ""
    
    lowest = 100
    least_student = ""
    
    for student in students:
        avg, grade = grade_for(student["scores"])

        if avg > highest:
            highest = avg
            top_student = student["name"]
            
        if lowest > avg:
            lowest = avg
            least_student = student["name"]
        
        print(f"{student["name"]} -> Average: {avg} -> Grade: {grade}")
    
    print(f"\n{top_student} got the highest score: {highest}")
    print(f"{least_student} got the least score: {lowest}")
                    
                
students_grade()

high_performing_students = [x["name"] for x in students if grade_for(x["scores"])[0] > 50] # Filter
mapped = [[x["name"], x["scores"], grade_for(x["scores"])[0]] for x in students]  # mapped
print(mapped)
print(high_performing_students)


# def students_grade(students: list[dict] = students):
#     highest = 0
#     top_student = ""
    
#     lowest = 100
#     least_student = ""
    
#     for student in students:
#         total = 0
#         for score in student["scores"]:
#             total += score
        
#         avg = round(total/len(students), 2)
        
#         if avg > 70:
#             grade = "A"
#         elif avg > 60:
#             grade = "B"
#         elif avg > 50:
#             grade = "C"
#         elif avg > 45:
#             grade = "D"
#         elif avg > 40:
#             grade = "E"
#         else:
#             grade = "F"
            
#         if avg > highest:
#             highest = avg
#             top_student = student["name"]
            
#         if lowest > avg:
#             lowest = avg
#             least_student = student["name"]
        
#         print(f"{student["name"]} -> Average: {avg} -> Grade: {grade}")
    
#     print(f"\n{top_student} got the highest score: {highest}")
#     print(f"{least_student} got the least score: {lowest}")