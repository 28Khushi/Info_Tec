#DICE ROLLER
import random

def roll_dice(num_dice):
    results = [random.randint(1, 6) for _ in range(num_dice)]
    return results

def main():
    print("Welcome to the Dice Rolling App!")
    while True:
        try:
            num_dice = int(input("How many dice would you like to roll? "))
            if num_dice <= 0:
                print("Please enter a positive number of dice.")
                continue
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue

        dice_results = roll_dice(num_dice)
        print(f"Result(s) of rolling {num_dice} dice:")
        for i, result in enumerate(dice_results, start=1):
            print(f"Die {i}: {result}")

        choice = input("Roll again? (yes/no): ").strip().lower()
        if choice != 'yes':
            print("Thank you for using the Dice Rolling App. Goodbye!")
            break

if __name__ == "__main__":
    main()
