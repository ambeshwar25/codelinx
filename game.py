import random
print("Hi! Welcome to the Number Guessing Game.\nYou have 3 Chance to guess the number. Let's start!")
low = int(input("Enter the lower number: "))
high = int(input("Enter the high number: "))
print(f"\nYou haave 7 chance to guess the number between {low} and {high}. Let's start!")
num = random.randint(low, high)
ch = 3              #total allowed chance
gc = 0              #guess counter
while  gc < ch:
    gc += 1
    guess = int(input("Enter your guess: "))
    if guess == num:
        print(f"Correct! The number is {num}. You guessed it in {gc} attempts.")
        break
    elif guess > num:
        print("Too high! Try a lower number")
    elif guess < num:
        print("Too low! Try a higher number.")
    elif gc >= ch and guess != num:
        print(f"Sorry! The number was {num}. Better luck next time.")
