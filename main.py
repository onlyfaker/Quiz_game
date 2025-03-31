from data import question_data
from question_model import Question

question_bank = []

for key in question_data:
    question_bank.append(Question(key["text"],key["answer"]))


    #testing
print(question_bank[3].answer)


