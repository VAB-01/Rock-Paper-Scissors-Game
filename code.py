import random as r
def rps():
    while True:
        print("Welcome to the rock-paper-scissors game!")
        print("Type 'rock', 'paper', or 'scissors'. To quit, type 'quit'.")
        player_input = input("Enter your choice: ").lower()

        if player_input == "quit":
            print("Thanks for playing!")
            break

        choices = ['rock', 'paper', 'scissors']
        computer_choice = r.choice(choices)

        if player_input not in choices:
            print("Invalid input. Please enter 'rock', 'paper', or 'scissors'.")
            continue

        print(f"Computer chose: {computer_choice}")

        if player_input == computer_choice:
            print("It's a draw!")
        elif (player_input == 'scissors' and computer_choice == 'paper') or \
             (player_input == 'rock' and computer_choice == 'scissors') or \
             (player_input == 'paper' and computer_choice == 'rock'):
            print("You win!")
        else:
            print("You lose!")

if __name__ == '__main__':
    rps()
