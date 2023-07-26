import random

def guessing_game() :
  answer = random.randint(1, 100)

  while True :
    guess = int(input('Guess a number: '))
    if guess == answer :
      print(f"Good shit! You got it right. The answer is {guess}")
      break
    elif guess < answer :
      print(f"Your guess of {guess} is too low!")
    else :
      print(f"Your guess of {guess} is too high!")
  

guessing_game()