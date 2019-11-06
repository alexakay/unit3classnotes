
import random #alows the random element to be used in the program
ran_menu = random.randint(1,3) #uses the random element to generate a random number between 1 and 3
print("Welcome to the Greenwood Cafe calorie & credit counter.")
print("TODAY IS DAY " + str(ran_menu)) #the random number that is generated determines what menu day it is, and this line of code prints which menu day it is at the Greenwood cafe
money = int(input("\nHow much money do you want to put on your card?"))
while money < 1.5: #the cheapest item at the cafe is $1.5, so if the user puts less than $1.5 on their card, it will tell them to add more in order to be able to purchase something from the cafe. The program will keep asking them to add more money until their input is greater than 1.5
    print("You cannot purchase anything from the cafe with $" + str(money) + ", please add more money.")
    money = int(input("How much money do you want to put on your card?"))
print("You have $" + str(money) + " on your card.") #tells them how much money is on their card

if ran_menu == 1: #if the random number generate is 1 (meaning it is menu day 1)...
    print("\nYou can buy a maximum of 3 items from the cafe per day.\nIf you made less than 3 purchases, enter 0 when asked what your other purchases were.\nPlease input all menu items as one capital letter.\n\nTODAYS MENU:\nAssorted muffins (M) \nGrilled cheese (G)\nRaspberry smoothie (R)\nVitamin water (V)\nIced tea (I)\nBagel with cream cheese (B)\n")
    item_11 = input(str("What was your first purchase from the cafe today?"))
    while item_11 != "M" and item_11 != "G" and item_11 != "R" and item_11 != "V" and item_11 != "I" and item_11 != "B" and item_11 != "0": #if they enetered something other than the valid inputs (listed in this line), the program will ask them to enter a valid input. It will keep asking them to do so until they have entered a valid menu item
        print("Please enter a valid purchase from the cafe.")
        item_11 = input(str("What was your first purchase from the cafe today?"))
    if item_11 == "M" or item_11 == "G" or item_11 == "R" or item_11 == "V" or item_11 == "I" or item_11 == "B" or item_11 == "0": #if their input was a valid menu item...
        if item_11 == "M":
            item_11 = 150 #this item is 150 calories
            money_11 =  (-2) #this item costs $2 (it is negative because it was easier for me to calculate the card balance if I could add rather than subtract)
            if money < money_11*-1: #if the cost of this item is greater than the amount on their card, it will tell them that they do not have enough on their card to purchase it
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11*-1 #reverses the sign (negative/positive) on the price so that when the card balance is calculated at the end, it doesn't charge the user for an item that they were unable to purchase
                item_11 = 0 #sets calories to 0 so that there aren't calories that they didn't eat on the calorie count at the end
            else:
                money = money + money_11 #if they have enough on their card to purchase this item, the price of this item is subtracted from their card balance (it says + because the cost of the item is a negative number)
            print("\nYour first cafe item was a muffin, 150 calories.")
        if item_11 == "G":
            item_11 = 250
            bacon1 = input("Would you like to add bacon to your grilled cheese? Yes (y), No (n).") #asks if they want to add bacon
            if bacon1 == "y" or bacon1 == "Y": #if they chose yes (uppercase or loweercase y)...
                print("Bacon has been added to your grilled cheese.")
                print("UPDATE: Your first cafe item was a grilled cheese with bacon, 350 calories.")
                item_11 = 350 #changed calories to 350
                money_11 = (-5) #price is $5
                if money < money_11 * -1:
                    print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                    money_11 = money_11 * -1
                    item_11 = 0 #same variable can be used (item_11, money_11) because the variable is only equal to one number in the end, and that value is determined by the user's input
                else:
                    money = money + money_11
            if bacon1 == "n" or bacon1 == "N": #if they chose no (uppercase or lowercase n)...
                print("\nYour first cafe item was a grilled cheese (without bacon), 250 calories.")
                item_11 = 250 #keeps calories at 250
                money_11 = (-4.5) #price without bacon is $4.5
                if money < money_11 * -1:
                    print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                    money_11 = money_11 * -1
                    item_11 = 0
                else:
                    money = money + money_11
        if item_11 == "R":
            item_11 = 100
            print("\nYour first cafe item was a smoothie, 100 calories.")
            money_11 = (-2)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "V":
            item_11 = 130
            print("\nYour first cafe item was a Vitamin water, 130 calories.")
            money_11 = (-1.5)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "I":
            item_11 = 90
            print("\nYour first cafe item was an Iced tea, 90 calories.")
            money_11 = (-1.5)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "B":
            item_11 = 260
            print("\nYour first cafe item was a bagel with cream cheese, 260 calories.")
            money_11 = (-3.5)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 != "0":
            item_21 = input("What was your second purchase from the cafe today?")
        while item_21 != "M" and item_21 != "G" and item_21 != "R" and item_21 != "V" and item_21 != "I" and item_21 != "B" and item_21 != "0":
            print("Please enter a valid purchase from the cafe.")
            item_21 = input(str("What was your second purchase from the cafe today?"))
        if item_21 == "M" or item_21 == "G" or item_21 == "R" or item_21 == "V" or item_21 == "I" or item_21 == "B" or item_21 == "0":
            if item_21 == "M":
                item_21 = 150
                print("Your second cafe item was a muffin, 150 calories.")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "G":
                bacon2 = input("Would you like to add bacon to your grilled cheese? Yes (y), No (n).")
                if bacon2 == "y" or bacon2 == "Y":
                    print("Bacon has been added to your grilled cheese.")
                    print("UPDATE: Your second cafe item was a grilled cheese with bacon, 350 calories.")
                    item_21 = 350
                    money_21 = (-5)
                    if money < money_21 * -1:
                        print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                        money_21 = money_21 * -1
                        item_21 = 0
                    else:
                        money = money + money_21
                if bacon2 == "n" or bacon2 == "N":
                    print("Your second cafe item was a grilled cheese (without bacon), 250 calories.")
                    item_21 = 250
                    money_21 = (-4.5)
                    if money < money_21 * -1:
                        print("You don't have enough on your card to purchase your second item.You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                        money_21 = money_21 * -1
                        item_21 = 0
                    else:
                        money = money + money_21
            if item_21 == "R":
                item_21 = 100
                print("Your second cafe item was a smoothie, 100 calories")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "V":
                item_21 = 130
                print("Your second cafe item was a Vitamin water, 130 calories.")
                money_21 = (-1.5)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "I":
                item_21 = 90
                print("Your second cafe item was an Iced tea, 90 calories.")
                money_21 = (-1.5)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "B":
                item_21 = 260
                print("Your second cafe item was a bagel with cream cheese, 260 calories.")
                money_21 = (-3.5)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "0": #if the user enters 0, it means they did not make a second purchase from the cafe
                item_21 = 0 #0 calories, cause no item eaten
                print("You did not make a second purchase at the cafe.")
                money_21 = 0 #$0, no purchase
            item_31 = input(str("What was your third purchase from the cafe today?"))
        while item_31 != "M" and item_31 != "G" and item_31 != "R" and item_31 != "V" and item_31 != "I" and item_31 != "B" and item_31 != "0":
            print("Please enter a valid purchase from the cafe.")
            item_31 = input(str("What was your third purchase from the cafe today?"))
        if item_31 == "M" or item_31 == "G" or item_31 == "R" or item_31 == "V" or item_31 == "I" or item_31 == "B" or item_31 == "0":
            if item_31 == "M":
                item_31 = 150
                print("Your third cafe item was a muffin, 150 calories.\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "G":
                bacon3 = input("Would you like to add bacon to your grilled cheese? Yes (y), No (n).")
                if bacon3 == "y" or bacon3 == "Y":
                    print("Bacon has been added to your grilled cheese.")
                    print("UPDATE: Your third cafe item was a grilled cheese with bacon, 350 calories.\n")
                    item_31 = 350
                    money_31 = (-5)
                    if money < money_31 * -1:
                        print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                        money_31 = money_31 * -1
                        item_31 = 0
                    else:
                        money = money + money_31
                elif bacon3 == "n" or bacon3 == "N":
                    print("Your third cafe item was a grilled cheese (without bacon), 250 calories.\n")
                    item_31 = 250
                    money_31 = (-4.5)
                    if money < money_31 * -1:
                        print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                        money_31 = money_31 * -1
                        item_31 = 0
                    else:
                        money = money + money_31
            if item_31 == "R":
                item_31 = 100
                print("Your third cafe item was a smoothie, 100 calories\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "V":
                item_31 = 130
                print("Your third cafe item was a Vitamin water, 130 calories.\n")
                money_31 = (-1.5)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "I":
                item_31 = 90
                print("Your third cafe item was an Iced tea, 90 calories.\n")
                money_31 = (-1.5)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "B":
                item_31 = 260
                print("Your third cafe item was a bagel with cream cheese, 260 calories.\n")
                money_31 = (-3.5)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "0": #user enters 0 if they do not want to make a third purchase
                item_31 = 0
                print("You did not make a third purchase at the cafe.")
                money_31 = 0
        spent = (money_11 + money_21 + money_31) * (-1)
        total_cal2 = int(item_11 + item_21 + item_31) #adds up the calories from all 3 items
        print("\nYour total amount of cafe calories for today is " + str(total_cal2) + " calories.") #tells user what their total amount of cafe calories for that day was
        print("Your new card balance is $" + (str(money))) #prints their new card balance. We calculated the new value of "money" after each purchase, meaning that money = money + money_11 + money_21 + money_31, which is why there is no equation to find "money" here at the end
    if money == 0:
        print("\nALERT: Your card balance has reached $0. Please add more money to continue purchasing from the cafe.") #if users new card balance is $0, the program informs the user and asks them to add more money in order to keep purchasing from the cafe


if ran_menu == 2:
    print("\nYou can buy a maximum of 3 items from the cafe per day.\nIf you made less than 3 purchases, enter 0 when asked what your other purchases were.\nPlease input all menu items as one capital letter.\n\nTODAYS MENU:\nCroissants (C) \nPure Leaf tea (P)\nMango smoothie (M)\nSun Chips (S)\nFlow water (F)\nBagel BLT (B)\n")
    item_11 = input(str("What was your first purchase from the cafe today?"))
    while item_11 != "C" and item_11 != "P" and item_11 != "M" and item_11 != "S" and item_11 != "F" and item_11 != "B" and item_11 != "0":
        print("Please enter a valid purchase from the cafe.")
        item_11 = input(str("What was your first purchase from the cafe today?"))
    if item_11 == "C" or item_11 == "P" or item_11 == "M" or item_11 == "S" or item_11 == "F" or item_11 == "B" or item_11 == "0":
        if item_11 == "C":
            item_11 = 150
            money_11 =  (-2)
            if money < money_11*-1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11*-1
                item_11 = 0
            else:
                money = money + money_11
            print("\nYour first cafe item was a croissant, 150 calories.")
        if item_11 == "P":
            item_11 = 150
            money_11 = (-2)
            print("Your first cafe item was a Pure Leaf tea, 150 calories.")
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "M":
            item_11 = 100
            print("\nYour first cafe item was a mango smoothie, 100 calories.")
            money_11 = (-2)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "S":
            item_11 = 150
            print("\nYour first cafe item was a bag of Sun chips, 150 calories.")
            money_11 = (-1.5)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "F":
            item_11 = 0
            print("\nYour first cafe item was a Flow water, 0 calories.")
            money_11 = (-2)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "B":
            item_11 = 320
            print("\nYour first cafe item was a bagel BLT, 320 calories.")
            money_11 = (-4)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 != "0":
            item_21 = input("What was your second purchase from the cafe today?")
        while item_21 != "C" and item_21 != "P" and item_21 != "M" and item_21 != "S" and item_21 != "F" and item_21 != "B" and item_21 != "0":
            print("Please enter a valid purchase from the cafe.")
            item_21 = input(str("What was your second purchase from the cafe today?"))
        if item_21 == "C" or item_21 == "P" or item_21 == "M" or item_21 == "S" or item_21 == "F" or item_21 == "B" or item_21 == "0":
            if item_21 == "C":
                item_21 = 150
                print("Your second cafe item was a croissant, 150 calories.")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "P":
                item_21 = 150
                money_21 = (-2)
                print("Your second cafe item is a Pure Leaf tea, 150 calories.")
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "M":
                item_21 = 100
                print("Your second cafe item was a mango smoothie, 100 calories")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "S":
                item_21 = 130
                print("Your second cafe item was a bag of sun chips, 150 calories.")
                money_21 = (-1.5)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "F":
                item_21 = 0
                print("Your second cafe item was a Flow water, 0 calories.")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "B":
                item_21 = 320
                print("Your second cafe item was a bagel BLT, 320 calories.")
                money_21 = (-4)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "0":
                item_21 = 0
                print("You did not make a second purchase at the cafe.")
                money_21 = 0
            item_31 = input(str("What was your third purchase from the cafe today?"))
        while item_31 != "C" and item_31 != "P" and item_31 != "M" and item_31 != "S" and item_31 != "F" and item_31 != "B" and item_31 != "0":
            print("Please enter a valid purchase from the cafe.")
            item_31 = input(str("What was your third purchase from the cafe today?"))
        if item_31 == "C" or item_31 == "P" or item_31 == "M" or item_31 == "S" or item_31 == "F" or item_31 == "B" or item_31 == "0":
            if item_31 == "C":
                item_31 = 150
                print("Your third cafe item was a croissant, 150 calories.\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "P":
                item_31 = 150
                money_31 = (-2)
                print("Your third cafe item is a Pure Leaf tea, 150 calories.")
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "M":
                item_31 = 100
                print("Your third cafe item was a mango smoothie, 100 calories\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "S":
                item_31 = 150
                print("Your third cafe item was a bag of Sun chips, 150 calories.\n")
                money_31 = (-1.5)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "F":
                item_31 = 0
                print("Your third cafe item was a Flow water, 0 calories.\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "B":
                item_31 = 320
                print("Your third cafe item was a bagel BLT, 320 calories.\n")
                money_31 = (-4)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "0":
                item_31 = 0
                print("You did not make a third purchase at the cafe.")
                money_31 = 0
        spent = (money_11 + money_21 + money_31) * (-1)
        total_cal2 = int(item_11 + item_21 + item_31)
        print("\nYour total amount of cafe calories for today is " + str(total_cal2) + " calories.")
        print("Your new card balance is $" + (str(money)))
    if money == 0:
        print("\nALERT: Your card balance has reached $0. Please add more money to continue purchasing from the cafe.")

if ran_menu == 3:
    print("\nYou can buy a maximum of 3 items from the cafe per day.\nIf you made less than 3 purchases, enter 0 when asked what your other purchases were.\nPlease input all menu items as one capital letter.\n\nTODAYS MENU:\nChocolate chip cookie (C) \nPizza slice (P)\nRice Krispy square (R)\nMelon cup (M)\nOreos (O)\nGatorade (G)\n")
    item_11 = input(str("What was your first purchase from the cafe today?"))
    while item_11 != "C" and item_11 != "P" and item_11 != "R" and item_11 != "M" and item_11 != "O" and item_11 != "G" and item_11 != "0":
        print("Please enter a valid purchase from the cafe.")
        item_11 = input(str("What was your first purchase from the cafe today?"))
    if item_11 == "C" or item_11 == "P" or item_11 == "R" or item_11 == "M" or item_11 == "O" or item_11 == "G" or item_11 == "0":
        if item_11 == "C":
            item_11 = 120
            money_11 =  (-1.5)
            if money < money_11*-1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11*-1
                item_11 = 0
            else:
                money = money + money_11
            print("\nYour first cafe item was a chocolate chip cookie, 120 calories.")
        if item_11 == "P":
            item_11 = 170
            money_11 = (-3)
            print("Your first cafe item was a slice of pizza, 170 calories.")
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "R":
            item_11 = 110
            print("\nYour first cafe item was a Rice Krispy square, 110 calories.")
            money_11 = (-1.5)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "M":
            item_11 = 90
            print("\nYour first cafe item was a melon cup, 90 calories.")
            money_11 = (-2)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "O":
            item_11 = 160
            print("\nYour first cafe item was Oreos, 160 calories.")
            money_11 = (-2)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 == "G":
            item_11 = 100
            print("\nYour first cafe item was a Gatorade, 100 calories.")
            money_11 = (-2)
            if money < money_11 * -1:
                print("You don't have enough on your card to purchase your first item. You have $" + str(money) + " on your card and this item is $" + str((money_11)*-1))
                money_11 = money_11 * -1
                item_11 = 0
            else:
                money = money + money_11
        if item_11 != "0":
            item_21 = input("What was your second purchase from the cafe today?")
        while item_21 != "C" and item_21 != "P" and item_21 != "R" and item_21 != "M" and item_21 != "O" and item_21 != "G" and item_21 != "0":
            print("Please enter a valid purchase from the cafe.")
            item_21 = input(str("What was your second purchase from the cafe today?"))
        if item_21 == "C" or item_21 == "P" or item_21 == "R" or item_21 == "M" or item_21 == "O" or item_21 == "G" or item_21 == "0":
            if item_21 == "C":
                item_21 = 120
                print("Your second cafe item was a chocolate chip cookie, 120 calories.")
                money_21 = (-1.5)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "P":
                item_21 = 170
                money_21 = (-3)
                print("Your second cafe item is a slice of pizza, 170 calories.")
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "R":
                item_21 = 110
                print("Your second cafe item was a Rice Krispy squre, 110 calories")
                money_21 = (-1.5)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "M":
                item_21 = 90
                print("Your second cafe item was a melon cup, 90 calories.")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "O":
                item_21 = 160
                print("Your second cafe item was Oreos, 160 calories.")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "G":
                item_21 = 100
                print("Your second cafe item was a Gatorade, 100 calories.")
                money_21 = (-2)
                if money < money_21 * -1:
                    print("You don't have enough on your card to purchase your second item. You have $" + str(money) + " on your card and this item is $" + str((money_21)*-1))
                    money_21 = money_21 * -1
                    item_21 = 0
                else:
                    money = money + money_21
            if item_21 == "0":
                item_21 = 0
                print("You did not make a second purchase at the cafe.")
                money_21 = 0
            item_31 = input(str("What was your third purchase from the cafe today?"))
        while item_31 != "C" and item_31 != "P" and item_31 != "R" and item_31 != "M" and item_31 != "O" and item_31 != "G" and item_31 != "0":
            print("Please enter a valid purchase from the cafe.")
            item_31 = input(str("What was your third purchase from the cafe today?"))
        if item_31 == "C" or item_31 == "P" or item_31 == "R" or item_31 == "M" or item_31 == "O" or item_31 == "G" or item_31 == "0":
            if item_31 == "C":
                item_31 = 120
                print("Your third cafe item was a chocolate chip cookie, 120 calories.\n")
                money_31 = (-1.5)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "P":
                item_31 = 170
                money_31 = (-3)
                print("Your third cafe item is a slice of pizza, 170 calories.")
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "R":
                item_31 = 110
                print("Your third cafe item was a Rice Krispy square, 110 calories\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "M":
                item_31 = 90
                print("Your third cafe item was a melon cup, 90 calories.\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "O":
                item_31 = 160
                print("Your third cafe item was Oreos, 160 calories.\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "G":
                item_31 = 100
                print("Your third cafe item was a Gatorade, 100 calories.\n")
                money_31 = (-2)
                if money < money_31 * -1:
                    print("You don't have enough on your card to purchase your third item. You have $" + str(money) + " on your card and this item is $" + str((money_31)*-1))
                    money_31 = money_31 * -1
                    item_31 = 0
                else:
                    money = money + money_31
            if item_31 == "0":
                item_31 = 0
                print("You did not make a third purchase at the cafe.")
                money_31 = 0
        spent = (money_11 + money_21 + money_31) * (-1)
        total_cal2 = int(item_11 + item_21 + item_31)
        print("\nYour total amount of cafe calories for today is " + str(total_cal2) + " calories.")
        print("Your new card balance is $" + (str(money)))
    if money == 0:
        print("\nALERT: Your card balance has reached $0. Please add more money to continue purchasing from the cafe.")