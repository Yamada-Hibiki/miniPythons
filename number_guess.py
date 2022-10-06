import random

maximum_number = input("Enter the maximum number of the range: ")

# Check if all the characters in the text are digits
if maximum_number.isdigit():
    maximum_number = int(maximum_number)
    
    if maximum_number <= 0:
        print("Please enter a number greater than or equal to 1")
        quit()

else:
    print("Please enter a number next time")
    quit()

random_number = random.randint(0, maximum_number)
guessed_time = 0

while True:
    guessed_time += 1
    guessed_number = input("So what is the number you guess??: ")
    
    if guessed_number.isdigit():
        guessed_number = int(guessed_number)
    else:
        print("Please enter a number next time")
        continue

    if guessed_number == random_number:
        print("You guessed the correct number!")
        break
    elif guessed_number > random_number:
        print("The correct number is below")
    else:
        print("The correct number is bigger")

# is equal to print("string " + int + " string") add spaces and convert int into string
print("You guessed", guessed_time, "times to find the number")

if guessed_time == 1:
    print("What a lucky shot!")