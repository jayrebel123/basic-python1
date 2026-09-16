age = int(input("enter your name: "))
has_id = True
has_banned = False
print("========================")
if age >= 18 and has_id:
    print("your enter allowed ")
if age >= 18 or has_id:
    print("Partial access")

if not has_banned:
    print("your not banned")