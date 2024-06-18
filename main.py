import time
import os
import sys

Black = "\033[1;30m"
Red = "\033[1;31m"
Green = "\033[1;32m"
Yellow = "\033[1;33m"
Blue = "\033[1;34m"
Purple = "\033[1;35m"
Cyan = "\033[1;36m"
White = "\033[1;37m"
DarkRed = "\033[0;31m"

selectedClass = False
damage = 2
HP = 10
MaxHP = 10
Defense = 20
Dexterity = 0
ActualDefense = 0

EnemyHP = 10.0
EnemyMaxHP = 10.0
EnemyDamage = 1

damageMult = 0
HPMult = 0
DefenseMult = 0
DexterityMult = 0

while True:
    while not selectedClass:
        os.system("clear")
        playerClass = input(f"{White}--- Select Class (Select Class to View Stats) ---\n\n{Green}[{Red}1{Green}] Barbarian\n{Green}[{Red}2{Green}] Sorcerer\n{Green}[{Red}3{Green}] Archer\n{Green}[{Red}4{Green}] Goblin\n\nSelect Number: ")
        if playerClass != "1" and playerClass != "2" and playerClass != "3" and playerClass != "4":
            os.system("clear")
            print(f"{DarkRed}Invalid Input. Try Again.")
            time.sleep(2)
            os.system("clear")
        elif playerClass == "1":
            os.system("clear")
            playerClass = input(f"{White}--- Viewing Barbarian Class ---\n\n{Green}+35% Damage\n+20% HP\n+20% Defense\n-30% Dexterity\n\n{Green}[{Red}1{Green}] Select\n{Green}[{Red}2{Green}] Back\n\nSelect Number: ")
            if playerClass == "1":
                playerClass = "Barbarian"
                selectedClass = True
                damageMult = 1.35
                HPMult = 1.2
                DefenseMult = 1.2
                DexterityMult = 0.7
            else:
                pass
        elif playerClass == "2":
            os.system("clear")
            playerClass = input(f"{White}--- Viewing Sorcerer Class ---\n\n{Green}+60% Damage\n-20% HP\n-20% Defense\n-10% Dexterity\n\n{Green}[{Red}1{Green}] Select\n{Green}[{Red}2{Green}] Back\n\nSelect Number: ")
            if playerClass == "1":
                playerClass = "Sorcerer"
                selectedClass = True
                damageMult = 1.6
                HPMult = 0.8
                DefenseMult = 0.8
                DexterityMult = 0.9
            else:
                pass
        elif playerClass == "3":
            os.system("clear")
            playerClass = input(f"{White}--- Viewing Archer Class ---\n\n{Green}+100% Damage\n-35% HP\n-35% Defense\n-20% Dexterity\n\n{Green}[{Red}1{Green}] Select\n{Green}[{Red}2{Green}] Back\n\nSelect Number: ")
            if playerClass == "1":
                playerClass = "Archer"
                selectedClass = True
                damageMult = 2.0
                HPMult = 0.65
                DefenseMult = 0.65
                DexterityMult = 0.8
            else:
                pass
        elif playerClass == "4":
            os.system("clear")
            playerClass = input(f"{White}--- Viewing Goblin Class ---\n\n{Green}-15% Damage\n+25% HP\n+25% Defense\n+30% Dexterity\n\n{Green}[{Red}1{Green}] Select\n{Green}[{Red}2{Green}] Back\n\nSelect Number: ")
            if playerClass == "1":
                playerClass = "Goblin"
                selectedClass = True
                damageMult = 0.85
                HPMult = 1.25
                DefenseMult = 1.25
                DexterityMult = 1.3
            else:
                pass

    os.system("clear")
    print(f"{White}Welcome to the game {Cyan}Celestial Chronicles{White}.")
    time.sleep(2.6)
    os.system("clear")
    print(f"{White}Just to be clear, dying will result in a {DarkRed}Permanent Loss of everything.")
    time.sleep(4)
    os.system("clear")
    print(f"{White}Proceed with caution. I wish you the best of luck.")
    time.sleep(2.6)
    os.system("clear")
    print(f"{White}Let's Initiate the tutorial now.")
    time.sleep(2.6)
    os.system("clear")
    MaxHP = MaxHP * HPMult
    HP = MaxHP
    damage = damage * damageMult
    while EnemyHP > 0:
        os.system("clear")
        ActualDefense = 0
        attackOption = input(f"{Green} You: {HP}/{MaxHP} - {damage} DMG\n{DarkRed}   VS\n{Red} Enemy: {EnemyHP}/{EnemyMaxHP} - {EnemyDamage} DMG\n\n{Green}[{Red}1{Green}] Attack\n{Green}[{Red}2{Green}] Defend\n\nSelect Number: ")
        if attackOption == "1":
            EnemyHP -= damage
            print(f"{Green}Attacked the monster for {damage} damage!")
            time.sleep(2)
        elif attackOption == "2":
            ActualDefense = Defense * DefenseMult
            print(f"{Green}Defended ourselves! the next attack will do {((1 - (ActualDefense / 100) * 100) * -1)}% less damage!")
            time.sleep(2)
        print(f"{Green}The monster attacked you for {EnemyDamage * (1 - (ActualDefense / 100))} damage!")
        HP -= EnemyDamage * (1 - (ActualDefense / 100))
        if HP < 0:
            print(f"{DarkRed} You Died. Your entire run is over!")
            sys.exit()
        time.sleep(2)
    os.system("clear")
    print("You killed the enemy! Good job completing the tutorial!")
    time.sleep(5)

    os.system("clear")
    print("make a menu system next")
    menuOption = input(f"{White}--- Main Menu ---\n\n{Green}[{Red}1{Green}] Explore for enemies\n{Green}[{Red}2{Green}] Enter the shop\n{Green}[{Red}3{Green}] Coming Soon!\n{Green}[{Red}4{Green}] Coming Soon!\n\nSelect Number: ")
