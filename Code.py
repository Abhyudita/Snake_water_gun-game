import random
computer=random.choice(["snake","water","gun"])
print("Do you wanna play?")
answer=input()
while(answer=="yes"):
    you=input("Enter your choice: ")
    print("You chose: "+you+" and the computer chose: "+computer)
    if(computer==you):
        print("Its a draw")
        print("-------------------------------------------------------------------")
    else:
        if(computer=="snake" and you=="gun"):
            print("You won")
        elif(computer=="snake" and you=="water"):
            print("You lost")
        elif(computer=="water" and you=="snake"):
            print("You win")
        elif(computer=="water" and you=="gun"):
            print("You lost")
        elif(computer=="gun" and you=="snake"):
            print("You lost")
        elif(computer=="gun" and you=="water"):
            print("You win")
        print("-------------------------------------------------------------------")
    print("Do you wanna play again?")
    answer=input()
    if(answer=="no"):
        break
