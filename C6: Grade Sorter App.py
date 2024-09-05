print("Welcome to the Grade Sorter App")

# initialize list, get user input
grades = []
grade = int(input("\nwhat is your first grade? "))
grades.append(grade)
grade = int(input("what is your second grade? "))
grades.append(grade)
grade = int(input("what is your third grade? "))
grades.append(grade)
grade = int(input("what is your fourth grade? "))
grades.append(grade)

print("\nyour grade are: " + str(grades))

# sort the list from high to low
grades.sort(reverse=True)
print("\nyour grades from high to low: " + str(grades))

print("The two lowest grades will be now dropped")
removed_grade = grades.pop()
print("removed grade " + str(removed_grade))
removed_grade = grades.pop()
print("removed grade " + str(removed_grade))

#recap remaining grades
print("\nyour remaining grades are: " + str(grades))
print("nice work, your highest grade is " + str(grades[0]) + ".")
