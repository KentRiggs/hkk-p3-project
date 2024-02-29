# lib/cli.py
def display_main_menu():
    print("\nWelcome to the Detective Game!")
    print("""
            ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⠤⠴⠒⠒⠒⠲⠤⢄⣀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣚⡉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠲⢄⡀⠀⠀⠀⠀
⣶⡀⠀⠀⢀⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⠖⠋⠉⠁⠀⠈⠉⠉⠉⠓⠒⠤⣄⠀⠀⠀⠀⠀⠀⠀⠙⢦⡀⠀⠀
⠘⢷⣶⡾⠿⠭⣙⠻⢶⣄⠀⠀⠀⠀⠀⠀⠀⢰⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢦⠀⠀⠀⠀⠀⠀⠀⠱⡄⠀
⠀⠀⠀⠀⠀⠀⠀⠙⣄⠙⡆⠀⠀⠀⠀⠀⠀⠈⣷⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡾⠀⠀⠀⠀⠀⠀⠀⠀⢹⡀
⠀⠀⠀⠀⠀⠀⠀⠀⠘⡆⢹⡀⠀⠀⠀⠀⢀⠞⠁⠈⠑⠢⠤⣀⣀⡀⠀⠀⠀⠀⣀⠴⠛⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣇
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⡀⢳⠀⠀⠀⢠⣯⢴⣶⣖⣺⣿⢲⣦⡬⣍⡉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠳⣈⢧⡀⠀⠸⣷⣾⣡⣿⣇⣼⣏⣨⡷⢛⣯⠿⣦⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠷⣯⣓⠂⣼⡿⢷⣾⣉⣀⣉⠉⠳⠟⣿⠴⡿⢻⠷⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⠃
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⣻⣷⣶⠤⣄⠀⠉⠙⣲⢄⠀⠀⠻⣿⣿⣿⡜⣷⠀⠀⠀⠀⠀⠀⠀⢠⣇⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣴⣿⣿⣿⠀⠀⠉⠲⣤⣼⣾⣷⡄⠀⠈⠁⢈⣇⣁⠀⠀⠀⠀⠀⠀⣰⠋⠈⣳
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣤⣾⡟⠻⣿⡿⣆⢀⣄⢀⣼⠿⣟⠛⠛⡄⠀⠀⣸⡏⣹⠀⠀⠀⠀⢀⡴⠁⠀⣰⠏
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠛⣦⡙⠒⠻⣄⡽⡏⣻⡟⢻⣿⢻⣤⠻⣿⣾⣿⣿⢁⣿⡆⠀⠀⣠⡞⠁⢀⣾⠋⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⠛⠿⠶⣾⣤⣿⣧⣟⣎⣉⣉⢙⣶⣿⣿⡿⠹⣾⣿⣿⡆⠀⢻⠀⢠⡿⠁⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠛⠛⠋⠉⠁⠀⠀⠀⠀⠛⠛⠃⢰⠋⠀⣾⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⢀⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠙⠲⢤⣀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡟⠁⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠉⢹⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠈⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣇⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡄⠀⠀⠀⠀⠀⠀⠀⢸⡄⠀⠘⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠤⣀⡀⠀⠀⠀⣀⡼⠁⠀⠀⢳⠀⠀⠀⠀⠀⠀⠀⠀⠀⡇⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠀⠀⠀⠀⠀⠈⢧⡀⠀⠀⠀⠀⠀⣠⠞⠁⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠉⠉⠀⠀⠀⠀
""")
    print("Please insert your name: ", end="")
    player_name = input()
    print(f"\nWelcome, {player_name}!")
    print("One of these suspects recently killed somebody.")
    print(""" 
          
 ➖➖🟥🟥🟥          ➖➖🟦🟦🟦           ➖➖🟩🟩🟩  
➖🟥🟥🟥🟥🟥        ➖🟦🟦🟦🟦🟦         ➖🟩🟩🟩🟩🟩
🟥🟥🟥🟦🟦🟦        🟦🟦🟦🟥🟥🟥         🟩🟩🟩🟨🟨🟨
🟥🟥🟥🟦🟦🟦        🟦🟦🟦🟥🟥🟥         🟩🟩🟩🟨🟨🟨
🟥🟥🟥🟥🟥🟥        🟦🟦🟦🟦🟦🟦         🟩🟩🟩🟩🟩🟩
🟥🟥🟥🟥🟥🟥        🟦🟦🟦🟦🟦🟦         🟩🟩🟩🟩🟩🟩
➖🟥🟥🟥🟥🟥        ➖🟦🟦🟦🟦🟦         ➖🟩🟩🟩🟩🟩
➖🟥🟥➖🟥🟥        ➖🟦🟦➖🟦🟦         ➖🟩🟩➖🟩🟩
➖🟥🟥➖🟥🟥        ➖🟦🟦➖🟦🟦         ➖🟩🟩➖🟩🟩
           """)
    start_investigation()

def start_investigation():
    while True:
        print("\nPress 1, 2, or 3 to choose which character to investigate.")
        print("Press 4 to accuse a character.")
        print("Press 5 to exit.")
        choice = input("Your choice: ")

        if choice in ["1", "2", "3"]:
            investigate_character(int(choice))
        elif choice == "4":
            make_accusation()
            break
        elif choice == "5":
            print("Thank you for playing. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")

def investigate_character(character_number):
    character_name = ["Hunter", "Kent", "Kairi"][character_number - 1]

    ascii_art = {
        
        1:"""
        ➖➖🟥🟥🟥
        ➖🟥🟥🟥🟥🟥
        🟥🟥🟥🟦🟦🟦
        🟥🟥🟥🟦🟦🟦
        🟥🟥🟥🟥🟥🟥
        🟥🟥🟥🟥🟥🟥
        ➖🟥🟥🟥🟥🟥
        ➖🟥🟥➖🟥🟥
        ➖🟥🟥➖🟥🟥 
        """,
        2:"""
        ➖➖🟦🟦🟦
        ➖🟦🟦🟦🟦🟦
        🟦🟦🟦🟥🟥🟥
        🟦🟦🟦🟥🟥🟥
        🟦🟦🟦🟦🟦🟦
        🟦🟦🟦🟦🟦🟦
        ➖🟦🟦🟦🟦🟦
        ➖🟦🟦➖🟦🟦
        ➖🟦🟦➖🟦🟦
        """,
        3:"""
        ➖➖🟩🟩🟩
        ➖🟩🟩🟩🟩🟩
        🟩🟩🟩🟨🟨🟨
        🟩🟩🟩🟨🟨🟨
        🟩🟩🟩🟩🟩🟩
        🟩🟩🟩🟩🟩🟩
        ➖🟩🟩🟩🟩🟩
        ➖🟩🟩➖🟩🟩
        ➖🟩🟩➖🟩🟩
        """
        }
    print(ascii_art[character_number])
    print(f"You are now speaking to {character_name}. Here are some questions you can ask them:")

    questions = [
        "What were you doing last night?",
        "Have you seen anything suspicious?",
        "Do you know who might have a motive?"
    ]
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")
    print("4. Return to main menu")

    while True:
        choice = input("Choose a question to ask: ")

        if choice in ["1", "2", "3"]:
            print(f"{character_name} says: [Placeholder response for question {choice}]")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def make_accusation():
    print("\nWho do you think the killer is?")
    print("1. Hunter")
    print("2. Kent")
    print("3. Kairi")
    choice = input("Your accusation: ")


    murderer = "22"  
    if choice == murderer:
        print("You're right! You win!")
    else:
        print("Wrong accusation. The killer gets away. You lose.")

if __name__ == "__main__":
    display_main_menu()