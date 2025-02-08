
student_heights = [180, 124 ,165,173, 189, 169, 146]


x = 0
y = 0
for line in range(len(student_heights)):  
  
  x = x + student_heights[line]  
  y += 1

print(f"total height = {x}")
print(f"number of students = {y}")
print(f"average height = {round(x/y)}")