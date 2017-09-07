time = int(input('Enter the second: '))

h = time // 3600
m = time % 3600 // 60
s = time % 3600 % 60

print(h, 'h ', m, 'm ', s, 's') 
