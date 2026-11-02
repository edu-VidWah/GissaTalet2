namn = input("Vad heter du? ")
print(f"Hej {namn} och välkommen till spelet!")
import random as rand
tal = rand.randint(1, 10)
for i in range(3):
    while i < 3:
        gissning = int(input("Gissa ett tal mellan 1 och 10 "))
        if gissning == tal:
            print("Snyggt jobbat, helt rätt!")
            break
        elif gissning != tal:
            print("du fick fel")
        break
    if gissning == tal:
        break
    if i == 2:
        print("du får inga fler försök")
        break
        
        
        
