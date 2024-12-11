import random, json
from src.utils.data import foods, loots, foods_energy, items_durability, shop_items, enemies
from src.utils.ui import fore, back, style


class Player:
    def __init__(
        self,
        name,
        coins=10,
        health=100,
        hunger=0,
        thirst=0,
        energy=100,
        foods_inventory=None,
        items_inventory=None,
    ):
        self.name = name
        self.coins = coins
        self.health = health
        self.hunger = hunger
        self.thirst = thirst
        self.energy = energy
        self.foods_inventory = foods_inventory if foods_inventory is not None else []
        self.items_inventory = items_inventory if items_inventory is not None else []
        self.xp = 0
        self.level = 1

    def explore(self):
        print(f"You are exploring the wilderness...")
        encounter = random.choice(["food", "enemy", "loot", "nothing"])
        if encounter == "food":
            food_found = random.choice([True, False])
            if food_found:
                food = random.choice(foods)
                print(fore.GREEN + f"{self.name} found some {food}.")
                self.foods_inventory.append(food)
                self.gain_xp(12)
            else:
                print(fore.RED + f"{self.name} found no food.")
                self.update_stats(
                    "bad",
                    random.randint(1, 10),
                    random.randint(1, 10),
                    random.randint(1, 10),
                    random.randint(1, 10),
                )
        elif encounter == "enemy":
            self.fight()
        elif encounter == "loot":
            loot = random.choice(loots)
            print(f"You found a {loot}!")
            self.items_inventory.append(loot)
        elif encounter == "nothing":
            print("You found nothing.")
                        
    def fight(self):
        enemy = random.choice(enemies)
        print(fore.YELLOW + f"You encountered a {enemy['name']}!")
        while enemy["health"] > 0 and self.health > 0:
            print("\nChoose your action")
            print("1. Attack")
            print("2. Defend")
            print("3. Run")
            action = input("> ")
            
            if action == "1":
                if "Sword" in self.items_inventory:
                    damage = random.randint(20, 30)
                    if enemy["level"] > self.level:
                        print(fore.RED + f"{enemy['name']} is too strong! you can only defend or run.")
                    elif self.level > enemy["level"] or self.level == enemy["level"]:
                        enemy["health"] -= damage
                        self.update_items_durability("Sword")
                        print(fore.YELLOW + f"You hit {enemy['name']} with {damage} damage using your sword.") 
                else:
                    damage = random.randint(10, 15)
                    enemy['health'] -= damage
                    print(f"You hit {enemy['name']} with {damage} damage using your hand.")
            elif action == "2":
                reduced_damage = max(enemy['damage'] - random.randint(5, 15), 0)
                self.health -= reduced_damage
                print(f"You defended yourself from {enemy['name']}, and reduce {reduced_damage} damage.")
            elif action == "3":
                if random.choice([True, False]):
                    print("You successfully escaped!")
                    return
                else:
                    print("Oops, you failed to escape!")
            else:
                print("Invalid choice.")
                
            if enemy["health"] > 0:
                self.health -= enemy['damage']
                print(f"{enemy['name']} is attacking with {enemy['damage']} damage.")
        
        if self.health <= 0:
            print(f"You was defeated...")
        else:
            print(f"You defeated the {enemy['name']}!")
            self.gain_xp(enemy['xp'])
            self.coins += random.randint(10, 50)

    def eat(self, food):
        food_energy = foods_energy
        if food in self.foods_inventory:
            self.foods_inventory.remove(food)
            self.update_stats(
                "good",
                min(self.health + 5, 100),
                max(self.hunger - food_energy[food], 0),
                max(self.thirst - 3, 0),
                min(self.energy + food_energy[food], 100),
            )
            self.gain_xp(5 + food_energy[food])
            print(
                fore.GREEN
                + f"You are eats {food} and gains {food_energy[food]} energy."
            )
        else:
            print(fore.RED + f"You doesn't have any {food} to eat.")

    def drink(self):
        print(fore.GREEN + "You are drinks water.")
        self.update_stats("good", 5, 5, 15, 10)
        self.gain_xp(5)

    def rest(self, hours):
        print("You are resting...")
        self.update_stats("neutral", 0, 10 + hours, 15 + hours, 5 * hours)

    def shop(self, item):
        items = shop_items
        if item in items and self.coins >= items[item]:
            self.items_inventory.append(item)
            self.coins -= items[item]
            print(fore.GREEN + f"{self.name} bought {item} for {items[item]} coins.")
        else:
            print(fore.RED + f"{self.name} can't afford {item}.")

    def chop_tree(self):
        if "Axe" in self.items_inventory:
            found_gapple = random.choice([True, False])
            print(fore.GREEN + f"{self.name} is chopping a tree...")
            wood = random.randint(1, 25)
            if found_gapple:
                print(
                    fore.BLUE
                    + back.GREEN
                    + f"Lucky! {self.name} found 1 Golden Apple when chopping a tree!"
                )
                self.foods_inventory.append("Golden Apple")
                self.gain_xp(20 * wood - 5)
            else:
                print(fore.GREEN + f"{self.name} chopped a tree and earned some coins.")
                self.gain_xp(10 + wood)
            self.update_stats(
                "bad", 5, random.randint(5, 30), random.randint(5, 25), 40
            )
            self.update_items_durability("Axe")
            self.coins += random.randint(1, 75)
        else:
            print(fore.RED + f"{self.name} needs an Axe to chop a tree.")

    def mining(self):
        if "Pickaxe" in self.items_inventory:
            found_diamond = random.choice([True, False])
            print(fore.GREEN + f"{self.name} is mining...")
            stone = random.randint(1, 25)
            if found_diamond:
                print(
                    fore.BLUE
                    + back.GREEN
                    + f"Lucky! {self.name} found diamond and earned 150 coin!"
                )
                self.update_stats(
                    "bad",
                    random.randint(5, 50),
                    random.randint(5, 25),
                    random.randint(5, 25),
                    random.randint(5, 50),
                )
                self.coins += 150
                self.gain_xp(30 * stone - 10)
            else:
                print(fore.GREEN + f"{self.name} mined and earned some coins.")
                self.update_stats(
                    "bad",
                    random.randint(1, 25),
                    random.randint(1, 15),
                    random.randint(1, 15),
                    random.randint(1, 25),
                )
                self.coins += random.randint(10, 100)
                self.gain_xp(10 + stone)
            self.update_items_durability("Pickaxe")
        else:
            print(fore.RED + f"{self.name} needs a Pickaxe to mine.")

    def update_stats(self, mode, health, hunger, thirst, energy):
        if mode == "good":
            self.health += health
            self.hunger -= hunger
            self.thirst -= thirst
            self.energy += energy
        elif mode == "bad":
            self.health -= health
            self.hunger += hunger
            self.thirst += thirst
            self.energy -= energy
        elif mode == "neutral":
            self.health += health
            self.hunger += hunger
            self.thirst += thirst
            self.energy += energy

    def update_items_durability(self, items_name):
        items_durability[items_name] -= 20
        if items_durability[items_name] < 1:
            print(fore.RED + f"Oh no!, Your {items_name} is broken!")
            self.items_inventory.remove(items_name)

    def gain_xp(self, amount):
        self.xp += amount
        if self.xp >= self.level * 100:
            self.xp -= self.level * 100
            self.level += 1
            print(
                fore.GREEN
                + back.YELLOW
                + f"{self.name} leveled up to level {self.level}!"
            )
            if self.level == 10:
                print(
                    fore.GREEN
                    + back.YELLOW
                    + f"{self.name}'s health is increased to 150!"
                )
                self.health = 150
            elif self.level == 20:
                print(
                    fore.GREEN
                    + back.YELLOW
                    + f"{self.name}'s energy is increased to 150"
                )
                self.energy = 150

    def check_survive(self):
        if self.health < 1 or self.thirst > 99 or self.hunger > 99 or self.energy < 1:
            if "Totem of Undying" in self.items_inventory:
                print(
                    fore.GREEN
                    + back.YELLOW
                    + f"{self.name} is saved from death by a strong holy power!"
                )
                self.health = 100
                self.hunger = 0
                self.thirst = 0
                self.energy = 50
                self.items_inventory.remove("Totem of Undying")
            else:
                print(fore.RED + f"GAME OVER!\n{self.name} has died.")
                exit()
        else:
            print(fore.GREEN + f"{self.name} is surviving.")

    def save_game(self, filename="savegame.json"):
        state = {
            "name": self.name,
            "coins": self.coins,
            "health": self.health,
            "hunger": self.hunger,
            "thirst": self.thirst,
            "energy": self.energy,
            "foods_inventory": self.foods_inventory,
            "items_inventory": self.items_inventory,
            "xp": self.xp,
            "level": self.level,
        }
        with open(filename, "w") as f:
            json.dump(state, f)
        print(fore.GREEN + f"Game saved to {filename}.")

    def load_game(self, filename="savegame.json"):
        with open(filename, "r") as f:
            state = json.load(f)
        self.name = state["name"]
        self.coins = state["coins"]
        self.health = state["health"]
        self.hunger = state["hunger"]
        self.thirst = state["thirst"]
        self.energy = state["energy"]
        self.foods_inventory = state["foods_inventory"]
        self.items_inventory = state["items_inventory"]
        self.xp = state["xp"]
        self.level = state["level"]
        print(fore.GREEN + f"Game loaded from {filename}")

    """
    TODO: improve this
    
    def lucky_box(self):
        print("Opening lucky box with 10 coins...")
        self.coins -= 10
        win = random.choice([True, False])
        if win:
            print("Nice, You win!")
            self.health = min(self.health + 25, 100)
            self.hunger = 0
        else:
            print("Loser. You lose everything, including your life :)")
            self.health = 0
    """
