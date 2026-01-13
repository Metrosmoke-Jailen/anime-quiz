score = 0  

print("🎌 Welcome to the Anime Quiz Game! 🎌")
print("Answer by typing A, B, C, or D.\n")

print("1) Who is the main character of Naruto?")
print("A) Sasuke")
print("B) Naruto")
print("C) Kakashi")
print("D) Itachi")

answer = input("Your answer: ").upper()

if answer == "B":
    print("Correct! 🎉\n")
    score = score + 1 
else:
    print("Wrong! The correct answer is B.\n")

# Question 2
print("2) What anime features the Survey Corps?")
print("A) One Piece")
print("B) Demon Slayer")
print("C) Attack on Titan")
print("D) Bleach")

user_answer = input("Your answer: ").upper()

if user_answer == "C":
    print("Correct! 🎉\n")
    score = score + 1
else:
    print("Wrong! The correct answer is C.\n")

print("3) Who uses a sword called Zangetsu?")
print("A) Luffy")
print("B) Goku")
print("C) Ichigo")
print("D) Tanjiro")

answer = input("Your answer: ").upper()

if answer == "C":
    print("Correct! 🎉\n")
    score = score + 1
else:
    print("Wrong! The correct answer is C.\n")

print("🏁 Quiz Finished!")
total_questions = 3
print(f"Your final score: {score}/{total_questions}")

if score == 3:
    print("🔥 Anime Master!")
elif score == 2:
    print("😄 Great job!")
elif score == 1:
    print("🙂 Not bad, keep watching anime!")
else:
    print("😅 Time for an anime marathon!")