class QuizBrain:

    def __init__(self,q_list):
        self.question_list = q_list
        self.question_number = 0
        self.score = 0

    def still_has_questions(self):
        size = len(self.question_list)
        if self.question_number<size:
            return True
        else:
            return False

    def next_question(self):
        q_num = self.question_number
        current_question = self.question_list[q_num]
        self.question_number+=1
        user_input = input(f"Q.{q_num+1}: {current_question.question}? (True/False): ")
        self.check_answer(user_input, current_question.answer)

    def check_answer(self, user_input, correct_answer):
        if user_input.lower()==correct_answer.lower():
            print(f"You got it!")
            self.score += 1
        else:
            print("Sorry! It is Wrong")

        print(f"The correct answer is {correct_answer}.")
        print(f"Your current score is {self.score}/{self.question_number}")
        print()
