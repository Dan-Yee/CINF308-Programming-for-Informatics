from select import select


bossDamageMultiplier = 1
playerDamageMultiplier = 1
bossHealthMultiplier = 1

gameDifficulties = tuple(["EASY", "NORMAL", "HARD"])
armorOptions = tuple([25, 50, 75])
weaponOptions = tuple([50, 75, 150, 200])
skillOptions = tuple(["DAMAGE", "ARMOR", "HEALTH"])

player = {"HEALTH" : 300,
            "ARMOR" : 100,
            "DAMAGE" : 100,
            "HEALING" : list()
            }

boss = {"HEALTH" : 500,
        "DAMAGE" : 100
        }

"""
Function to display the current stats of the player: health remaining, armor remaining, weapon damage, available healing potions
"""
def displayPlayerStats():
    print("Your current stats:")
    print("Health:", player["HEALTH"])
    print("Armor:", player["ARMOR"])
    print("Weapon Damage:", player["DAMAGE"])
    print("Available Healing", player["HEALING"])

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
    displayPlayerStats()

startGame()