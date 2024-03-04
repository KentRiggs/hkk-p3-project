# lib/cli.py
from models.model_1 import engine, Base, session_scope, create_user, delete_user, update_user_wins, find_user_by_name, list_all_users
Base.metadata.create_all(engine)



def display_main_menu():
 game_over = False
 won = False
 choice = ""
 main_menu_active = True
 while main_menu_active:
    print("\nWelcome to the Detective Game!")
    print("Please insert your name or press 1 for the Admin Menu: ", end="")

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
    if game_over and choice == "5":
            print("Thank you for playing. Goodbye!")
            main_menu_active = False
    elif game_over and choice == "4":
            complete_game(player_name, won=won)
            main_menu_active = False
    else:
        input_value = input()
        if input_value == '1':
            admin_menu()
            continue
        elif input_value.strip():
            player_name = input_value
            with session_scope() as session:
                user, created = create_user(player_name, session=session)
                if created:
                    print(f"\nWelcome, {player_name}! Let's start your first game.")
                    won = start_investigation(player_name)
                    game_over = True
                    break
                else:
                    print(f"\nWelcome back, {user.name}! You have {user.wins} wins.")
                    won = start_investigation(player_name)
                    game_over = True
                    break  
        else:
            print("You must enter a valid name to start the game.")
            
def admin_menu():
    while True:
        print("\nAdmin Menu:")
        print("1. Delete a user")
        print("2. List all users")
        print("3. Exit admin menu")
        choice = input("Your choice: ")

        if choice == "1":
            username_to_delete = input("Enter the username to delete: ")
            with session_scope() as session:
                success = delete_user(username_to_delete, session)
                if success:
                    print(f"User '{username_to_delete}' deleted successfully.")
                else:
                    print("User not found or could not be deleted.")
        elif choice == "2":
             with session_scope() as session:
                list_all_users(session)
        elif choice == "3":
            print("Returning to the main menu...")
            return
        else:
            print("Invalid choice, please try again.")


def start_investigation(player_name):
    game_over = False
    won = False
    while not game_over:
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
        print("\nPress 1, 2, or 3 to choose which character to investigate.")
        print("Press 4 to accuse a character.")
        print("Press 5 to exit.")
        choice = input("Your choice: ")

        if choice in ["1", "2", "3"]:
            investigate_character(int(choice))
        elif choice == "4":
            won = make_accusation(player_name)
            game_over = True
            if won:
                complete_game(player_name, won=won)
        elif choice == "5":
            print("Thank you for playing. Goodbye!")
            game_over = True
        else:
            print("Invalid choice, please try again.")
    return won


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

    responses = {
        "Hunter": [
            "Yo, I smashed Heihachi's face in!",
            "While I was gaming Kent seemed to be acting sneaky",
            "I think everyone is jealous of my insane godfist speed."
        ],
        "Kent": [
            "Just making some python visualizations.",
            "Nope, nothing, not at all. No sus here.",
            "Hunter plays that violent fighting game a LOT."
        ],
        "Kairi": [
            "Studying! Study study study all day every day.",
            "Hard to see much other than code and numbers these days.",
            "I think Kent is jealous of Hunter's gaming abilities."
        ]
    }

    while True:
        choice = input("Choose a question to ask from above: ")

        if choice in ["1", "2", "3"]:
            index = int(choice) - 1  
            print(f"{character_name} says: {responses[character_name][index]}")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def make_accusation(player_name):
    print("\nWho do you think the killer is?")
    print("1. Hunter")
    print("2. Kent")
    print("3. Kairi")
    choice = input("Your accusation: ")


    murderer = "2"  
    if choice == murderer:
        print("You have excellent judgement! The Killer has been apprehended.")
        return True
    else:
        print("Wrong accusation. The killer gets away. You lose.")
        print("""
     _       __           _   
    | |     / _|         | |  
  __| | ___| |_ ___  __ _| |_ 
 / _` |/ _ \  _/ _ \/ _` | __|
| (_| |  __/ ||  __/ (_| | |_ 
 \__,_|\___|_| \___|\__,_|\__|
                              
""")
        return False

def complete_game(user_name, won=False):
     with session_scope() as session:
        if won:
            if update_user_wins(user_name, session=session):
                print("Congratulations! Your win has been recorded.")
                print("""  
       _      _                   
      (_)    | |                  
__   ___  ___| |_ ___  _ __ _   _ 
\ \ / / |/ __| __/ _ \| '__| | | |
 \ V /| | (__| || (_) | |  | |_| |
  \_/ |_|\___|\__\___/|_|   \__, |
                             __/ |
                            |___/ 
                      """)
            else:
                print("Couldn't update your wins. Please try again.")
        else:
            print("Better luck next time!")
     return False

if __name__ == "__main__":
    display_main_menu()