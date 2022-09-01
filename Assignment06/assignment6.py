from random import randint
from time import sleep

# multipliers applied to boss damage, boss health, and player damage (default is 1x)
bossDamageMultiplier = 1
bossHealthMultiplier = 1
playerDamageMultiplier = 1

# tuples to represent different game options: difficulty and skill selection
gameDifficulties = tuple(["EASY", "NORMAL", "HARD"])
skillOptions = tuple(["DAMAGE", "ARMOR", "HEALTH"])

# tuples to represent possible random options when giving out armor and weapons from chests
potionOptions = tuple([25, 50, 75])
armorOptions = weaponOptions = tuple([50, 75, 150, 200])

# tuple to represent possible moves for boss fight
playerOptions = tuple(["RUN", "HEAL", "ATTACK"])

# dictionary to represent player information
player = {"HEALTH" : 300,
            "ARMOR" : 100,
            "DAMAGE" : 100,
            "HEALING" : list()
            }

# dictionary to represent boss information
boss = {"HEALTH" : 500,
        "DAMAGE" : 100
        }

"""
Function to display the current stats of the player: health remaining, armor remaining, weapon damage, available healing potions
"""
def displayStats(user):
    if(user == "PLAYER"):
        print("Your current stats:")
        print("Health:", player["HEALTH"])
        print("Armor:", player["ARMOR"])
        print("Weapon Damage:", player["DAMAGE"])
        print("Available Healing", player["HEALING"])
    else:
        print("Boss stats:")
        print("Health:", boss["HEALTH"])
        print("Weapon Damage:", boss["DAMAGE"])

"""
Function that informs the player of the current multipliers being applied based on their selected difficulty
"""
def printMultipliers(difficulty):
    print("Active Multipliers for", difficulty, "mode:")
    print("\tPlayer Weapon Damage: ", playerDamageMultiplier, "x", sep = "")
    print("\tBoss Weapon Damage: ", bossDamageMultiplier, "x", sep = "")
    print("\tBoss Health: ", bossHealthMultiplier, "x", sep = "")

"""
Function that asks the user to select the game difficulty
Changes the multipliers applied to boss damage, boss health, and player damage based on difficulty
Changes the values of boss damage, boss health, and player damage 
"""
def setDifficulty():
    global bossDamageMultiplier
    global bossHealthMultiplier
    global playerDamageMultiplier

    difficulty = input("Please select a difficulty: Easy, Normal, or Hard: ")
    difficulty = difficulty.upper()
    while(difficulty not in gameDifficulties):
        print("Sorry, difficulty not recognized. Please try again.")
        difficulty = input("Please select a difficulty: Easy, Normal, or Hard: ")
        difficulty = difficulty.upper()
    
    if(difficulty == "EASY"):
        bossDamageMultiplier = 0.75
        playerDamageMultiplier = 1.25
        bossHealthMultiplier = 0.75
    elif(difficulty == "HARD"):
        bossDamageMultiplier = 1.25
        playerDamageMultiplier = 0.75
        bossHealthMultiplier = 1.25
    
    boss["HEALTH"] = boss["HEALTH"] * bossHealthMultiplier
    boss["DAMAGE"] = boss["DAMAGE"] * bossDamageMultiplier
    player["DAMAGE"] = player["DAMAGE"] * playerDamageMultiplier
    return difficulty.title()

"""
Function that allows the player to select a skill and apply its benefits to their stats
"""
def selectSkill():
    print("Skill Selection: You may select to have a 1.5x multiplier applied directly to your: Damage, Armor, or Health.")
    skill = input("Where would you like to apply your skill?: ")
    skill = skill.upper()
    while(skill not in skillOptions):
        print("Sorry, that is not an option. Please try again.")
        skill = input("Where would you like to apply your skill?: ")
        skill = skill.upper()
    
    player[skill] = player[skill] * 1.5
    print("You have applied a 1.5x multiplier to your player's", skill.title())

"""
Function for looting a chest. If the player went left, the chest will contain a weapon. If the player went right, the chest will contain armor.
Both chests contain healing potions. However, the weapon chest has less of them compared to the armor chest
"""
def lootChest(direction):
    numOfPotions = 0
    if(direction == "LEFT"):
        # weapon chest
        numOfPotions = randint(1, 5)
        randomWeapon = weaponOptions[randint(0, len(weaponOptions) - 1)]
        sleep(2)
        print("You find a new weapon that does", randomWeapon, "damage.")
        player["DAMAGE"] = randomWeapon
    elif(direction == "RIGHT"):
        # armor chest
        numOfPotions = randint(5, 8)
        randomArmor = armorOptions[randint(0, len(armorOptions) - 1)]
        sleep(2)
        print("You find a new piece of armor that has", randomArmor, "hit points.")
        player["ARMOR"] = randomArmor
    
    sleep(3)
    print("At the bottom of the chest, you find", numOfPotions, "random healing potions.")
    print("(They are added to your healing inventory)")

    for i in range(numOfPotions):
        randomPotion = potionOptions[randint(0, len(potionOptions) - 1)]
        player["HEALING"].append(randomPotion)

"""
Main driver function for the entire game
"""
def startGame():
    print("\nWelcome to my game!")
    difficulty = setDifficulty()
    print("You have selected to play on", difficulty, "mode.\n")
    printMultipliers(difficulty.title())
    print()
    selectSkill()
    print()
    displayStats("PLAYER")
    print()

    # main portion of game
    sleep(2)
    print("You've just departed from home...seeking adventure.")
    sleep(2)
    print("You come across a fork in the road. You can choose to go left or right...")
    sleep(2)
    print("Down the left path, you might get a better weapon for the struggles ahead...")
    sleep(2)
    print("Down the right path, you might get better armor to defend yourself...")
    sleep(2)

    # user to decide which path to take
    print()
    direction = input("Which path do you choose? Left or Right: ")
    direction = direction.upper()
    while(not(direction == "LEFT" or direction == "RIGHT")):
        print("Direction not recognized. Please enter \"left\" or \"right\".")
        direction = input("Which path do you choose? Left or Right: ")
        direction = direction.upper()
    
    print("And down the", direction.lower(), "path you go.")
    sleep(2)

    # loot chest section of game
    print()
    print("On your way, you find an old rusty chest. You open it...")
    lootChest(direction)
    sleep(2)
    print()
    print("You are unable to carry everything you now have and choose to settle for the new loot...")

    sleep(2)
    print()
    displayStats("PLAYER")

    if(randint(0, 1) == 0):                                                             # 50/50 chance of the player to step on a thorn mid-game and lose hit points
        print()
        print("Ow! You stepped on a random thorn on the road and lost 50 health points")
        player["HEALTH"] = player["HEALTH"] - 50
    
    sleep(2)
    print()
    print("As you continue on, you run into a monster.")
    sleep(2)
    displayStats("BOSS")

    sleep(2)
    while(player["HEALTH"] > 0 or boss["HEALTH"] > 0):
        print()
        print("You are face to face with the monster now...")
        sleep(2)
        print()
        print("You have three options: Run, Heal, or Attack")
        playerMove = input("What is your move?: ")
        playerMove = playerMove.upper()
        while(playerMove not in playerOptions):
            print("Move not recognized. Please try again.")
            playerMove = input("What is your move?: ")
            playerMove = playerMove.upper()
        
        sleep(2)
        print()
        if(playerMove == "RUN"):                                                            # player chooses to run from the fight
            print("You run back the way you came, as fast as you could...")
            sleep(2)
            print("You run into another monster. But this time, you are 100% outmatched.")
            sleep(2)
            print("In one fell swoop, you are cut clean in half by the monster. You die.")
            player["HEALTH"] = 0
            break
        elif(playerMove == "ATTACK"):                                                       # player chooses to attack the monster
            print("You choose to fight. You swing at the monster and do", player["DAMAGE"], "hit points to the monster.")
            boss["HEALTH"] = boss["HEALTH"] - player["DAMAGE"]
            sleep(2)
            print()
            displayStats("BOSS")
            if(boss["HEALTH"] <= 0):                                                        # if boss was defeated after player's attack, jump to end game section
                boss["HEALTH"] = 0
                break
        elif(playerMove == "HEAL"):                                                         # player chooses to heal themselves; monster doesn't counter attack
            print("You choose to heal. You look through your collection of healing potions.")
            print(player["HEALING"])
            sleep(2)
            if(len(player["HEALING"]) == 0):                                                # fail safe to make sure player isn't stuck in a loop when there are no potions left
                print("You don't have any healing potions left")
                continue
            print()
            healAmount = int(input("Which amount would you like to heal?: "))
            while(healAmount not in player["HEALING"]):
                print("You do not have that potion. Please choose a different one.")
                healAmount = int(input("Which amount would you like to heal?: "))
            player["HEALTH"] = player["HEALTH"] + healAmount
            player["HEALING"].remove(healAmount)

            sleep(2)
            print("You have healed yourself by", healAmount, "hit points.")
            print()
            displayStats("PLAYER")
            continue
        
        # boss counter attacks
        sleep(2)
        print()
        print("The monster counter attacks you!")
        bossDamage = boss["DAMAGE"]
        if(bossDamage <= player["ARMOR"]):                                                  # player has more armor than boss damage
            player["ARMOR"] = player["ARMOR"] - bossDamage
            print("Your armor has taken the hit...this time.")
        elif(bossDamage > player["ARMOR"]):                                                 # player has less or no armor compared to boss damage
            bossDamage -= player["ARMOR"]
            player["ARMOR"] = 0
            player["HEALTH"] = player["HEALTH"] - bossDamage
            print("Your armor is now broken...you take the brunt of the damage.")

            if(player["HEALTH"] <= 0):                                                      # game over, player was killed
                player["HEALTH"] = 0
                break
        sleep(2)
        print()
        displayStats("PLAYER")

        # boss self-heals by 25 50% of the time
        sleep(2)
        print()
        if(randint(0, 1) == 0):                                                             # 50/50 chance of the monster healing
            print("The monster heals themself by 25 hit points...")
            boss["HEALTH"] = boss["HEALTH"] + 25
        else:
            print("The monster doesn't heal this time.")
        sleep(2)
        displayStats("BOSS")

    # end of game notice
    sleep(2)
    print()
    if(player["HEALTH"] <= 0):                                                              # if player was killed
        print("You were defeated by the monster...")
        sleep(2)
        print("You forgot to tell anyone where you were going...")
        sleep(2)
        print("Your life was not remembered :(")
    elif(boss["HEALTH"] <= 0):                                                              # if monster was defeated
        print("You defeated the monster!")
        sleep(2)
        print("The King of the Empire of Py has recognized you for your skills...")
        sleep(2)
        print("You have been named Commander in Chief of all armed forces.")

    sleep(2)
    print()
    print("Thank you for playing. I worked hard on this game...")
startGame()