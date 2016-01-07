from random import randint

print "Scores and Grades"

for count in range(0,10):
  score = randint(60,100)

  if score >= 90:
    print "Score:" + str(score)+"You got a A"
  elif 80 <= score <=89:
    print "Score:" + str(score)+"You got a B"
  elif 70 <= score <=79:
    print "Score:" + str(score)+"You got a C"
  elif 60 <=score <=69:
    print "Score:" + str(score)+"You got a D"





print "End of the program. Bye!"
