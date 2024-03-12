print("Welcome to the tip calculator")
totalBill = float(input("What was the total bill? £"))
tip = int(input("How much tip do you want to give? "))
split = int(input("How many people are splitting the bill? "))
finalTip = totalBill * (tip / 100)
finalBill = finalTip + totalBill
eachPerson = "{:.2f}".format(finalBill / split)
print(f"Each person should pay £{eachPerson}")
