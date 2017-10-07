'''
input number and print whether even or odd.
'''

while True :
    inputNum = int(input("Enter the number: "))

    if (inputNum == 0) :
        print("Good-bye!")
        break

    if (inputNum % 2 == 0) :
        print("Even!")
    else :
        print("Odd!")
