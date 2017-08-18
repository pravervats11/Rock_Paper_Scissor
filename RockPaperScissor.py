import random
from random import randint
OptionList = ["Rock","Paper","Scissor"]
print "Let's Play || Rock Paper Scissor || with C.P.U \n"
print "\n"
print "Here are some RULES for those are new to this game: \n"
print "1. Rock Beats Scissor but looses against Paper \n"
print "2. Scissor Beats Paper but looses against Rock \n"
print "3. Paper Beats Rock but looses against Scissor Obviously :( \n"
while True:
    Player1 = str(raw_input('Input your Choice Player1:'))
    CPUvalue = random.randint(0,2)
    CPU = OptionList[CPUvalue]
    if Player1 == CPU:
        print("CPU also played " +CPU)
        print "||| It's a TIE |||"
    elif Player1 == "Rock":
        if CPU == "Scissor":
            print "||| You Won ||| CPU played Scissor"
        elif CPU == "Paper":
            print "||| You Loose ||| CPU played Paper"
    elif Player1 == "Paper":
        if CPU == "Scissor":
            print "||| You Loose ||| CPU played Scissor"
        elif CPU == "Rock":
            print "||| You Won ||| CPU played Rock"
    elif Player1 == "Scissor":
        if CPU == "Rock":
            print "||| You Loose ||| CPU played Rock"
        elif CPU == "Paper":
            print "||| You Win ||| CPU played Paper"
    else:
        print "Enter a valid move"
    Choice1 = raw_input('Do You want to Continue with the Game : (Yes/No) \n')
    Choice = str(Choice1)
    if Choice == "Yes":
        continue
    elif Choice == "No":
        break
    else:
        print "Enter a valid Choice"
