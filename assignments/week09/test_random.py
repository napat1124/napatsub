import random

test_random = random.randiant(0,10)

guess_number = int(input("What is your guess number?: "))

if test_random == guess_number:
    print("เจ๋งแจ๋ว")

if guess_number < test_random:
    print("มั่ว เพิ่มอีก")

elif guess_number > test_random:
    print("มั่ว น้อยลงหน่อย")
    