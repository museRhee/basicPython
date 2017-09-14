#input subject score
aScore = int(input("Score of A? "))
bScore = int(input("Score of B? "))
cScore = int(input("Score of C? "))

#average score
avg = (aScore + bScore + cScore) / 3

#round off score
avg = round(avg, 2)

#pass if each score over 60 and avg over 70
if aScore < 60 :
    print("failure_history score is " + str(aScore))
elif bScore < 60 :
    print("failure_general knowledge score is " + str(bScore))
elif cScore < 60 :
    print("failure_manners score is " + str(cScore))
elif avg < 70 :
    print("failure_average score is " + str(avg))
else :
    print("passed_average score is " + str(avg))
