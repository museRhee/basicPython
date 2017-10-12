'''
Enter height of Pyramid and make it by "#".
'''

#Input height of pyramid.
height = int(input("height of pyramid? "))

for h in range(height):
    space = height - h - 1              #N of space.
    block = h*2 + 1                     #N of block.
    print(' ' * space + '#' * block)
