#Number Guessing Game
import random

def main():
    name=input("Enter your name:")
    print("Welcome",name,"To the Guessing Game")
    
    rule=input("Want to know about the rules Y/N:")
    if (rule=="Y"):
        print("1)Generate a random number between 1 and 100 \n")
        print("2) You will get 10 attempts to complete the game \n")    
        print("3)If you guessed correctly you will be the winner of the game")
    else:
        pass
    

    game_again= "yes"

    while game_again.lower() == "yes":
        random_number = random.randint(1, 100)
        attempts = 0

        print("\nI've selected a random number between 1 and 100. Try to guess it!")

        while attempts < 10:
            try:
                user_guess = int(input("\nEnter your guess: "))
            except ValueError:
                print("Invalid input! Please enter a valid number.")
                continue

            attempts += 1

            if user_guess == random_number:
                print(f"Congratulations! You guessed the number {random_number} in {attempts} attempts.")
                break
            elif user_guess < random_number:
                print("Too low! Try again.")
            else:
                print("Too high! Try again.")

        if attempts >= 10:
            print(f"\nGame over! The number was {random_number}.")

        game_again = input("Do you want to play again? (yes/no): ")

    print("Thank you for playing the Number Guessing Game!")

if __name__ == "__main__":
    main()

    











