#input length of each side
sideA = int(input("length of 1sd side "))
sideB = int(input("length of 2nd side "))
sideC = int(input("lenght of 3rd side "))

#find the biggest side
if (sideA>=sideB and sideA>=sideC) :
    sideBig = sideA
    sideSec = sideB
    sideThr = sideC
elif (sideB>=sideA and sideB>=sideC) :
    sideBig = sideB
    sideSec = sideA
    sideThr = sideC
else :
    sideBig = sideC
    sideSec = sideA
    sideThr = sideB

#check the kind of triangle
if (sideBig < sideSec+sideThr) :            #if triangle
    if (sideBig == sideSec == sideThr) :
        print("regular triangle")
    elif (sideBig == sideSec or sideBig == sideThr or sideSec == sideThr) :
        print("isosceles triangle")
    elif (sideBig^2 == sideSec^2 + sideThr^2) :
        print("right-angled triangle")
    else :
        print("normal triangle")
else :                                      #if not triangle
    print("not triangle")                   
    
