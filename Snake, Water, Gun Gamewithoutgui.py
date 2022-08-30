import random

def gamewin(comp, you):
    if comp == you:
        return None
    elif comp == "s":
        if you == "w":
            return False
        elif you == "g":
            return True
    elif comp == "w":
        if you == "g":
            return False
        elif you == "s":
            return True
    elif comp == "g":
        if you == "s":
            return False
        elif you == "w":
            return True

print("Comp Turn: Snake(S), Water(W) or Gun(G) ")
randno = random.randint(1, 3)
if randno == 1:
    comp = "s"
elif randno ==2:
    comp = 'w'
elif randno == 3:
    comp = 'g'
else:
    comp = None

you = input("Your Turn: Snaks(S), Water(W) or Gun(G) ")
a = gamewin(comp, you)
print(f"Computer Choose {comp}")
print(f"You Choose {you}")

if a == None:
    print("The Game Tei!")
elif a:
    print("You win!")
else:
    print("You Lose!")