#Grocery List App
import datetime

time = datetime.datetime.now()
month = str(time.month)
day = str(time.day)
hour = str(time.hour)
minute = str(time.minute)

# Welcome Message

glist = ["Meat", "Cheese"]

print("welcome to the grocery list app")
print("Current date and time: " + month + "/" + day + "\t" + hour + ":" + minute)
print("you currently have " + str(glist) + " in your shopping list.")

add_food1 = input("type of food to add to the grocery list: ")
glist.append(add_food1.title())

add_food2 = input("type of food to add to the grocery list: ")
glist.append(add_food2.title())

add_food3 = input("type of food to add to the grocery list: ")
glist.append(add_food3.title())

glist.sort()
print("here is your grocery list: ")
print(glist)

# Grocery Shopping
print("simulating grocery shopping...")
print("Current grocery list: " + str(len(glist)) + " items\n")

buy1 = input("What item did you just buy?: ").title()
glist.remove(buy1)
print("removing " + str(buy1))

buy2 = input("What item did you just buy?: ").title()
glist.remove(buy2)
print("removing " + str(buy2))

buy3 = input("What item did you just buy?: ").title()
glist.remove(buy3)
print("removing " + str(buy3))



# the store is out of an item
print("\ncurrent grocery list: " + str(len(glist)) + " items.")
noitem = glist.pop()
print("\nSorry the Store is out of " + noitem + ".")
buy4 = input("What food would you like instead?: ").title()
glist.insert(0, buy4)

print("\nHere is what remains in your grocery list: " )
print(glist)

# the buy value changes every time its used, so i could use one value for every buy.