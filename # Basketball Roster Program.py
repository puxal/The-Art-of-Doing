# Basketball Roster Program

roster = []
PG = input("Who is your pointguard?:\t").title()
roster.append(PG)
SG = input("Who is your shootingguard?:\t").title()
roster.append(SG)
SF = input("Who is your smallforward?:\t").title()
roster.append(SF)
PF = input("Who is your powerforward?:\t").title()
roster.append(PF)
C = input("Who is your center?:\t").title()
roster.append(C)

print(roster)

# Display a list of all the players
print("\n\t\tYour starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t" + roster[0])
print("\t\t\tShooting Guard: \t" + roster[1])
print("\t\t\tStrong Forward: \t" + roster[2])
print("\t\t\tPower Forward: \t" + roster[3])
print("\t\t\tCenter: \t\t" + roster[4])

# Remove an injured player
injured = roster.pop(2)
roster_length = len(roster)

print("\n\toh no, "+ injured + " is injured.\nYour roster only has " + str(roster_length) + " players")

# add a new player
added = input("who will take " + injured + "'s spot?: ").title()
roster.insert(2, added)

# making a new list

print("\n\t\tYour Starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t" + roster[0])
print("\t\t\tShooting Guard: \t" + roster[1])
print("\t\t\tStrong Forward: \t" + roster[2])
print("\t\t\tPower Forward: \t" + roster[3])
print("\t\t\tCenter: \t\t" + roster[4])
print("\nGood Luck " + roster[2] + ", you will do great!")

print("Your roster has "+ str(len(roster)) + " players.")

roster_length = len(roster)

# Display a list of all the players
print("\n\t\tYour starting 5 for the upcoming basketball season")
print("\t\t\tPoint Guard: \t\t" + roster[0])
print("\t\t\tShooting Guard: \t" + roster[1])
print("\t\t\tStrong Forward: \t" + roster[2])
print("\t\t\tPower Forward: \t" + roster[3])
print("\t\t\tCenter: \t\t" + roster[4])

