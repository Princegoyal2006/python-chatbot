import datetime
import random

# ---------------- WELCOME MESSAGE ----------------
def welcome_msg():
    print("Hello! I am a Rule-Based Chatbot.")
    print("You can chat with me, check time/date, play a game or use calculator.")
    print("Type 'bye' to exit.\n")


# ---------------- NUMBER GUESSING GAME ----------------
def number_game():
    print("\nGame Started!")
    print("I have selected a number between 1 and 50.")
    print("Type 'exit' to stop the game.")

    number = random.randint(1, 50)

    while True:
        user_input = input("Your Guess: ").lower()

        if user_input == "exit":
            print("Game Ended.\n")
            break

        if user_input.isdigit():
            guess = int(user_input)
            if guess > number:
                print("Too High!")
            elif guess < number:
                print("Too Low!")
            else:
                print("🎉 Congratulations! You guessed it right.\n")
                break
        else:
            print("Invalid input. Enter a number.")


# ---------------- CALCULATOR ----------------
def calculator():
    print("\nCalculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit Calculator")

    while True:
        choice = input("Enter choice: ")

        if choice == "5":
            print("Calculator Closed.\n")
            break

        if choice not in ["1", "2", "3", "4"]:
            print("Invalid choice.")
            continue

        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == "1":
            print("Result:", num1 + num2)
        elif choice == "2":
            print("Result:", num1 - num2)
        elif choice == "3":
            print("Result:", num1 * num2)
        elif choice == "4":
            if num2 != 0:
                print("Result:", num1 / num2)
            else:
                print("Division by zero not allowed.")


# ---------------- CHATBOT RULES ----------------
def chatbot_response(user_input):
    user_input = user_input.lower()

    if "hi" in user_input or "hello" in user_input:
        return "Hello! How can I help you?"

    elif "who are you" in user_input:
        return "I am a rule-based chatbot made using Python."

    elif "time" in user_input:
        return "Current time is " + datetime.datetime.now().strftime("%H:%M:%S")

    elif "date" in user_input:
        return "Today's date is " + datetime.datetime.now().strftime("%d-%m-%Y")

    elif "calculator" in user_input:
        calculator()
        return "Calculator session finished."

    elif "game" in user_input:
        number_game()
        return "Game session finished."

    elif "bye" in user_input or "exit" in user_input:
        return "exit"

    else:
        return "Sorry, I didn't understand that."


# ---------------- MAIN PROGRAM ----------------
def chatbot():
    welcome_msg()
    while True:
        user_input = input("You: ")
        response = chatbot_response(user_input)

        if response == "exit":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Chatbot:", response)


# Run chatbot
chatbot()