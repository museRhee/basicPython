'''
enter m, and find n.
enter 0, program exit.

n satisfies the following condition.
1.sum of integers from 1 to n is same or less than m
2.n is the biggest one which satisfied the condition 1.
'''

while (True) :
    m = int(input("Enter the number m: "))  
    
    if (m == 0) :                        #program exit if enter 0
        print('Good-bye')
        break
 
    n =0                                 #initial value of count number
    totalSum = 0                         #initial sum of totalSum
   
   #find n by totalSum
    while (True) :
        totalSum += n
        
        if (totalSum > m) :
            print('the number is', n-1)  #n is over m. so n-1
            break
        else :
            n += 1
