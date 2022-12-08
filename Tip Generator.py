#Tip Generator

print("Tip Calculator")
print()
print()
total_spent = float(input("How much did you spend?: "))
print()
tip = int(input("What % do you want to tip?: ")) 
print()
people = int(input("How many people in your group?: "))
bill_with_tip = total_spent* tip/100 + total_spent
bill_with_people = bill_with_tip/people
final_amount = round(bill_with_people,2)
print("you each owe $",final_amount)
