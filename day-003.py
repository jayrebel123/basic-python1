'''#f
name = "jay"
age  = 398

print(f"your name is {name} : your age is {age:.2f}")


total_bill = float(input("enter your total bill :"))
tip_percent = int(input("enter your tip_percent :"))
num_person = int(input("enter your num person :"))

#
amount_bill = total_bill * (tip_percent / 100)
final_bill = total_bill + tip_percent 
cost_per_person = final_bill / num_person 

#
print(f"your total bill {total_bill:.2f}")
print(f"your final_bill {final_bill:.2f}")
print(f"your cost bill {cost_per_person:.2f}")'''



# Day 3: Tip & Bill Splitter Calculator
print("========= Tip & Bill ==========")
total_bill = float(input("enter your total bill :"))
per_tip = int(input("enter your per tip :"))
num_person = int(input("enter your num person : "))

#assin
amount_bill = total_bill * (per_tip / 100)
final_bill = total_bill + amount_bill
cost_per = final_bill / num_person

#
print(f"your total bill : {amount_bill:.2f}")
print(f"your final bill {final_bill:.2f}")
print(f"your cost bill {cost_per:.2f}")
