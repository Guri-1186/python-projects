print ("Welcome to the tip calculator!")
bill = float(input("What was the total bill?"))
tip = int(input("How much tip would you like to give? 10, 12 or 15: "))
persons = int(input("How many people to split the bill?"))

tip_amount = (bill * tip)/100
bill_with_tip = bill + tip_amount
amount_per_person = bill_with_tip / persons
final_amount = round(amount_per_person, 2)

print(f"Each person should pay: ${final_amount}")
