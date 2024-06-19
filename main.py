from readchar import readkey, key
import os
import time
import random
import math
import sys

dp = 0

ac = 10

italic = '\x1B[3m'
darkred = '\033[38;2;100;1;1m'
red = '\033[38;2;255;0;0m'
orange = '\033[38;2;255;90;0m'
gold = '\033[38;2;230;190;0m'
silver = '\033[38;2;221;221;221m'
copper = '\033[38;2;170;44;0m'
paleyellow = '\033[38;2;255;255;215m'
yellow = '\033[38;2;255;255;0m'
green = '\033[38;2;00;135;00m'
lime = '\033[38;2;00;255;00m'
darkgrey = '\033[38;2;100;100;100m'
turquoise = '\033[38;2;0;255;255m'
teal = '\033[38;2;0;170;170m'
blue = '\033[38;2;0;0;221m'
purple = '\033[38;2;140;0;240m'
white = '\033[38;2;255;255;255m'
normal = '\033[1m'
clearf = '\033[0m'
platinum = '\033[38;2;205;192;255m'

classcolours = [red, silver, blue, gold, lime, paleyellow, darkred, green]

wait = ""

classes = ["warrior", "rogue", "mage", "cleric", "druid", "monk", "berserker", "ranger"]
classdescriptions = [
    "'Strike strong, defend stronger.' Warriors are masterful at using melee weapons paired with shields to both defend and attack. They excel as all-rounders with a balanced approach to offense and defense.", "'Attack swiftly, and use your knife skills to your advantage.' Rogues excel at debilitating their opponents with bleed effects while dealing high damage with knives. They are swift and adept at damage over time.", "'Feel the mana surging through you.' Mages are adept arcanists, harnessing all forms of magic - from arcane, to holy, to natural. They excel in area-of-effect and burst damage.", "'Let those who defy you feel the wrath of the divine.' Clerics are powerful mages who call upon divine might. They excel as healers and light mages, and are also proficient with warhammers. They are versatile in healing, area-of-effect, and damage-dealing.", "'Face nature with open arms and your foes will face it too.' Druids harness the power of nature - summoning storms, controlling plants, and transforming into beasts. They are bulky units with strong DPS and area-of-effect burst capabilities.", "'Land blow after blow, burdened by nothing in your fists.' Monks rely on their fists, honed through years of training, to rapidly strike their foes. They are swift attackers, specializing in double strike DPS.", "'Let your primal fury within guide your blade.' Berserkers channel their fury in battle, honing their combat skills while becoming more vulnerable. They excel in dealing insane DPS and can function as bulky tanks.", "'Your enemies lie helpless before they even see you.' Rangers are experts with the bow and crossbow, able to snipe enemies from a distance, often before being detected. They excel in ranged combat and are proficient in single-strike and continuous DPS."]

styles = ["swift", "strong", "magic", "tough"]

actions = ["Attack", "Run"]

enemies = []

ask = ""

inventory = []
spells = []
activespells = []

enemy1hp = 0
enemy2hp = 0
enemy3hp = 0

enemy1dmg = 0
enemy1weapon = ""
enemy2dmg = 0
enemy2weapon = ""
enemy3dmg = 0
enemy3weapon = ""

maxhp = 0
hp = 0
xp = 0
lvl = 0
knives = 20
knifetier = 1

damageMult = 0

weaponeq = ""
shieldeq = ""
armoreq = ""
helmeteq = ""
talisman1eq = ""

askeq = ""

def chooseclass():
    global classes, classdescriptions, selectedclass, maxhp, hp, knives, xp, lvl, actions, spells, inventory, knifetier
    currentclass = 0
    os.system("clear")
    print("Which class would like to select?")
    time.sleep(2)
    os.system("clear")
    selectedclass = ""
    while selectedclass == "":
        os.system("clear")
        print(clearf + classcolours[currentclass] + normal + "["+classes[currentclass].capitalize()+ "]")
        print(clearf + italic + classdescriptions[currentclass])
        print(clearf + normal + "<"+" "*(len(classes[currentclass]))+">")
        print("[ENTER] to select your class.")
        keyInput = readkey()
        if keyInput == key.LEFT:
            time.sleep(0.1)
            if currentclass > 0:
                currentclass -= 1
            else:
                currentclass = 7
        if keyInput == key.RIGHT:
            time.sleep(0.1)
            if currentclass < 7:
                currentclass += 1
            else:
                currentclass = 0
        if keyInput == key.ENTER:
            time.sleep(1)
            selectedclass = classes[currentclass]
    if selectedclass in classes:
        if selectedclass == "warrior" or selectedclass == "Warrior":
            selectedclass = "warrior"
            maxhp = 12
            inventory.append("bronze sword")
            inventory.append("wooden shield")
        elif selectedclass == "druid" or selectedclass == "Druid":
            selectedclass = "druid"
            maxhp = 8
            inventory.append("basic staff")
            actions.append("magic")
            spells.append("thorn lash")
            spells.append("wild shape")
        elif selectedclass == "cleric" or selectedclass == "Cleric":
            selectedclass = "cleric"
            maxhp = 8
            inventory.append("basic staff")
            inventory.append("holy charm")
            actions.append("magic")
            spells.append("heal I")
            spells.append("purge")
        elif selectedclass == "monk" or selectedclass == "Monk":
            selectedclass = "monk"
            maxhp = 10
            inventory.append("batle staff")
            inventory.append("white belt")
        elif selectedclass == "rogue" or selectedclass == "Rogue":
            selectedclass = "rogue"
            maxhp = 6
            inventory.append("bronze dagger")
            actions.append("knife throw")
            knives = 20
            knifetier = 1
            inventory.append("throwing knifes")
        elif selectedclass == "berserker" or selectedclass == "Berserker":
            selectedclass = "berserker"
            maxhp = 14
            inventory.append("bronze sword")
            actions.append("rage")
        elif selectedclass == "ranger":
            selectedclass = "ranger"
            maxhp = 8
            inventory.append("oaken longbow")
            inventory.append("bandit mask")
        elif selectedclass == "mage" or selectedclass == "Mage":
            selectedclass = "mage"
            maxhp = 6
            inventory.append("basic staff")
            actions.append("magic")
            spells.append("frozen bolt")
            spells.append("regenerate")
        print("Cool! You are now a " + selectedclass + ".")
        print("")
        hp = maxhp
        lvl = 1
        xp = 0

def selecteqtut():
    global inventory, weaponeq, armoreq, helmeteq, shieldeq, talisman1eq
    while len(inventory) > 0:
        print(f"Current Inventory: {inventory}")
        print(f"Current Equipped:\nWeapon: {weaponeq}\nArmor: {armoreq}\nHelmet: {helmeteq}\nShield: {shieldeq}\nTalisman #1: {talisman1eq}")
        print("Would you like to equip anything? (for the tutorial, equip everything you have! (state the index of your item e.g. item 1 is 0, item 2 is 1, item 3 is 2 etc etc)")
        askeq = input("> ")
        if askeq == "0":
            if inventory[0] == "bronze sword":
                inventory.remove("bronze sword")
                weaponeq = "bronze sword"
            elif inventory[0] == "basic staff":
                inventory.remove("basic staff")
                weaponeq = "basic staff"
            elif inventory[0] == "battle staff":
                inventory.remove("battle staff")
                weaponeq = "battle staff"
            elif inventory[0] == "bronze dagger":
                inventory.remove("bronze dagger")
                weaponeq = "bronze dagger"
            elif inventory[0] == "oaken longbow":
                inventory.remove("oaken longbow")
                weaponeq = "oaken longbow"
        elif askeq == "1":
            if inventory[1] == "wooden shield":
                inventory.remove("wooden shield")
                shieldeq = "wooden shield"
            elif inventory[1] == "holy charm":
                inventory.remove("holy charm")
                talisman1eq = "holy charm"
            elif inventory[1] == "bandit mask":
                inventory.remove("bandit mask")
                helmeteq = "bandit mask"
    print("Good job on equipping everything! lets finish the tutorial now!")

def fight():
    global enemies, enemy1hp, enemy2hp, enemy3hp, enemy1dmg, enemy2dmg, enemy3dmg, enemy1weapon, enemy2weapon, enemy3weapon, ask, actions, damageMult
    if len(enemies) == 1:
      print("You see a " + enemies[0] + "!")
    if len(enemies) == 2:
      print("You see a " + enemies[0] + " and a " + enemies[1] + "!")
    if len(enemies) == 3:
      print("You see a " + enemies[0] + ", a " + enemies[1] + " and a " + enemies[2] + "!")
    enemy1hp = 0
    enemy2hp = 0
    enemy3hp = 0
    enemy1dmg = 0
    enemy1weapon = ""
    enemy2dmg = 0
    enemy2weapon = ""
    enemy3dmg = 0
    enemy3weapon = ""

    if enemies[0] == "goblin":
        enemy1hp = 6
        enemy1dmg = 2
        enemy1weapon = "slashes you with a dagger"
    if len(enemies) >= 2:
        if enemies[1] == "goblin":
            enemy1hp = 6
            enemy1dmg = 2
            enemy1weapon = "slashes you with a dagger"
        if len(enemies) == 3:
            if enemies[2] == "goblin":
                enemy1hp = 6
                enemy1dmg = 2
                enemy1weapon = "slashes you with a dagger"

    while len(enemies) > 0:
        print("What would you like to do? ")
        print(actions[:])
        ask = input("\n> ")
    
        if ask != "attack" or ask != "run" or ask != "magic" or ask != "knife throw" or ask != "rage":
            print("not a valid action!")
        if ask == "attack":
            pass
        if ask == "run":
            print("You ran away! maybe next time!")
            menu()
        if ask == "magic":
            pass
        if ask == "knife throw":
            pass
        if ask == "rage":
            print("Damage increased by 8% for this battle!")
            damageMult = 1.08
    
def start():
    global enemies, wait
    print("Welcome to Celestial Chronicles!")
    time.sleep(2)
    print("First of all, we need a few quick things to start building your character.")
    time.sleep(3.5)
    chooseclass()
    time.sleep(1)
    selecteqtut()
    time.sleep(1)
    print("[ENTER] to continue.")
    wait = input("")
    print("Next, let's test your skills on a goblin to get you used to this game.")
    time.sleep(1)
    enemies.append("goblin")
    fight()
    time.sleep(2)

def menu():
    pass # main menu do later

start()
