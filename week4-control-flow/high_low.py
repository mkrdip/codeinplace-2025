
# importing Python's native random package
import random


NUM_ROUNDS = 5


def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")

    # Milestone 5
    score = 0
    game_round = 0
    
    # Milestone 4
    for i in range(NUM_ROUNDS):
        computer_number = random.randint(1, 100)
        your_number = random.randint(1, 100)

        # Milestone 1
        # print("The computer's number is ", computer_number)
        game_round = game_round + 1
        print("Round: ", game_round)
        print("Your number is ", your_number)
        
        # Milestone 2
        user_guess = input("Do you think your number is higher or lower than the computer's?: ")

        # Extension 1
        while user_guess != "higher" and user_guess != "lower":
            user_guess = input("Please only enter higher or lower: ")
        
        # Calculate if your number is higher or lower than the computer's
        # if your_number > computer_number and user_guess == higher:
        # Milestone 3
        if user_guess == "higher" and your_number > computer_number:
            print("You are right! The computer's number was ", computer_number)
            score = score + 1 
            print("Your score is now ", score)
        elif user_guess == "lower" and your_number < computer_number:
            print("You are right! The computer's number was  ", computer_number)
            score = score + 1 
            print("Your score is now ", score)
        else:
            print("Aww, that's incorrect. The computer's number was ", computer_number)
            score = score + 0
            print("Your score is now ", score)
        print("\n")
    # Extension 2   
    if score == NUM_ROUNDS:    
        print("Wow! You played perfectly!")
    elif score > int(NUM_ROUNDS/2):
        # print("DEBUG", int(NUM_ROUNDS/2))
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")
    
    print("\nThanks for playing!")

    
if __name__ == "__main__":
    main()
