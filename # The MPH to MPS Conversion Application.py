# Challenge 2: The MPH to MPS Conversion Application

print("Welcome to the MPH to MPS Conversion Application")

mph = float(input("\nWhat is your speed in Miles Per Hour?\n"))
# googles conversion suggestion
mps = mph / 2.237
# round to second place
mps = round(mps, 2)



print(f"\nThanks, your speed is {mps} in meters per second.")
