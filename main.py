from click.termui import clear, pause
from src.game.player import Player
from src.utils.data import fake
from src.utils.ui import fore, intro, welcome, shop_menu, player_menu, game_menu


def display_intro():
    print(fore.GREEN + intro)
    
def display_welcome():
    print(fore.YELLOW + welcome)

def display_menu():
    print(
        fore.YELLOW + f"""
        Available action:
        (1) Explore
        (2) Eat
        (3) Rest
        """
    )
    
def display_status(player):
    print(
        fore.GREEN + f"""
        Your Status:
        {player.name} Level {player.level}
        XP: {player.xp}/100         Coins: {player.coins}
            
        HP: {player.health}         EP: {player.energy}
        Hunger: {player.hunger}     Thirst: {player.thirst}
        """
        )
    
def display_inventory(player):
    print(fore.GREEN + f"""
          Your Inventory:
          Foods: 
            {player.foods_inventory}
            
          Items:
            {player.items_inventory}
          """)

def shop(player):
    clear()
    print(fore.YELLOW + shop_menu)
    item = str(input(fore.MAGENTA + f"{player.name} want to buy: "))
    player.shop(item)

def next_turn(player, check_survive=True):
    if check_survive:
        player.check_survive()
        pause()
        main(player)
    else:
        pause()
        main(player)
    
def main(player):
    clear()
    display_welcome()
    choice = str(input(fore.MAGENTA + "Your choice: "))
    if choice == '1':
        player.explore()
        next_turn(player)
    elif choice == '2':
        food = str(input(fore.MAGENTA + "Food name: "))
        player.eat(food)
        player.drink()
        next_turn(player)
    elif choice == '3':
        hours = int(input(fore.MAGENTA + "Rest for (hour): "))
        player.rest(hours)
        next_turn(player)
    elif choice == 'status':
        display_status(player)
        next_turn(player, check_survive=False)
    elif choice == 'help':
        display_menu()
        next_turn(player, check_survive=False)
    elif choice == 'inventory':
        display_inventory(player)
        next_turn(player, check_survive=False)
    elif choice == 'exit':
        exit()
    else:
        print(fore.RED + "Invalid choice!")
        next_turn(player, check_survive=False)

if __name__ == "__main__":
    try:
        display_intro()
        player_name = str(input(fore.MAGENTA + "Enter your name: "))
        if not player_name:
            player_name = fake.first_name()
            player = Player(player_name)
        else:
            player = Player(player_name)
        main(player)
    except KeyboardInterrupt:
        print("\nProgram closed.")
