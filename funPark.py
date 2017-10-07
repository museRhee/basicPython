''''
input child's height, weight and print if can ride or not.
if height over 155 and weight over 50, cannot ride.
'''

#input child's height and weight
height = int(input("child's height? "))
weight = int(input("child's weight? "))

#print result
if (height<=155 and weight<=50):
    print("Can ride")
else:
    print("Cannot ride") 
