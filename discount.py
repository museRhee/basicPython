'''
Input the number of fruits and print total price.
if the number of grapes over 3 or more, 10% discount.
'''

#input the number of fruits
appleNum = int(input("Number of aaple? "))
grapeNum = int(input("Number of grape? "))
pearNum = int(input("Number of pear? "))
orangeNum = int(input("Number of orange? "))

#price of fruits
appleP = 1000
grapeP = 3000
pearP = 2000
orangeP = 500

#total price
totalP = (appleNum*appleP + grapeNum*grapeP +
          pearNum*pearP + orangeNum*orangeP)

#get a discount when grapeNum>=3
if (grapeNum >= 3):
    totalP = totalP*0.9

#print total price
print("Total price is ", int(totalP), sep="")
                      
