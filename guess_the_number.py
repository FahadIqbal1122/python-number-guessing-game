import random
import time

def play_game():
    secret_number = random.randint(1, 100)
    attempts = 0
    
    print("Hey! I'm thinking of a number between 1 and 100!")
    print("Can you guess what it is?")
    
    while True:
        try:
            guess = int(input("Your guess: "))
            attempts += 1
            
            if guess < secret_number:
                print("Nope, too low! Aim higher!")
            elif guess > secret_number:
                print("Too high! Try lower!")
            else:
                print(f"\nWOOHOO! You got it in {attempts} tries!")
                print("You're awesome!")
                break
                
        except ValueError:
            print("Oops! That's not a number! Try again!")

if __name__ == "__main__":
    while True:
        play_game()
        play_again = input("\nWanna play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("\nThanks for playing! Catch ya later!")
            break
