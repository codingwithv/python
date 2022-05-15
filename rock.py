import random

l = ["rock", "paper", "scissor"]
'''
rock vs paper > paper wins
rock vs scissor > rocks wins
paper vs scissor > scissor wins

'''
while True:
    ccount = 0
    ucount = 0
    uc = int(input('''
Game Start......
1 Yes
2 No
    '''))
    if uc == 1:
        for a in range(1, 11):
            userinput = int(input('''
1 Rock
2 Paper
3 Scissor
            '''))
            if userinput == 1:
                uchoice = "rock"
            elif userinput == 2:
                uchoice = "paper"
            elif userinput == 3:
                uchoice = "scissor"
            Comchoise = random.choice(l)
            if Comchoise == uchoice:
                print("Computer value: ", Comchoise)
                print("User value: ", uchoice)
                print("Game Draw")
                # ucount = ucount + 1
                # ccount = ccount + 1
            elif (uchoice == "rock" and Comchoise == "scissor") or (uchoice == "paper" and Comchoise == "rock") or (
                    uchoice == "scissor" and Comchoise == "paper"):
                print("Computer value: ", Comchoise)
                print("User value: ", uchoice)
                print("You Win...")
                ucount = ucount + 1
            else:
                print("Computer value: ", Comchoise)
                print("User value: ", uchoice)
                print("Computer win...")
                ccount = ccount + 1

        if ucount == ccount:
            print("Final Game Draw...")
            print("User Score: ", ucount)
            print("Computer score: ", ccount)
        elif ucount > ccount:
            print("Final You Win The Game...")
            print("User Score: ", ucount)
            print("Computer score: ", ccount)
        else:
            print("Final Computer Win The Game...")
            print("User Score: ", ucount)
            print("Computer score: ", ccount)


    else:
        break
