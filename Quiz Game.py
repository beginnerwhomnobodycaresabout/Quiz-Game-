ready = str(input("Are You Ready For The Quiz?✨ "))
score = 0
instructions = str(input("Okey So There Will be 5 Questions And 4 options For Each Of Them And The Answers Will be Marked By 1, 2, 3, 4 "))
question1 = int(input("What is the capital of France?\n\n1.Berlin    2.Madrid\n 3.Paris      4. Rome\n"))
if(question1 == 3):
    print("Correct Answer Mate!🎉")
    score += 1
else:
    print("Oops! Not This Time 😊")
question2 = int(input("What is the largest planet in our solar system?\n\n1.Earth    2.Jupiter\n 3.Mars      4. Rome\n "))
if(question2 == 2):
    print("Correct Answer Mate!🎉")
    score += 1
else:
    print("Oops! Not This Time 😊")
question3 = int(input("Which element has the chemical symbol 'O'?\n\n1.Oxygen    2.Hydrogen\n 3.Carbondioxide      4. Heleiuem\n"))
if(question3 == 1):
    print("Correct Answer Mate!🎉")
    score += 1
else:
    print("Oops! Not This Time 😊")
question4 = int(input('Who wrote "To Kill a Mockingbird"\n1.Harpe Lee    2.Me\n 3.J.k Rowling      4. Mark Twain\n'))
if(question4 == 1):
    print("Correct Answer Mate!🎉")
    score += 1
else:
    print("Oops! Not This Time 😊")
question5 = int(input('What is the hardest natural substance on Earth?\n1.Gold     2.Diamond\n 3.Iron     4. Platinum\n'))
if(question5 == 2):
    print("Correct Answer Mate!🎉")
    score += 1
else:
    print("Oops! Not This Time 😊")
print("OMG You Made It Till the End BTW Your Score Is", score)
if(score > 2):
    print("It's Good You Are Above Average ")
else:
    print("Um, Not That Good Study Harder Kid ")