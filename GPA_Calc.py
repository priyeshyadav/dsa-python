print("Welcome to GPA Calculator")
print("Enter all your latter grades, One per line")
print("Enter a blank line to terminate")
#Dictionary got GPA Calc
points = {'A+':4.0, 'A' :4.0, 'A-' :3.67, 'B+' :3.33, 'B' :3.0, 'B-' :2.67,'C+' :2.33, 'C' :2.0, 'C' :1.67, 'D+' :1.33, 'D' :1.0, 'F' :0.0}
course_num = 0
total_points = 0
terminate = False

while not terminate:
    grade = input()
    if grade == '':
        terminate = True
    elif grade not in points:
        print(f' This grade {grade} is not listed, Ignored !')
    else:
        course_num += 1
        total_points += points[grade]
if course_num > 0:
    print("Your GPA is {0:.3}".format(total_points/course_num))
else:
    print("No Grade entered")