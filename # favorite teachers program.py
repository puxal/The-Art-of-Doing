# favorite teachers program
print("welcome to the favorite teachers program")
fav_teachers = []
fav_teachers.append(input("who is your first favorite teacher?: ").title())
fav_teachers.append(input("who is your second favorite teacher?: ").title())
fav_teachers.append(input("who is your third favorite teacher?: ").title())
fav_teachers.append(input("who is your fourth favorite teacher?: ").title())

#summary of list
print("your favorite teachers ranked are: " + str(fav_teachers))
print("your favorite teachers listed alphabetically are: " + str(sorted(fav_teachers)))
print("your favorite teachers reverse alphabetically are: "+ str(sorted(fav_teachers, reverse=True)))
print("your top two favorite teachers are: " + str(fav_teachers[0] + " and " + str(fav_teachers[1])))
print("your next two favorite are: " + str(fav_teachers[2] + " and " + str(fav_teachers[3])))
print("your last favorite teacher is: " + str(fav_teachers[-1]))
print("you have a total of "+ str(len(fav_teachers)) + " favorite teachers.")

# add a new favorite teacher
fav_teachers.insert(0, input("\nOops, " + fav_teachers[0] + " is no longer yur first favrit teacher. Who is your FAVORITE teacher? ").title())

print(fav_teachers)

#summary of list
print("your favorite teachers ranked are: " + str(fav_teachers))
print("your favorite teachers listed alphabetically are: " + str(sorted(fav_teachers)))
print("your favorite teachers reverse alphabetically are: "+ str(sorted(fav_teachers, reverse=True)))
print("your top two favorite teachers are: " + str(fav_teachers[0] + " and " + str(fav_teachers[1])))
print("your next two favorite are: " + str(fav_teachers[2] + " and " + str(fav_teachers[3])))
print("your last favorite teacher is: " + str(fav_teachers[-1]))
print("you have a total of "+ str(len(fav_teachers)) + " favorite teachers.")

# remove favorite teacher
fav_teachers.remove(input("\nyouve decided you no longer like a teacher. which teacher would you like to remove?" ).title())

#summary of list
print("your favorite teachers ranked are: " + str(fav_teachers))
print("your favorite teachers listed alphabetically are: " + str(sorted(fav_teachers)))
print("your favorite teachers reverse alphabetically are: "+ str(sorted(fav_teachers, reverse=True)))
print("your top two favorite teachers are: " + str(fav_teachers[0] + " and " + str(fav_teachers[1])))
print("your next two favorite are: " + str(fav_teachers[2] + " and " + str(fav_teachers[3])))
print("your last favorite teacher is: " + str(fav_teachers[-1]))
print("you have a total of "+ str(len(fav_teachers)) + " favorite teachers.")

