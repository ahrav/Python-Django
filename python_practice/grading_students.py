import math

def gradingStudents(grades):

    new_grades = []
    for x in grades:
        if x < 38:
            new_grades.append(x)
        elif x%10 >= 3 and x%10 < 5 or x%10 > 7:
            num = x%10
            if num > 7:
                new_num = 10 - num
                new_grades.append((new_num+x))
            else:
                new_num = 5 - num
                new_grades.append((x+new_num))
        else:
            new_grades.append(x)

    return new_grades

grades = [45,56,57,67,68,32,45,88,95]
print (gradingStudents(grades))

print (57%10)