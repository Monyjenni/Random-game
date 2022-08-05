import random as rand
number=rand.randint(1,100)
i=5
for number in range(5):
    usernumber=int(input("choose a number between 1 and 100.You have to"+ str(i)"guess left."))
    if number==usernumber:
        print("You win")
    else:
        print("You lost")