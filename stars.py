
# PART 1
# x = [4, 6, 1, 3, 5, 7, 25]

# def draw_stars():
#   for count in x:
#     print "*" * count
# draw_stars()


# PART 2
x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars1(arr):
  for val in arr:
    if type(val) == str:
      print val[0].lower() * len(val)
    elif type(val) == int:
      print "*" * val
draw_stars1(x)
