#input time by second
time = int(input("Enter the second : "))

#h:hours, m:minute, s:second
h = time // 3600
m = time % 3600 // 60
s = time % 3600 % 60

#print result
print(str(h) + "h " + str(m) + "m " + str(s) + "s")

'''
#if not type conversion, using "sep"
print(h, "h ", m, "m ", s, "s", sep="")
'''
