aScore = int(input("Score of A? "))
bScore = int(input("Score of B? "))
cScore = int(input("Score of C? "))

avg = int((aScore + bScore + cScore) / 3)

if (aScore>=60 and bScore>=60 and cScore>=60) and (avg>=70):
    print("The average is ", avg, " and passed", sep="")
else:
    print("The average is ", avg, " and failed", sep="")
    
