appleNum = int(input("Number of aaple? "))
grapeNum = int(input("Number of grape? "))
pearNum = int(input("Number of pear? "))
orangeNum = int(input("Number of orange? "))

appleP = 1000
grapeP = 3000
pearP = 2000
orangeP = 500

totalP = appleNum*appleP + grapeNum*grapeP + pearNum*pearP + orangeNum*orangeP

if (grapeNum >= 3):
    totalP = int(totalP*0.9)

print("Total price is ", totalP, sep="")
                      
