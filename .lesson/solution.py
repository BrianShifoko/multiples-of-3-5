# Print numbers 1 to 100
for i in range(1,101):
  # For multiples of both 3 and 5, print "X is a multiple of 3 and 5"
  if i % 3 == 0 and i % 5 == 0:
    print(i, "is a multiple of 3 and 5")
  # For multiples of 3, print "X is a multiple of 3"
  if i % 3 == 0:
    print(i, "is a multiple of 3 and 5")
  # For multiples of 5, print "X is a multiple of 5"
  elif i % 5 == 0:
    print(i, "is a multiple of 5")
  else:
    print(i)