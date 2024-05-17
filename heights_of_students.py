students_heights = input().split()

for n in range(0, len(students_heights)):
    students_heights[n] = int(students_heights[n])


total_height = 0
for height in students_heights:
    total_height += height

print(f"total height = {total_height}")