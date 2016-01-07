# create a list of unassorted values
# have it from lowest to highest
# swap values in list until sorting is done
# compare adjacent values
# after a 1 swap is done, continue to swap again if needed


import random
import datetime

before = datetime.datetime.now()

arr = []
for x in range(100):
  arr.append(random.randint(0,10000))
count = len(arr) - 1
while count > 0:
  for i in range(0, len(arr) - 1):
    if arr[i] > arr[i+1]:
      temp = arr[i]
      arr[i] = arr[i + 1]
      arr[i+1] = temp
  count -= 1


after = datetime.datetime.now()

time = after - before
print time
print arr


