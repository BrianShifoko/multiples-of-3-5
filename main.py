# See Instructions tab

# Print numbers 1 to 100
data = 0
for i in range(1,101):
# For multiples of 3, print "X is a multiple of 3"  
  if i % 3 ==0 :
    print(i,  "is a multiple of 3")
# For multiples of 5, print "X is a multiple of 5"    
  elif i % 5 == 0:
      print(i, "is a multiple of 5")
  else :
    print(i, "")
print(data)