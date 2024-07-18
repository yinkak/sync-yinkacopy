import random
randomnumber = random.randint(1,100)
print(randomnumber) #remove this line, used only for testing purposes
input_int = int(input("enter your guess between 1 and 100: "))

if input_int < randomnumber:
        print("too low")
elif input_int > randomnumber:
    print("too high")
elif input_int == randomnumber:
    print("you got it!")

while input_int != randomnumber:
    guess_input = input("enter your guess between 1 and 100: ")
    input_int = int(guess_input)
    if input_int < randomnumber:
        print("too low")
    elif input_int > randomnumber:
        print("too high")
    elif input_int == randomnumber:
        print("you got it!")
        


    