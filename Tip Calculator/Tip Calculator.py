print("Welcome To the Tip Calculator.")
bill = float(input("What was the total bill? $"))
tipPercent = int(input("What percentage tip would you like to give? 10, 12, 15? "))
finalBill = bill + bill*(tipPercent/100)
people = int(input("How many people to split the bill? "))
tipAmount = finalBill/people
print(f"Each person should pay ${tipAmount}")