import random

class Companion:
    def __init__(self, name, skill):
        self.name = name
        self.skill = skill
        self.health = 100
        self.level = 1
        self.experience = 0
        self.relationship = 0  # Relationship level with the player

    def gain_experience(self, points):
        self.experience += points
        print(f"{self.name} gains {points} experience!")
        if self.experience >= 100:  # Level up
            self.level_up()

    def level_up(self):
        self.level += 1
        self.experience = 0
        print(f"{self.name} leveled up! Now at level {self.level}.")

    def change_relationship(self, amount):
        self.relationship += amount
        print(f"{self.name}'s relationship level is now {self.relationship}.")

class AdventureGame:
    def __init__(self):
        self.inventory = {}
        self.health = 100
        self.strength = 10
        self.magic = 10
        self.agility = 10
        self.character_class = ""
        self.gold = 20
        self.quest_completed = False
        self.skill_points = 0
        self.skill_tree = {'strength': 0, 'magic': 0, 'agility': 0}
        self.world_event = ""
        self.companions = []
        self.morality = 0  # New morality system
        self.crafting_materials = {}  # New crafting materials
        self.start_game()

    def start_game(self):
        self.choose_class()
        print(f"\nWelcome, {self.character_class}!")
        self.dynamic_world_event()
        print("You find yourself at a crossroads in a dense forest.")
        self.crossroads()

    def choose_class(self):
        print("Choose your character class:")
        print("1. Warrior (High strength)")
        print("2. Mage (High magic)")
        print("3. Rogue (High agility)")
        choice = input("Choose a class (1/2/3): ")

        if choice == '1':
            self.character_class = 'Warrior'
            self.strength += 5
            print("You chose Warrior! Strength +5.")
        elif choice == '2':
            self.character_class = 'Mage'
            self.magic += 5
            print("You chose Mage! Magic +5.")
        elif choice == '3':
            self.character_class = 'Rogue'
            self.agility += 5
            print("You chose Rogue! Agility +5.")
        else:
            print("Invalid choice. Choose again.")
            self.choose_class()

    def dynamic_world_event(self):
        events = [
            "A terrible drought affects the land, making resources scarce.",
            "A festival is happening in a nearby village, offering many opportunities.",
            "Bandits have started raiding travelers in the area.",
            "A powerful storm has damaged the roads, creating new paths."
        ]
        self.world_event = random.choice(events)
        print("\nDynamic World Event: ", self.world_event)

    def crossroads(self):
        print("\nYou can go left, right, or straight ahead.")
        choice = input("Which way do you want to go? (left/right/straight): ").lower()

        if choice == 'left':
            self.left_path()
        elif choice == 'right':
            self.right_path()
        elif choice == 'straight':
            self.straight_path()
        else:
            print("Invalid choice. Try again.")
            self.crossroads()

    def left_path(self):
        print("\nYou take the left path and encounter a wise old wizard.")
        print("He offers you a choice: a magic wand, a potion, or knowledge of spells.")
        choice = input("Do you choose the wand, potion, or spells? (wand/potion/spells): ").lower()

        if choice == 'wand':
            self.wand_choice()
        elif choice == 'potion':
            self.potion_choice()
        elif choice == 'spells':
            self.spells_choice()
        else:
            print("Invalid choice. Try again.")
            self.left_path()

    def spells_choice(self):
        print("\nYou chose the knowledge of spells!")
        print("You can now cast a fireball or a shield.")
        choice = input("Do you want to cast fireball or shield? (fireball/shield): ").lower()

        if choice == 'fireball':
            print("You cast a fireball and scare off a nearby monster. You gain experience!")
            for companion in self.companions:
                companion.gain_experience(20)
        elif choice == 'shield':
            print("You create a protective shield, but it drains your energy. You must retreat!")
            self.crossroads()
        else:
            print("Invalid choice. Try again.")
            self.spells_choice()

    def right_path(self):
        print("\nYou take the right path and stumble upon a fierce dragon!")
        print("You can either try to fight it, sneak past it, or distract it.")
        choice = input("Do you want to fight, sneak, or distract? (fight/sneak/distract): ").lower()

        if choice == 'fight':
            self.fight_dragon()
        elif choice == 'sneak':
            self.sneak_past_dragon()
        elif choice == 'distract':
            self.distract_dragon()
        else:
            print("Invalid choice. Try again.")
            self.right_path()

    def distract_dragon(self):
        print("\nYou throw a rock to distract the dragon!")
        print("While it investigates, you can either steal its treasure or run away.")
        choice = input("Do you want to steal or run? (steal/run): ").lower()

        if choice == 'steal':
            print("You successfully grab some treasure and escape! You win!")
            for companion in self.companions:
                companion.gain_experience(30)
                self.morality -= 1  # Slightly negative morality
        elif choice == 'run':
            print("You escape safely, but without any treasure. Better luck next time!")
        else:
            print("Invalid choice. Try again.")
            self.distract_dragon()

    def straight_path(self):
        print("\nYou walk straight ahead and find a mysterious cave.")
        print("Inside, you see treasure and a giant spider guarding it.")
        choice = input("Do you want to take the treasure, leave, or investigate further? (take/leave/investigate): ").lower()

        if choice == 'take':
            self.take_treasure()
        elif choice == 'leave':
            self.leave_cave()
        elif choice == 'investigate':
            self.investigate_cave()
        else:
            print("Invalid choice. Try again.")
            self.straight_path()

    def investigate_cave(self):
        print("\nYou decide to investigate further and find a hidden chamber.")
        print("Inside, you discover an ancient scroll and a healing potion.")
        choice = input("Do you want to take the scroll, the potion, or leave? (scroll/potion/leave): ").lower()

        if choice == 'scroll':
            self.inventory['ancient scroll'] = 1
            print("You take the scroll. It might be useful later!")
            self.leave_cave()
        elif choice == 'potion':
            self.inventory['healing potion'] = 1
            print("You take the healing potion! It can restore your health.")
            self.leave_cave()
        elif choice == 'leave':
            print("You leave the items behind and exit the cave.")
            self.leave_cave()
        else:
            print("Invalid choice. Try again.")
            self.investigate_cave()

    def wand_choice(self):
        print("\nYou chose the magic wand!")
        print("With a flick of your wrist, you can cast powerful spells.")
        print("Do you want to use it to heal a nearby animal or create a barrier?")
        choice = input("Choose: heal/barrier: ").lower()

        if choice == 'heal':
            self.health += 20
            print("You heal the animal! Your health is now", self.health)
            print("It guides you to safety. You win!")
            for companion in self.companions:
                companion.gain_experience(50)
                companion.change_relationship(1)
        elif choice == 'barrier':
            print("You create a barrier, but it attracts unwanted attention. You are trapped!")
            self.crossroads()
        else:
            print("Invalid choice. Try again.")
            self.wand_choice()

    def potion_choice(self):
        print("\nYou chose the potion!")
        print("It grants you temporary invisibility.")
        print("Do you want to explore further or escape back?")
        choice = input("Choose: explore/escape: ").lower()

        if choice == 'explore':
            print("You find hidden treasures! You win!")
            for companion in self.companions:
                companion.gain_experience(40)
                companion.change_relationship(1)
        elif choice == 'escape':
            print("You escape safely but with no treasures. Better luck next time!")
        else:
            print("Invalid choice. Try again.")
            self.potion_choice()

    def fight_dragon(self):
        print("\nYou bravely fight the dragon.")
        if self.strength >= 15:
            print("Your strength is enough to defeat the dragon! You win!")
            for companion in self.companions:
                companion.gain_experience(50)
        else:
            print("The dragon defeats you. Game over!")

    def sneak_past_dragon(self):
        print("\nYou sneak past the dragon, but it notices you!")
        print("You must either run away or hide behind a rock.")
        choice = input("Choose: run/hide: ").lower()

        if choice == 'run':
            print("You escape, but leave without treasure. Better luck next time!")
        elif choice == 'hide':
            print("You hide successfully and find a treasure chest behind the rock!")
            self.inventory['treasure chest'] = 1
            print("You now have a treasure chest in your inventory!")
        else:
            print("Invalid choice. Try again.")
            self.sneak_past_dragon()

    def take_treasure(self):
        print("\nYou take the treasure, but the spider wakes up!")
        print("You must run away! Do you want to fight it or flee?")
        choice = input("Choose: fight/flee: ").lower()

        if choice == 'fight':
            if self.strength >= 10:
                print("You defeat the spider and escape with the treasure! You win!")
                for companion in self.companions:
                    companion.gain_experience(40)
            else:
                print("The spider defeats you. Game over!")
        elif choice == 'flee':
            print("You flee, but the treasure is lost. Better luck next time!")
        else:
            print("Invalid choice. Try again.")
            self.take_treasure()

    def leave_cave(self):
        print("\nYou leave the cave safely but feel something is missing...")
        print("You wander back to the crossroads. What will you do now?")
        self.crossroads()

    def random_event(self):
        event = random.choice([
            "You find a healing herb!", 
            "A bandit attacks you!", 
            "You discover a hidden path.",
            "You meet a traveler who offers you a quest.",
            "You stumble upon a merchant selling items."
        ])
        print("\nRandom Event: ", event)
        if event == "You find a healing herb!":
            self.health += 15
            print("Your health increases to", self.health)
        elif event == "A bandit attacks you!":
            if self.strength >= 10:
                print("You fight off the bandit and survive!")
                for companion in self.companions:
                    companion.gain_experience(25)
            else:
                print("The bandit defeats you. Game over!")
        elif event == "You discover a hidden path.":
            print("You explore the hidden path and find a treasure chest!")
            self.inventory['treasure chest'] = 1
            print("You now have a treasure chest in your inventory!")
        elif event == "You meet a traveler who offers you a quest.":
            self.offer_quest()
        elif event == "You stumble upon a merchant selling items.":
            self.visit_merchant()

    def offer_quest(self):
        print("\nThe traveler asks you to find a lost artifact in the cave.")
        choice = input("Do you accept the quest? (yes/no): ").lower()

        if choice == 'yes':
            print("You embark on the quest to find the lost artifact!")
            self.quest_completed = False  # Reset quest status
            self.quest_in_cave()
        else:
            print("You decline the quest and continue your journey.")

    def quest_in_cave(self):
        print("\nYou enter the cave to find the artifact.")
        print("You must navigate through dangerous paths and defeat the guardian.")
        if random.choice([True, False]):
            print("A guardian appears!")
            self.fight_guardian()
        else:
            print("You navigate safely and find the artifact! Quest complete!")
            self.quest_completed = True
            self.gain_skill_points()

    def fight_guardian(self):
        print("\nYou engage in battle with the guardian.")
        if self.strength >= 15:
            print("You defeat the guardian and retrieve the artifact! Quest complete!")
            self.quest_completed = True
            self.gain_skill_points()
            for companion in self.companions:
                companion.gain_experience(50)
        else:
            print("The guardian defeats you. Game over!")

    def gain_skill_points(self):
        self.skill_points += 1
        print("You gain a skill point! You can now improve your skills.")
        self.upgrade_skills()

    def upgrade_skills(self):
        print("\nYou have", self.skill_points, "skill points to spend.")
        print("1. Strength")
        print("2. Magic")
        print("3. Agility")
        choice = input("Which skill do you want to upgrade? (1/2/3): ")

        if choice == '1':
            self.skill_tree['strength'] += 1
            self.strength += 2
            self.skill_points -= 1
            print("Strength upgraded! Current Strength:", self.strength)
        elif choice == '2':
            self.skill_tree['magic'] += 1
            self.magic += 2
            self.skill_points -= 1
            print("Magic upgraded! Current Magic:", self.magic)
        elif choice == '3':
            self.skill_tree['agility'] += 1
            self.agility += 2
            self.skill_points -= 1
            print("Agility upgraded! Current Agility:", self.agility)
        else:
            print("Invalid choice. Try again.")
            self.upgrade_skills()

        if self.skill_points > 0:
            self.upgrade_skills()
        else:
            print("No more skill points available.")

    def visit_merchant(self):
        print("\nThe merchant offers you the following items:")
        print("1. Health Potion (Restores 20 health) - 10 gold")
        print("2. Strength Elixir (Increases strength by 5) - 15 gold")
        print("3. Magic Crystal (Increases magic by 5) - 15 gold")
        print("4. Agility Booster (Increases agility by 5) - 15 gold")
        print("5. Companion Recruitment (Gain a companion) - 25 gold")
        print("6. Crafting materials (10 gold each)")

        choice = input("Which item do you want to buy? (health/strength/magic/agility/companion/crafting/leave): ").lower()

        if choice == 'health':
            if self.gold >= 10:
                self.health += 20
                print("You bought a Health Potion! Your health is now", self.health)
                self.gold -= 10
            else:
                print("You don't have enough gold!")
        elif choice == 'strength':
            if self.gold >= 15:
                self.strength += 5
                print("You bought a Strength Elixir! Your strength is now", self.strength)
                self.gold -= 15
            else:
                print("You don't have enough gold!")
        elif choice == 'magic':
            if self.gold >= 15:
                self.magic += 5
                print("You bought a Magic Crystal! Your magic is now", self.magic)
                self.gold -= 15
            else:
                print("You don't have enough gold!")
        elif choice == 'agility':
            if self.gold >= 15:
                self.agility += 5
                print("You bought an Agility Booster! Your agility is now", self.agility)
                self.gold -= 15
            else:
                print("You don't have enough gold!")
        elif choice == 'companion':
            if self.gold >= 25:
                self.recruit_companion()
                self.gold -= 25
            else:
                print("You don't have enough gold!")
        elif choice == 'crafting':
            self.buy_crafting_materials()
        elif choice == 'leave':
            print("You leave the merchant.")
        else:
            print("Invalid choice. Try again.")
            self.visit_merchant()

    def buy_crafting_materials(self):
        if self.gold >= 10:
            material = input("Which material do you want to buy? (wood/stone/herbs): ").lower()
            if material in self.crafting_materials:
                self.crafting_materials[material] += 1
            else:
                self.crafting_materials[material] = 1
            self.gold -= 10
            print(f"You bought {material}! Your inventory now has {self.crafting_materials}.")
        else:
            print("You don't have enough gold!")

    def recruit_companion(self):
        companions = [
            Companion("Elara", "Healing"),
            Companion("Thorin", "Strength"),
            Companion("Luna", "Agility")
        ]
        new_companion = random.choice(companions)
        self.companions.append(new_companion)
        print(f"You have recruited {new_companion.name} who specializes in {new_companion.skill}!")

    def check_companions(self):
        if self.companions:
            print("\nYour companions:")
            for companion in self.companions:
                print(f"- {companion.name} (Health: {companion.health}, Skill: {companion.skill}, Level: {companion.level})")
        else:
            print("\nYou have no companions.")

    def check_endings(self):
        if self.quest_completed and self.world_event == "A festival is happening in a nearby village, offering many opportunities.":
            print("Congratulations! You are celebrated as a hero in the festival!")
        elif self.quest_completed and self.world_event == "Bandits have started raiding travelers in the area.":
            print("You help defend against the bandits and become a local legend!")
        elif self.morality < 0:
            print("Your choices have led to a dark path. The world remembers you as a villain.")
        else:
            print("Your adventure continues...")

game = AdventureGame()
