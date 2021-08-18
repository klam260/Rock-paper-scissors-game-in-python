import sys
import random

def computerChoice():
    #options for rock paper scissor
    choice = ['rock', 'paper', 'scissor']

    #randint will choose a number from 0-2, which will be the choice for rock paper or scissors
    computerchoice = choice[random.randint(0,2)]

    return computerchoice

#tests whether the value is a number or not. absolute value function used to remove negative number input by user.
#if not a number, return 
def checkValue(inputVal):
    if(abs(inputVal.strip().isdigit())):
        print("You inputted a number please input rock, paper or scissor")
        return False
    else:
        if(inputVal.strip().lower() == 'rock'):
            return True
        
        elif(inputVal.strip().lower() == 'scissor'):
            return True

        elif(inputVal.strip().lower() == 'paper'):
            return True
        else:
            print("Incorrect value entered try again")
            return False



#exits the system once results have been shown
def results(compchoice, playerchoice):
    print("Test")
    if compchoice == playerchoice :
        print("Tie")

    elif compchoice == "scissor" and playerchoice == "paper":
        print("Computer choice: " + compchoice + " Player Choice: " + playerchoice)
        print("Computer Wins!")

    elif compchoice == "scissor" and playerchoice == "rock":
        print("Computer choice: " + compchoice + " Player Choice: " + playerchoice)
        print("Player Wins!")

    elif compchoice == "paper" and playerchoice == "rock":
        print("Computer choice: " + compchoice + " Player Choice: " + playerchoice)
        print("Player Wins!")

    elif compchoice == "paper" and playerchoice == "scissor":
        print("Computer choice: " + compchoice + " Player Choice: " + playerchoice)
        print("Computer Wins!")

    elif compchoice == "rock" and playerchoice == "paper":
        print("Computer choice: " + compchoice + " Player Choice: " + playerchoice)
        print("Player Wins!")
    
    elif compchoice == "rock" and playerchoice == "scissors":
        print("Computer choice: " + compchoice + " Player Choice: " + playerchoice)
        print("Computer Wins!")
    else:
        print("Error rock, paper or scissor not accepted")


def matchStart():
    val = False
    playerchoice = ""
    
    while(val == False):
        print('Please enter your choice of rock, paper, or scissor: ')
        playerchoice = input()
        val = checkValue(playerchoice)

    #generates computer choice
    compchoice = computerChoice()
    results(compchoice, playerchoice)
 
    


#Testing code

matchStart() 

        
        





        


