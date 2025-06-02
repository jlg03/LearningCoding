questions = ("How many animals are in the periodic table",
             "Which animal lays the largest eggs",
             "What is the most abundant gas on Earth atmosphere",
             )

options = (("A. 116", "B. 117", "C. 118"),
           ("A. Whale", "B. Crocodile", "C. Ostrich"),
           ("A. Nitrogen", "B. Oxygen", "C. Hydrogen"))
answers = ("C", "D", "A")
guesses = []
score = 0
quest_no = 0

for question in questions:
    print("---------------------")
    print(question)
    for option in options[quest_no]:
        print(option)
    guess = input("Enter guess(A, B, C):").upper()
    guesses.append(guess)
    if guess == answers[quest_no]:
        score += 1
        print("correct")
    else:
        print(f"Answer at {quest_no} is wrong")       
    quest_no += 1

print(f"{score}/3")

print("Answers: ")
for answer in answers:
    print(answer, end=" ")
print()
print("Guesses:")
for guess in guesses:
    print(guess, end=" ")       
