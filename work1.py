import random

class Quiz:
    def __init__(self):
        self.questions = [ ]
        self.score = 0

    def load_questions(self):
        file = open("questions.txt", "r")
        for line in file:
            line = line.strip()
            if line != "":
                parts = line.split(" | ")
                self.questions.append(parts)
        file.close()

    def start_quiz(self):
        selected_questions = random.sample(self.questions, 5)

        for q in selected_questions:
            print("\n" + q[0])
            print("A:", q[1])
            print("B:", q[2])

            answer = input("Your answer: ")

            if answer.lower() == q[3].lower():
                self.score += 1

        print("\nYour Score:", self.score)
        self.save_high_score()

    def save_high_score(self):
        try:
            file = open("leaderboard.txt", "r")
            high_score = int(file.read())
            file.close()
        except:
            high_score = 0

        if self.score > high_score:
            file = open("leaderboard.txt", "w")
            file.write(str(self.score))
            file.close()
            print("New High Score Saved!")
        else:
            print("High Score:", high_score)


quiz = Quiz()
quiz.load_questions()
quiz.start_quiz()