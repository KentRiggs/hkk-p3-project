from models.initialize_db import initialize_database
from models.user import User
from models.npcs import NPC
from models.response import Response
import random



# response_name_to_delete = "placeholder"
# deletion_success = Response.delete_response("placeholder")

# if deletion_success:
#     print(f"The response with the name '{response_name_to_delete}' was deleted successfully.")
# else:
#     print(f"The response with the name '{response_name_to_delete}' could not be found or deleted.")


# all_responses = Response.list_all_responses()
# for response in all_responses:
#     print(response)

# Response.delete_response("innocent3")

# seventhinnocent = Response(
#     name="seventhinnocent", 
#     responses=["I headed over to do the Asteroids task in Weapons. It's actually kind of fun, despite the tension in the game.", "Not exactly suspicious, but the emergency meeting was called right as I was about to complete a long task. Frustrating timing!", "Honestly, it's anyone's guess. I've been trying to stick with groups to avoid getting picked off. Haven't really noticed anyone acting with a motive."], 
#     is_suspicious=False  # change to true if its a suspicious response
# )

# if seventhinnocent.create_response():
#     print("New response has been created and saved to the database.")
# else:
#     print("Failed to create new response in the database.")

# NPC.update_ascii_art("Kairi", """
# ➖➖🟩🟩🟩
# ➖🟩🟩🟩🟩🟩
# 🟩🟩🟩🟨🟨🟨
# 🟩🟩🟩🟨🟨🟨
# 🟩🟩🟩🟩🟩🟩
# 🟩🟩🟩🟩🟩🟩
# ➖🟩🟩🟩🟩🟩
# ➖🟩🟩➖🟩🟩
# ➖🟩🟩➖🟩🟩""")

# npcs = NPC.list_all_npcs()

# for npc in npcs:
#    print(f"Name: {npc.name}, ASCII Art: {npc.ascii_art}, Is Killer: {npc.is_killer}")


# npc = NPC(name="Batsheva", ascii_art="""
# ➖➖🟨🟨🟨           
# ➖🟨🟨🟨🟨🟨  
# 🟨🟨🟨🟪🟪🟪  
# 🟨🟨🟨🟪🟪🟪   
# 🟨🟨🟨🟨🟨🟨 
# 🟨🟨🟨🟨🟨🟨    
# ➖🟨🟨🟨🟨🟨
# ➖🟨🟨➖🟨🟨    
# ➖🟨🟨➖🟨🟨""", is_killer=False)
# npc_created = npc.create_npc()
# if npc_created:
#     print("NPC created successfully!")
# else:
#     print("Failed to create NPC.")


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
            player_name = input_value.strip()
            user_id, created = User.create_user(player_name)
            user = User.find_user_by_name(player_name)
            if created:
                print(f"\nWelcome, {player_name}! Let's start your first game.")
            else:
                print(f"\nWelcome back, {player_name}! You have {user.wins} wins.")
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
            success = User.delete_user(username_to_delete)
            if success:
                    print(f"User '{username_to_delete}' deleted successfully.")
            else:
                    print("User not found or could not be deleted.")
        elif choice == "2":
             User.list_all_users()
        elif choice == "3":
            print("Returning to the main menu...")
            return
        else:
            print("Invalid choice, please try again.")


def start_investigation(player_name):
    game_over = False
    won = False
    npc_candidates = NPC.list_all_npcs()
    filtered_npcs = [npc for npc in npc_candidates if npc.name not in ["NPC1", "NPC2"]]
    selected_npcs = random.sample(filtered_npcs, 3)
    killer_npc = random.choice(selected_npcs)
    killer_npc.is_killer = True

    responses_pool = {}  


    for npc in selected_npcs:
        if npc.is_killer:
            npc.responses = generate_responses(is_suspicious=True, npc_name=npc.name)
        else:
            npc.responses = generate_responses(is_suspicious=False, npc_name=npc.name)


        unique_response = None
        while unique_response is None or unique_response in responses_pool.values():
            unique_response = random.choice(npc.responses)
        responses_pool[npc.name] = unique_response

    while not game_over:
        print("One of these suspects recently killed somebody.")
        for npc in selected_npcs:
            print(f"Name: {npc.name}")
            print(f"{npc.ascii_art}")

        print("\nPress 1, 2, or 3 to choose which character to investigate.")
        print("Press 4 to accuse a character.")
        print("Press 5 to exit.")
        choice = input("Your choice: ")

        if choice in ["1", "2", "3"]:
            investigate_character(selected_npcs[int(choice) - 1])
        elif choice == "4":
            won = make_accusation(player_name, selected_npcs)
            game_over = True
            if won:
                complete_game(player_name, won=won)
        elif choice == "5":
            print("Thank you for playing. Goodbye!")
            game_over = True
        else:
            print("Invalid choice, please try again.")
    return won

def generate_responses(is_suspicious, npc_name):
    if is_suspicious:
        suspicious_sets = Response.get_suspicious_responses()
        selected_set = random.choice(suspicious_sets)
    else:
        innocent_sets = Response.get_innocent_responses()
        selected_set = random.choice(innocent_sets)
    
    return selected_set[2:]


def investigate_character(npc):
    print(npc.ascii_art)
    print(f"\nYou are now speaking to {npc.name}. Here are some questions you can ask them:")
    questions = ["What were you doing in the last 2 minutes?",
                 "Have you seen anything suspicious?",
                "Do you know who might have a motive?"]
    for i, question in enumerate(questions, 1):
        print(f"{i}. {question}")
    print("4. (Go back).")

    while True:
        choice = input("Choose a question to ask from above: ")

        if choice in ["1", "2", "3"]:
            index = int(choice) - 1  
            question = questions[index]
            response = npc.responses[index] 
            print(f"{npc.name} says: {response}")
        elif choice == "4":
            break
        else:
            print("Invalid choice, please try again.")

def make_accusation(player_name, selected_npcs):
    print("\nWho do you think the killer is?")
    for i, npc in enumerate(selected_npcs, 1):
        print(f"{i}. {npc.name}")
    
    choice = input("Your accusation: ")
    accused_npc = selected_npcs[int(choice) - 1]
    
    if accused_npc.is_killer:
        print("You have excellent judgement! you have identified the killer. You win!")
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
        if won:
            if User.update_user_wins(user_name):

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

if __name__ == "__main__":
    initialize_database()
    display_main_menu()

