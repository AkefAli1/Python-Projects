class QuizBrain:
    def __init__(self, q_list):
        self.questionnumber = 0
        self.questionlist = q_list
        self.score = 0

    def still_has_questions(self):
        if self.questionnumber < len(self.questionlist):
            return True
        else:
            return False

    def next_question(self):
        current_question = self.questionlist[self.questionnumber]
        self.questionnumber += 1
        user_answer = input(f"Q.{self.questionnumber}: {current_question.text}.(True/False)?: ")
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right")
            self.score += 1
        else:
            print("You are wrong")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is {self.score}/{self.questionnumber}")
        print("\n")






