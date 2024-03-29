import random


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
            (user_choice == 'scissors' and computer_choice == 'paper') or \
            (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "Computer wins!"


def main():
    choices = ['rock', 'paper', 'scissors']
    total_rounds = 3

    while True:
        user_score = 0
        computer_score = 0

        print("\nRock, Paper, Scissors Game\n")

        for _ in range(total_rounds):
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

            while user_choice not in choices:
                print("Invalid choice. Please enter rock, paper, or scissors.")
                user_choice = input("Enter your choice: ").lower()

            computer_choice = random.choice(choices)
            print(f"\nYour choice: {user_choice.capitalize()}")
            print(f"Computer's choice: {computer_choice.capitalize()}")

            result = determine_winner(user_choice, computer_choice)
            print(result)

            if result == 'You win!':
                user_score += 1
            elif result == 'Computer wins!':
                computer_score += 1

            print(f"\nYour score: {user_score}")
            print(f"Computer's score: {computer_score}")

        play_again = input("\nDo you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
