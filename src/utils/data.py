import faker

fake = faker.Faker()

foods = ["Berries", "Apple", "Chicken", "Rabbit"]
loots = ["Sword"]
foods_energy = {
    "Berries": 5,
    "Apple": 7,
    "Chicken": 15,
    "Rabbit": 10,
    "Golden Apple": 20,
}
items_durability = {"Axe": 100, "Pickaxe": 100, "Sword": 100}
shop_items = {"Axe": 10, "Pickaxe": 15, "Golden Apple": 100, "Totem of Undying": 1000}
enemies = [{"name": "Skeleton", "health": 20, "damage": 10, "level": 1, "xp": 20},
           {"name": "Goblin", "health": 25, "damage": 7, "level": 1, "xp": 20},
           {"name": "Orc", "health": 25, "damage": 15, "level": 1, "xp": 25},
           {"name": "Shaman", "health": 25, "damage": 20, "level": 2, "xp": 35}]
