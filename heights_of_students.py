students_heights = input().split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])

number_of_students = 0
for student in students_heights:
    number_of_students += 1

print(f"Total of students = {number_of_students}")

total_height = 0
for height in students_heights:
    total_height += height

print(f"total height = {total_height}")

avarage_height = round(total_height / number_of_students)
print(f"avarage_height = {avarage_height}")