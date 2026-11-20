import random
purchase_list = {"Silver": 500, "Armor": 0, "Weapons": 0, "Food": 0, "Potions": 0, "Team Mood": 100}
fieren_magic = False
## Scripts
welcome_script = "Frieren, Stark, and Fern are in a city, refuelling before continuing on their journey to the demon king’s palace. "
welcome_script = welcome_script + "They have 500 silver to spend, and need to maintain their equipment, fix their clothing, "
welcome_script = welcome_script + "get a lot of potions, (stone) bread, and other consumables considering that they won't be seeing "
welcome_script = welcome_script + "a city for a while. Lastly make sure to keep everyone somewhat happy!"
main_menu = "Lumiose city:"+"\n"+"  "+"A - Go to an Inn"+"\n"+"  "+"B - Weapons Shop"+"\n"+"  "+"C - Armor Shop"+"\n"+"  "
main_menu = main_menu+"D - Magic Shop"+"\n"+"  "+"E - Go Down an Alley"+"\n"+"  "+"Z - Leave the city"
inn = """
Welcome to the MainTouwn Inn! A room will cost 100 silver, and will rest your team back to normal. Would you like to stay here?
    Y - Yes
    N - No
"""
bad_news = "While you were resting, a thief snuck into your room and stole some of your items!"
w_shop = """
Welcome to Too Pointy Too Stabby! Where we sell weapons so pointy that not even we can handle them!
    1/Q - 40 Credits (Team Worth: 30) - Secondhand and used weapons
    2/W - 83 Credits (Team Worth: 50) - Weapon repair
    3/E - 174 Credits (Team Worth: 100) - Brand new fancy weapons
    Z - Go back to the city
"""
a_shop = """
Welcome to Blocked! Making sure all damage gets blocked!
    1/Q - 31 Credits (Team Worth: 30) - Old, used, and dingy armor
    2/W - 66 Credits (Team Worth: 50) - Armor repair
    3/E - 139 Credits (Team Worth: 100) - High impact peformance armor
    Z - Go back to the city
"""
m_shop = """
Welcome to Albus Dumbledore's Magic Emporium! The old shopkeeper sees that one of your team members is more magic inclined, it's best if you get in and get out.
    1/Q - 16 Credits (Team Worth: 30) - Magic Spell
    2/W - 34 Credits (Team Worth: 50) - 10 potions
    3/E - 71 Credits (Team Worth: 100) - Magic item
    Z - Go back to the city
"""
alley = """
You enter into a dark alley, it's a bit of a squeeze but your team make it through. On the other side you see some local vendors, only 2 pique your interest.
    F - A vendor selling food
    G - A vendor selling jewelry and perfume
    Z - Go back to the city
"""
f_shop = """
The guy running the food stand actually has hot foods available, but considering that you are buying for a journey, they might not have the same value as prepared foods.
    1/Q - 36 Credits (Team Worth: 30) - Hot snacks
    2/W - 17 Credits (Team Worth: 50) - Prepared foods (stone bread)
    3/E - 8 Credits (Team Worth: 100) - Leftovers (Previous days)
    Z - Go back to the alley
"""
j_shop = """
The woman running the jewelry stand looks like she has a lot of experience, but the items she's selling wil make your team happier.
    1/Q - 24 Credits (Team Worth: 30) - Perfumes
    2/W - 50 Credits (Team Worth: 50) - Matching set of jewelry
    3/E - 105 Credits (Team Worth: 100) - Pure gems
    Z - Go back to the alley
"""
## Functions
def main_loop():
    print("\n"+main_menu+"\n")
    choice = input("Choice: ")
    if choice.lower() == "a":
        inn_logic()
    elif choice.lower() == "b":
        w_shop_logic()
    elif choice.lower() == "c":
        a_shop_logic()
    elif choice.lower() == "d":
        m_shop_logic()
    elif choice.lower() == "e":
        alley_logic()
    elif choice.lower() == "z":
        ending_logic()
    else:
        main_loop()

def inn_logic():
    print(inn)
    choice = input("Choice: ")
    if choice.lower() == "y":
        purchase_list["Silver"] = purchase_list["Silver"] - 100
        purchase_list["Team Mood"] = 100
        lose_items()
        main_loop()
    elif choice.lower() == "n":
        main_loop()
    else:
        inn_logic()
def w_shop_logic():
    print(w_shop)
    choice = input("Choice: ")
    if choice == "1" or choice.lower() == "q":
        purchase_list["Silver"] -= 40
        purchase_list["Weapons"] += 30
        print(f"Silver left: {purchase_list['Silver']}")
        w_shop_logic()
    elif choice == "2" or choice.lower() == "w":
        purchase_list["Silver"] -= 83
        purchase_list["Weapons"] += 50
        print(f"Silver left: {purchase_list['Silver']}")
        w_shop_logic()
    elif choice == "3" or choice.lower() == "e":
        purchase_list["Silver"] -= 174
        purchase_list["Weapons"] += 100
        print(f"Silver left: {purchase_list['Silver']}")
        w_shop_logic()
    elif choice.lower() == "z":
        main_loop()
    else:
        w_shop_logic()
def a_shop_logic():
    print(a_shop)
    choice = input("Choice: ")
    if choice == "1" or choice.lower() == "q":
        purchase_list["Silver"] -= 31
        purchase_list["Armor"] += 30
        print(f"Silver left: {purchase_list['Silver']}")
        a_shop_logic()
    elif choice == "2" or choice.lower() == "w":
        purchase_list["Silver"] -= 66
        purchase_list["Armor"] += 50
        print(f"Silver left: {purchase_list['Silver']}")
        a_shop_logic()
    elif choice == "3" or choice.lower() == "e":
        purchase_list["Silver"] -= 139
        purchase_list["Armor"] += 100
        print(f"Silver left: {purchase_list['Silver']}")
        a_shop_logic()
    elif choice.lower() == "z":
        main_loop()
    else:
        a_shop_logic()
def m_shop_logic():
    print(m_shop)
    choice = input("Choice: ")
    if choice == "1" or choice.lower() == "q":
        purchase_list["Silver"] -= 16
        purchase_list["Potions"] += 30
        print(f"Silver left: {purchase_list['Silver']}")
        fieren_magic = True
        m_shop_logic()
    elif choice == "2" or choice.lower() == "w":
        purchase_list["Silver"] -= 34
        purchase_list["Potions"] += 50
        print(f"Silver left: {purchase_list['Silver']}")
        m_shop_logic()
    elif choice == "3" or choice.lower() == "e":
        purchase_list["Silver"] -= 71
        purchase_list["Potions"] += 100
        print(f"Silver left: {purchase_list['Silver']}")
        fieren_magic = True
        m_shop_logic()
    elif choice.lower() == "z":
        main_loop()
    else:
        fieren_magic = True
        m_shop_logic()
def alley_logic():
    print(alley)
    choice = input("Choice: ")
    if choice.lower() == "f":
        f_shop_logic()
    elif choice.lower() == "g":
        j_shop_logic()
    elif choice.lower() == "z":
        main_loop()
    else:
        alley_logic()
def f_shop_logic():
    print(f_shop)
    choice = input("Choice: ")
    if choice == "1" or choice.lower() == "q":
        purchase_list["Silver"] -= 36
        purchase_list["Food"] += 30
        print(f"Silver left: {purchase_list['Silver']}")
        f_shop_logic()
    elif choice == "2" or choice.lower() == "w":
        purchase_list["Silver"] -= 17
        purchase_list["Food"] += 50
        print(f"Silver left: {purchase_list['Silver']}")
        f_shop_logic()
    elif choice == "3" or choice.lower() == "e":
        purchase_list["Silver"] -= 8
        purchase_list["Food"] += 100
        print(f"Silver left: {purchase_list['Silver']}")
        f_shop_logic()
    elif choice.lower() == "z":
        alley_logic()
    else:
        f_shop_logic()
def j_shop_logic():
    print(j_shop)
    choice = input("Choice: ")
    if choice == "1" or choice.lower() == "q":
        purchase_list["Silver"] -= 24
        purchase_list["Team Mood"] += 30
        print(f"Silver left: {purchase_list['Silver']}")
        j_shop_logic()
    elif choice == "2" or choice.lower() == "w":
        purchase_list["Silver"] -= 50
        purchase_list["Team Mood"] += 50
        print(f"Silver left: {purchase_list['Silver']}")
        j_shop_logic()
    elif choice == "3" or choice.lower() == "e":
        purchase_list["Silver"] -= 105
        purchase_list["Team Mood"] += 100
        print(f"Silver left: {purchase_list['Silver']}")
        j_shop_logic()
    elif choice.lower() == "z":
        alley_logic()
    else:
        j_shop_logic()

def lose_items():
    rannum = random.randint(1, 5)
    if rannum == 1:
        if purchase_list["Armor"] > 0:
            purchase_list["Armor"] -= 10
            print(bad_news)
            print("You lost 10 unit of armors!")
    elif rannum == 2:
        if purchase_list["Weapons"] > 0:
            purchase_list["Weapons"] -= 10
            print(bad_news)
            print("You lost 10 unit of weapons!")
    elif rannum == 3:
        if purchase_list["Food"] > 0:
            purchase_list["Food"] -= 10
            print(bad_news)
            print("You lost 10 unit of food!")
    elif rannum == 4:
        if purchase_list["Potions"] > 0:
            purchase_list["Potions"] -= 10
            print(bad_news)
            print("You lost 10 potions!")
    elif rannum == 5:
        print("There was news of a thief in the MainTouwn Inn, but none of your belongings were stolen!")
def ending_logic():
    item_total()
    if fieren_magic:
        print(
"""Fieren blew all your stuff on a spell that allows you to detect if an ingredient you don’t want is in your food and is now in debt."""
        )
        print("BAD SPELL ENDING")
    elif purchase_list["Silver"] < 0:
        print(
"""You have mismanaged your teams funds in your quest for getting the most stuff, the team will now be jailed for not being able to pay their debts."""
)
        print("BAD DEBT ENDING")
    elif purchase_list["Team Mood"] <= 0:
        print(
"""That person has felt so horrible that they’ve decided to leave the group. The group obviously can’t function without every member, so this will lead to the group’s demise."""
        )
        print("BAD RELATIONSHIP ENDING")
    elif purchase_list["Armor"] < 50 or purchase_list["Weapons"] < 50 or purchase_list["Food"] < 50 or purchase_list["Potions"] < 50:
        print(
"""You have not gotten enough supplies for the team, meaning that they won’t survive (or at least it’ll be thin)."""
        )
        print("BAD SUPPLIES ENDING")
    else:
        print(
"""You did it! The team is all ready to continue and they’ll be stocked until they get to the next city!"""
        )
        print("GOOD ENDING")
    choice = input("Reopen to play again...")
def item_total():
    print("You have left Lumiose City with:")
    print(str(purchase_list["Silver"]),"Silver")
    if purchase_list["Armor"]:
        print(str(purchase_list["Armor"]),"Units of Armor")
    if purchase_list["Weapons"]:
        print(str(purchase_list["Weapons"]),"Units of Weapons")
    if purchase_list["Food"]:
        print(str(purchase_list["Food"]),"Units of Food")
    if purchase_list["Potions"]:
        print(str(purchase_list["Potions"]),"Potions")
    print("")


## Main Code
input("31 years after the death of Himmel the Hero... (press Enter to continue)")
print(welcome_script+"\n")
main_loop()