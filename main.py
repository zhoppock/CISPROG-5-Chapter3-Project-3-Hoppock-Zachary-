#import the random and math modules
import random
import math
#input the range of numbers to choose from, and also your number to guess
smaller = int(input("Enter the smaller number: "))
larger = int(input("Enter the larger number: "))
myNumber = int(input("\nEnter a number for the computer to guess: "))
#the logarithm will determine how many guesses the computer has to use
logNumber = larger - smaller + 1
count = 0
guesses = round(math.log(logNumber,2))
print("\nThe computer gets", guesses, "guesses.")
#the computer will begin to guess your number
while True:
  count += 1
  if count > guesses:
    print("\nThe computer has ran out of guesses.  Better luck next time.")
    break
  print("\nComputer, enter your guess: ", end = "")
  comNumber = random.randint(smaller, larger)
  print(comNumber)
  if comNumber < myNumber:
    print("Too small!")
  elif comNumber > myNumber:
    print("Too large!")
  else:
    print("\nCongratulations! The computer got it in", count, "tries!")
    break