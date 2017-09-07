pencilNum = int(input("The number of pencil? "))
penNum = int(input("The number of pen? "))

pencilP = 1000
penP = 2000
totalP = pencilNum*pencilP + penNum*penP

if (totalP>=10000):
    totalP = int(totalP*0.9)

print("Total price is", totalP, "won")

