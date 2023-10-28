print("Welcome")
print("You have three trials to guess a number")
import random
guess=(random.randrange(20,30))
test=True
guesses=1
while test and guesses<=3:
    num=int(input("Guess a number between 20 and 30:  "))
    if guess==num:
        print("Excellent, Your answer is",guess)
        test=False
    else:
        print("Wrong guess try again")
        guesses=guesses+1
#We print out to the player that the trials are over
if(guesses>3):
    print("You have exhausted your three trials. Your answer was",guess)
