# age and ticket price
print("================age and ticket ======================")
#user data collect
age = int(input("Enter your age :"))
is_student = input("Are you student ? (yes or no) : ").strip().lower() == "yes"
day = input("Enter your weekday :").strip().lower()

#ticket data coditions
if age <= 0:
    ticket_price = 0
elif age < 12:
    ticket_price = 10
elif age >= 65:
    ticket_price = 30
else:
    ticket_price = 50

#discount
if day == "sunday":
    ticket_price -= 5
    print("Appled: discount 5$ sunday")

#student discount
if is_student and age > 12 and day not in ["monday","friday"]:
    ticket_price -= 2
    print("Appled: student discount 2$ ")


print(f"\n your final ticket price {ticket_price:.2f}")