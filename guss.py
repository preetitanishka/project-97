import random print("Number guessing game")
 # randint function to generate the random number between 1 to 9 number = random.randint(1, 9) 
 # number of chances to be given to the user to guess the number 
 # or it is the inputs given by user into input box here number of chances are 5 chances = 0 
        print("Guess a number (between 1 and 9):")
# While loop count the number of chances
while chances < 5:
    if guess == number:
        # if number entered by user is the same as the generated
        # number by radient function then break from loopusing loop
        # control statement "break"
        print("Congratulation YOU WON!!")
        break
    # Check whether the user guessed the correct answer
    if not chances < 5:
        print("YOU LOSE!! the Number is", number)
