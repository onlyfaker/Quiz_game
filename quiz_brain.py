
class QuizBrain:

    def __init__(self,q_list):
        print("workk pleasee")
        self.question_list = q_list
        self.question_number=0

    def next_question(self):
        q_num = self.question_number
        question = self.question_list[q_num].question
        input(f"Q.{q_num+1}: {question}? (True/False): ")



