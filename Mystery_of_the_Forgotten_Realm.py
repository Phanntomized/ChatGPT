import random

# Inventory to hold items
inventory = []

def start_game():
    print("Welcome to the Mystery of the Forgotten Realm!")
    print("You awaken in a mysterious forest with no memory of how you got there.")
    first_choice()

def first_choice():
    print("\nWhat would you like to do?")
    print("1. Explore the Forest")
    print("2. Follow a Mysterious Light")
    print("3. Climb a Nearby Mountain")
    print("4. Seek Out a Town")
    print("5. Investigate a Ruined Castle")

    choice = input("> ")
    
    if choice == "1":
        explore_forest()
    elif choice == "2":
        follow_light()
    elif choice == "3":
        climb_mountain()
    elif choice == "4":
        seek_town()
    elif choice == "5":
        investigate_castle()
    else:
        print("Invalid choice. Try again.")
        first_choice()

def explore_forest():
    print("\nYou wander deeper into the forest.")
    print("1. Find a Hidden Glade")
    print("2. Follow a River")
    
    choice = input("> ")
    
    if choice == "1":
        hidden_glade()
    elif choice == "2":
        follow_river()
    else:
        print("Invalid choice. Try again.")
        explore_forest()

def follow_light():
    print("\nYou follow the light.")
    print("1. Approach the Light")
    print("2. Ignore the Light")
    
    choice = input("> ")
    
    if choice == "1":
        approach_light()
    elif choice == "2":
        ignore_light()
    else:
        print("Invalid choice. Try again.")
        follow_light()

def climb_mountain():
    print("\nYou begin to climb the mountain.")
    print("1. Reach the Summit")
    print("2. Slip and Fall")
    
    choice = input("> ")
    
    if choice == "1":
        reach_summit()
    elif choice == "2":
        slip_and_fall()
    else:
        print("Invalid choice. Try again.")
        climb_mountain()

def seek_town():
    print("\nYou make your way to a nearby town.")
    print("1. Meet the Locals")
    print("2. Visit the Tavern")
    
    choice = input("> ")
    
    if choice == "1":
        meet_locals()
    elif choice == "2":
        visit_tavern()
    else:
        print("Invalid choice. Try again.")
        seek_town()

def investigate_castle():
    print("\nYou explore the ruined castle.")
    print("1. Explore the Dungeons")
    print("2. Search the Towers")
    
    choice = input("> ")
    
    if choice == "1":
        explore_dungeons()
    elif choice == "2":
        search_towers()
    else:
        print("Invalid choice. Try again.")
        investigate_castle()

# Define character
class Character:
    def __init__(self, name, role):
        self.name = name
        self.role = role

# Define ending functions for each path
def hidden_glade():
    sprite = Character("Lyra", "Sprite")
    print(f"\nIn the hidden glade, you see {sprite.name}, a beautiful {sprite.role}.")
    print("1. Help Lyra with her task.")
    print("2. Demand to be granted a wish.")
    
    choice = input("> ")
    if choice == "1":
        print("Lyra grants you her favor, and you become allies. (Ending 1)")
        inventory.append("Sprite's Favor")
    elif choice == "2":
        print("Lyra curses you for your greed. (Ending 2)")
    else:
        print("Invalid choice. Try again.")
        hidden_glade()

def follow_river():
    print("\nYou follow the river and find a fisherman.")
    print("1. Ask for help.")
    print("2. Steal his catch.")
    
    choice = input("> ")
    if choice == "1":
        print("The fisherman shares his wisdom and gives you a fishing rod. (Ending 3)")
        inventory.append("Fishing Rod")
    elif choice == "2":
        print("The fisherman curses you, and you lose your way. (Ending 4)")
    else:
        print("Invalid choice. Try again.")
        follow_river()

def approach_light():
    print("\nYou approach the light and find it is a portal.")
    print("1. Step through the portal.")
    print("2. Examine it closely.")
    
    choice = input("> ")
    if choice == "1":
        print("You enter a new world filled with wonders. (Ending 5)")
    elif choice == "2":
        print("The portal activates a trap, and you are captured. (Ending 6)")
    else:
        print("Invalid choice. Try again.")
        approach_light()

def ignore_light():
    print("\nYou decide to ignore the light and continue your journey.")
    print("1. Search for treasure.")
    print("2. Look for shelter.")
    
    choice = input("> ")
    if choice == "1":
        print("You find a hidden stash of gold! (Ending 7)")
        inventory.append("Gold")
    elif choice == "2":
        print("You find shelter but are ambushed by bandits. (Ending 8)")
    else:
        print("Invalid choice. Try again.")
        ignore_light()

def reach_summit():
    print("\nAt the summit, you see a magnificent view.")
    print("1. Meditate on your journey.")
    print("2. Shout to the valley below.")
    
    choice = input("> ")
    if choice == "1":
        print("You gain insight and wisdom. (Ending 9)")
    elif choice == "2":
        print("An echo returns, awakening a sleeping giant. (Ending 10)")
    else:
        print("Invalid choice. Try again.")
        reach_summit()

def slip_and_fall():
    print("\nYou slip and fall but land safely in a cave.")
    print("1. Explore the cave.")
    print("2. Call for help.")
    
    choice = input("> ")
    if choice == "1":
        print("You find ancient treasures hidden within. (Ending 11)")
        inventory.append("Ancient Treasure")
    elif choice == "2":
        print("A creature finds you first. (Ending 12)")
    else:
        print("Invalid choice. Try again.")
        slip_and_fall()

def meet_locals():
    print("\nYou meet the locals who seem suspicious.")
    print("1. Gain their trust.")
    print("2. Try to intimidate them.")
    
    choice = input("> ")
    if choice == "1":
        print("You earn their friendship and learn valuable secrets. (Ending 13)")
    elif choice == "2":
        print("They band together and chase you out of town. (Ending 14)")
    else:
        print("Invalid choice. Try again.")
        meet_locals()

def visit_tavern():
    print("\nIn the tavern, you overhear a discussion.")
    print("1. Join the conversation.")
    print("2. Eavesdrop from a distance.")
    
    choice = input("> ")
    if choice == "1":
        print("You become part of a daring quest. (Ending 15)")
        inventory.append("Quest Details")
    elif choice == "2":
        print("You overhear dark plans and decide to leave. (Ending 16)")
    else:
        print("Invalid choice. Try again.")
        visit_tavern()

def explore_dungeons():
    print("\nIn the dungeons, you find a prisoner.")
    print("1. Free the prisoner.")
    print("2. Leave him to his fate.")
    
    choice = input("> ")
    if choice == "1":
        print("The prisoner turns out to be a powerful ally. (Ending 17)")
        inventory.append("Powerful Ally")
    elif choice == "2":
        print("You are caught and imprisoned. (Ending 18)")
    else:
        print("Invalid choice. Try again.")
        explore_dungeons()

def search_towers():
    print("\nIn the towers, you discover a library of forgotten lore.")
    print("1. Read the ancient texts.")
    print("2. Take a book and leave.")
    
    choice = input("> ")
    if choice == "1":
        print("You unlock powerful spells. (Ending 19)")
    elif choice == "2":
        print("The book is cursed, leading to your downfall. (Ending 20)")
    else:
        print("Invalid choice. Try again.")
        search_towers()

# Function to display the inventory
def show_inventory():
    if inventory:
        print("\nYour Inventory:")
        for item in inventory:
            print(f"- {item}")
    else:
        print("\nYour inventory is empty.")

# Add a random event
def random_event():
    events = [
        "You encounter a wandering merchant who offers to trade.",
        "A sudden storm forces you to seek shelter.",
        "You find a hidden path leading to a secret location."
    ]
    print("\n" + random.choice(events))

# Start the game
start_game()
random_event()
show_inventory()
