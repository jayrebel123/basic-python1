'''#input 
name = input("Enter your name :")
age  = int(input("enter your age :"))
#print
print(name)
print(age)
#bill slipt 
print("============bill slipt & calcuator ==================")
total = int(input("Enter your bill :"))
per_slipt = int(input("Enter your slipt :"))
num_person = int(input("Enter slipter per person :"))
#arragement
amount = total * (per_slipt / 100)
final = total + amount
cost = final / num_person 

#PRINT
print(f"your amount : {amount:.2f}")
print(f"your final : {final:.2f}")
print(f"your cost : {cost:.2f}")'''

# Day 5: Tip & Bill Splitter Calculator

print("=== Tip and Bill Splitter ===")

# 1. Take user input and convert string types to float/int
total_bill = float(input("Enter total bill amount ($): "))
tip_percent = int(input("Enter tip percentage (e.g., 10, 12, 15): "))
num_people = int(input("How many people are splitting the bill? "))

# 2. Perform math calculations
tip_amount = total_bill * (tip_percent / 100)
final_bill = total_bill + tip_amount
cost_per_person = final_bill / num_people

# 3. Output clean, formatted results using f-strings
print("\n--- Breakdown ---")
print(f"Total Tip: ${tip_amount:.2f}")
print(f"Total Bill (including tip): ${final_bill:.2f}")
print(f"Each person pays: ${cost_per_person:.2f}")
