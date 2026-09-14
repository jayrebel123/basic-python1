'''a = 10
b = 3
print(a//b)
print(a%b)

age = int(input())
next_year_age = age+1
print(next_year_age)


# tipbill
print("=========== tip bill ===============")
total = int(input("enter your total bill:"))
tip = int(input("enter your tip :"))
per_number = int(input("enter your share person :"))

#
amount = total * (tip / 100)
final = total + amount
cost = final / per_number

#
print(f"amount {amount:.2f}")
print(f"final {final :.2f}")
print(f"cost {cost:.2f}")'''

print("======= ticket =========")
heigth = int(input("enter your heigth :"))
if heigth >= 120:
    print("enjoy rider ")
    age = int(input("enter your age :"))
    if age >= 12:
        bill = 5
        print(f"your bill is {bill:.2f}")
    elif age >=15:
        bill1 = 10
        print(f"your bill {bill1:.2f}")
    elif age >= 18:
        bill2 = 15
        print(f"your bill {bill2:.2f}")
    else:
        print("your not eable")

    
