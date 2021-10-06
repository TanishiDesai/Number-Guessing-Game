import random 
number = random.randint(1,9)
chances = 0
print("Number Guessing Game")
print("Guess a number between 1 and 9")
while chances < 5 :
    guess = int(input("Enter you Guess : "))
    if (guess == number) :
        print("Congratulations YOU WON!!!")
        break 
    elif (guess < number) :
        print("Your guess was too low. Guess a number higher than " , guess)
    else  :
        print("Your guess was too high. Guess a number lower than " , guess)
    chances += 1

if not chances < 5 : 
    print("Sorry.. You lose.. The number was ", number)