from random import randint

heads = 0
tails = 0


for count in range(0,5001):
  flip = randint(1,2)

  if flip < 2:
      heads += 1
      print "Attempt #" + str(count) + ": Throwing a coin... It's a head! Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"
  elif flip > 1:
        tails += 1
        print "Attempt #" + str(count) + ": Throwing a coin... It's a tail! Got " + str(heads) + " head(s) so far and " + str(tails) + " tail(s) so far"

print "Ending the program, thank you!"



