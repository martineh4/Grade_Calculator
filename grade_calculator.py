student_grades={"Carly": [78, 66, 90], "Tom": [92, 96, 88], "Lisa": [88, 94, 79], "Josh": [56, 54, 40]}

# Calculates student average
student_averages={}
for student, grades in student_grades.items():
    average=sum(grades)/len(grades)
    student_averages[student]=average

# Determines letter grades based on student averages
student_letter_grades={}
for student, average in student_averages.items():
    if average>=90:
        letter="A"
    elif average>=80:
        letter="B"
    elif average>=70:
        letter="C"
    elif average>=60:
        letter="D"
    else:
        letter="F"
    student_letter_grades[student]=letter

# Determines top performer and highest average
top_performer=None
highest_average=0
for student, average in student_averages.items():
    if average>highest_average:
        top_performer=student
        highest_average=average

# Calculates class average
class_average=sum(student_averages.values())/len(student_averages)

# Determines number of students that are passing
students_passing=0
for letter in student_letter_grades.values():
    if letter in ["A", "B", "C"]:
        students_passing+=1

# Output
print(f"Student Averages: {student_averages}")
print(f"Student Letter Grades: {student_letter_grades}")
print(f"Top Performing Student: {top_performer} with {highest_average} as their average")
print(f"Class Average: {class_average}")
print(f"Number of Students Passing: {students_passing}")