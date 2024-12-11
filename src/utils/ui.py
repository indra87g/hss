from colorama import Fore, Back, Style, init

init(autoreset=True)
fore = Fore
back = Back
style = Style

intro = """
        -====== Human Survival Simulator CLI ======-
        Author: indra87g
        Version: v1.0.0
        License: CC BY-NC-SA 3.0
        Github: https://github.com/indra87g/human-survival-simulator
        Bug Report: https://github.com/indra87g/human-survival-simulator/issues
        Documentation: https://indra87g.github.io/human-survival-simulator
        
        * Recomended terminal window size is 120*34 !
        -==========================================-
        """
        
welcome = """
        Welcome!
        You are the brave knight that protect everything you have from dark energy in this corrupted world...
        
        Type "status" to see your current status
        Type "help" to see all advanced action
        Type "inventory" to see your current inventory
        Type "exit" to close the game
        Type "save" or "load" to manage savegame
        
        Can you survive? only You and God know it...
        """

shop_menu = """
        -====== Shop ======-    
        Foods:
          Golden Apple (100c)
          
        Items:
          Axe (10c)
          Pickaxe (15c)
          
        Rare Items:
          Totem of Undying (1000c)
        -====================-
        """

player_menu = """
        1. Search Food     2. Eat Foods
        3. Drink Water     4. Sleep
        5. Chop Tree       6. Shop
        7. Mining
        """

game_menu = """
        97. Save     98. Load     99. Exit
        """