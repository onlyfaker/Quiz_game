from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    question_bank.append(Question(key["text"],key["answer"]))

quiz = QuizBrain(question_bank)
score=0

while quiz.still_has_questions():#could put while true...
    user_answer = quiz.next_question()

print("You have completed the quiz!")
print(f"your final scopre is:{quiz} {len(question_bank)}")