student_scores = ["78","65","89","86","5","91","64","89"]

for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])

y = student_scores[0]
for value_scores in range(0,len(student_scores)):
  print(value_scores)  
  if y <= student_scores[value_scores]:
     y = student_scores[value_scores]
  else:
      y > student_scores[value_scores]
      y = y

print (f"The highest score in the class is: {y}")  


highest_score = 0
for score in student_scores:
  print(score)
  if score > highest_score:
    highest_score = score


print(f"The highest score in the class is: {highest_score}")