#input subject score
aScore = int(input("Score of A? "))
bScore = int(input("Score of B? "))
cScore = int(input("Score of C? "))

#average score
avg = (aScore + bScore + cScore) / 3


#print result
if (aScore>=60 and bScore>=60 and cScore>=60) and (avg>=70):
    print("The average is ", int(avg), " and passed", sep="")
else:
    print("The average is ", int(avg), " and failed", sep="")
    
