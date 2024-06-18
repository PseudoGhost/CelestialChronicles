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

classes = ["warrior", "rogue", "mage", "cleric", "druid", "monk", "berserker", "ranger"]
classdescriptions = [
    "'Strike strong, defend stronger.' Warriors are masterful at using melee weapons paired with shields to both defend and attack. They excel as all-rounders with a balanced approach to offense and defense.", "'Attack swiftly, and use your knife skills to your advantage.' Rogues excel at debilitating their opponents with bleed effects while dealing high damage with knives. They are swift and adept at damage over time.", "'Feel the mana surging through you.' Mages are adept arcanists, harnessing all forms of magic - from arcane, to holy, to natural. They excel in area-of-effect and burst damage.", "'Let those who defy you feel the wrath of the divine.' Clerics are powerful mages who call upon divine might. They excel as healers and light mages, and are also proficient with warhammers. They are versatile in healing, area-of-effect, and damage-dealing.", "'Face nature with open arms and your foes will face it too.' Druids harness the power of nature - summoning storms, controlling plants, and transforming into beasts. They are bulky units with strong DPS and area-of-effect burst capabilities.", "'Land blow after blow, burdened by nothing in your fists.' Monks rely on their fists, honed through years of training, to rapidly strike their foes. They are swift attackers, specializing in double strike DPS.", "'Let your primal fury within guide your blade.' Berserkers channel their fury in battle, honing their combat skills while becoming more vulnerable. They excel in dealing insane DPS and can function as bulky tanks.", "'Your enemies lie helpless before they even see you.' Rangers are experts with the bow and crossbow, able to snipe enemies from a distance, often before being detected. They excel in ranged combat and are proficient in single-strike and continuous DPS."]

styles = ["swift", "strong", "magic", "tough"]

actions = ["Attack", "Defend", "Run"]

inventory = []
actions = []
spells = []

def chooseclass():
    global classes, classdescriptions, selectedclass, eqweapon, eqoffhand, eqhelm, maxhp, atkbonus, hp, magicbonus, throwingknife, xp, lvl, actions, spells, inventory
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
            maxhp = 10
            atkbonus = 1
            eqweapon = "bronze sword"
            eqoffhand = "wooden shield"
        elif selectedclass == "druid" or selectedclass == "Druid":
            selectedclass = "druid"
            maxhp = 8
            atkbonus = 0
            eqweapon = "basic staff"
            actions.append("magic")
            spells.append("thorn lash")
            spells.append("wild shape")
        elif selectedclass == "cleric" or selectedclass == "Cleric":
            selectedclass = "cleric"
            maxhp = 8
            atkbonus = 0
            eqweapon = "basic staff"
            inventory.append("bronze warhammer")
            inventory.append("holy charm")
            actions.append("magic")
            spells.append("heal I")
            spells.append("purge")
        elif selectedclass == "monk" or selectedclass == "Monk":
            selectedclass = "monk"
            maxhp = 8
            atkbonus = 1
        elif selectedclass == "rogue" or selectedclass == "Rogue":
            selectedclass = "rogue"
            maxhp = 8
            atkbonus = 1
            eqweapon = "bronze dagger"
            actions.append("knife throw")
            throwingknife = 20
            locationactions.append("throwing knifes")
        elif selectedclass == "berserker" or selectedclass == "Berserker":
            selectedclass = "berserker"
            maxhp = 12
            atkbonus = 1
            eqweapon = "bronze sword"
            actions.append("rage")
        elif selectedclass == "ranger":
            selectedclass = "ranger"
            maxhp = 9
            atkbonus = 1
            eqweapon = "oaken longbow"
        elif selectedclass == "mage" or selectedclass == "Mage":
            selectedclass = "mage"
            maxhp = 6
            atkbonus = 0
            eqweapon = "basic staff"
            actions.append("magic")
            spells.append("magic missile")
        print("Cool! You are now a " + selectedclass + ".")
        print("")
        hp = maxhp
        lvl = 1
        xp = 0

def choosestyle():
    global style, atkbonus, magicbonus, ac, maxhp, hp, styleb, styles
    print("Next, which style would you like to play?")
    print("["+turquoise+"Swift,"+ red +" strong,"+purple+" magic, "+ white + "or"+green + " tough"+ white + "?]")
    styleb = input("Style: " + normal).lower()
    if stylep in styles:
        if stylep == "swift":
            style = "agile"
            ac = ac + 1
        elif stylep == "strong":
            style = "strong"
            atkbonus = atkbonus + 1
        elif stylep == "magic":
            style = "magical"
            magicbonus = magicbonus + 1
        elif stylep == "tough":
            style = "tough"
            maxhp = maxhp + 1
            hp = hp + 1
        print("Nice! You are a " + style + " person.")
        print("")
    else:
        print("Just saying, that's not a style that you can have. Maybe it will come soon!")
        print("")
        time.sleep(2)
        os.system("clear")
        choosestyle()

def fight():
    pass # do this soon!

def start():
    global enemies, dp
    dp = 1
    print("Welcome to Celestial Chronicles!")
    time.sleep(2)
    print("First of all, we need a few quick things to start building your character.")
    time.sleep(2)
    chooseclass()
    time.sleep(1)
    choosestyle()
    time.sleep(1)
    print("[ENTER] to continue.")
    wait = input("")
    print("Next, let's test your fighting skills on a goblin to get you used to this game.")
    time.sleep(1)
    enemies.append("goblin")
    fight()
    time.sleep(2)
