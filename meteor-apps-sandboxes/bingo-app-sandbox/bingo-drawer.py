import random

# Generate numbers 1 to 75
numbers = [i for i in range(1, 76)]

# Store drawn numbers
drawnNum = []

print numbers                   # ==> [1, 2, 3, ..., 75]
#  print numbers[0]                # ==> 1
print "Total numbers available:", len(numbers)
print "----------------------------------------"

for i in range(1, 76):
    tmp = random.choice(numbers)
    print "Numbers drawn:", tmp
    drawnNum.append(tmp)
    numbers.remove(tmp)
    print drawnNum
    #  print numbers
    print "Numbers remain:", len(numbers)
    print "--------------------"

print
print "----------------------------------------"
print "Total drawn numbers:", len(drawnNum)
print "Total numbers remain:", len(numbers)
