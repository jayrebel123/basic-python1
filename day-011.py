#number guess game 
print("======game guess number =========")
print("========== you can guess 1 to 100 ===================")
import random
secret_number = random.randint(1,100)
attempts = 0
guess_correctly = False

#while
while not guess_correctly:
    guess = int(input("take your guess :"))
    attempts +=1

    if guess < secret_number:
        print("Try again : try higher :")
    elif guess > secret_number:
        print("Try again : try lower :")
    else:
        guess_correctly = True
        print(f"\n conguralutations : you attempts is {attempts}")