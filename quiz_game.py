print("Welcome to this mini Python quiz !!")

answer = input("Would you like to play?: ")
if answer.lower() != "yes":
    print("Ok... maybe next time!")
    quit()

print("Alright let's get it!")
score = 0
correct_answers = 0

answer = input("1st question, What is the most recent version of Python? Enter a number: ")
if answer == "3":
    print("Correct!")
    score += 1
    correct_answers += 1
else:
    print("Wrong answer...")

answer = input("2nd question, In which year Python was released? Enter a number: ")
if answer == "1991":
    print("Correct!")
    score += 1
    correct_answers += 1
else:
    print("Wrong answer...")

answer = input("3rd question, Python can be used for web development, software development, mathematics and system "
               "scripting: ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
    correct_answers += 1
else:
    print("Wrong answer...")

answer = input("4th question, Python is an interpreter system: ")
if answer.lower() == "yes":
    print("Correct!")
    score += 1
    correct_answers += 1
else:
    print("Wrong answer...")

answer = input("This last question is a hard one so you will get 2 points. Press Enter if you are ready: ")
if answer != "":
    print("Apparently you are not ready!")
    quit()

answer = input("Last question, Who created Python? Enter his full name: ")
if answer.lower() == "guido van rossum":
    print("Correct!")
    score += 2
    correct_answers += 1
else:
    print("Wrong answer...")

print("You got " + str(score) + " points in total")
print("Accuracy: " + str((correct_answers / 5) * 100) + "%!")

if score <= 2:
    print("You better know more about Python...")
elif 3 <= score <= 4:
    print("You did pretty good!")
else:
    print("Very good! Keep it going my Python developer")


