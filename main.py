import random
purchase_list = {"Silver": 500, "Armor": 110, "Weapons": 110, "Food": 110, "Potions": 110, "Fieren Mood": 100, "Stark Mood": 100, "Fern Mood": 100}
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
w_shop = ""
a_shop = ""
m_shop = ""
alley = ""
f_shop = ""
j_shop = ""
## Functions
def main_loop(purchase_list):
    print("\n"+main_menu+"\n")
    choice = input("Choice: ")
    if choice.lower() == "a":
        print(inn)
        choice = input("Choice: ")
        print(choice)
        if choice.lower() == "y":
            purchase_list["Silver"] = purchase_list["Silver"] - 100
            purchase_list["Fieren Mood"] = 100
            purchase_list["Stark Mood"] = 100
            purchase_list["Fern Mood"] = 100
            purchase_list = lose_items(purchase_list)
            main_loop(purchase_list)
        elif choice.lower() == "n":
            main_loop(purchase_list)
    if choice.lower() == "b":
        print()
    if choice.lower() == "c":
        print()
    if choice.lower() == "d":
        print()
    if choice.lower() == "e":
        print()
    if choice.lower() == "z":
        return purchase_list
def lose_items(purchase_list):
    rannum = random.randint(1, 5)
    if rannum == 1:
        if purchase_list["Armor"] > 0:
            purchase_list["Armor"] -= 10
            print("You lost 10 unit of armors!")
            print(bad_news)
    elif rannum == 2:
        if purchase_list["Weapons"] > 0:
            purchase_list["Weapons"] -= 10
            print("You lost 10 unit of weapons!")
            print(bad_news)
    elif rannum == 3:
        if purchase_list["Food"] > 0:
            purchase_list["Food"] -= 10
            print("You lost 10 unit of food!")
            print(bad_news)
    elif rannum == 4:
        if purchase_list["Potions"] > 0:
            purchase_list["Potions"] -= 10
            print("You lost 10 potions!")
            print(bad_news)
    elif rannum == 5:
        print("There was news of a thief in the MainTouwn Inn, but none of your belongings were stolen!")
    return purchase_list
def ending_logic(purchase_list):
    item_total(purchase_list)
    if fieren_magic:
        print(
"""Fieren blew all your stuff on a spell that allows you to detect if an ingredient you don’t want is in your food and is now in debt."""
        )
        print("BAD SPELL ENDING")
        print("Reopen to play again...")
    elif purchase_list["Silver"] < 0:
        print(
"""You have mismanaged your teams funds in your quest for getting the most stuff, the team will now be jailed for not being able to pay their debts."""
)
        print("BAD DEBT ENDING")
        print("Reopen to play again...")
    elif purchase_list["Fieren Mood"] <= 0 or purchase_list["Stark Mood"] <= 0 or purchase_list["Fern Mood"] <= 0:
        print(
"""That person has felt so horrible that they’ve decided to leave the group. The group obviously can’t function without every member, so this will lead to the group’s demise."""
        )
        print("BAD RELATIONSHIP ENDING")
        print("Reopen to play again...")
    elif purchase_list["Food"] :
        print(
"""You have not gotten enough supplies for the team, meaning that they won’t survive (or at least it’ll be thin)."""
        )
        print("BAD SUPPLIES ENDING")
        print("Reopen to play again...")
    else:
        print(
"""You did it! The team is all ready to continue and they’ll be stocked until they get to the next city!"""
        )
        print("GOOD ENDING")
        print("Reopen to play again...")
def item_total(purchase_list):
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


## Main Code
input("31 years after the death of Himmel the Hero... (press Enter to continue)")
print(welcome_script+"\n")
purchase_list = main_loop(purchase_list)
ending_logic(purchase_list)