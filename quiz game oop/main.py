from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []
for item in question_data:
    question_n = Question(item["question"], item["correct_answer"])
    question_bank.append(question_n)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("Hurray! You've completed the quiz")
print(f"Your final score is {quiz.score}/{quiz.questionnumber}")

