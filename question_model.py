from data import QUESTION_DATA
class Question:

    def __init__(self):
        self.text = QUESTION_DATA[0]["text"]
        self.answer = QUESTION_DATA[0]["answer"]

#testing
q1=Question()
print(q1.text,q1.answer)