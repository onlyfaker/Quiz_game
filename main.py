from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    question_bank.append(Question(key["text"],key["answer"]))

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    user_answer = quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is: {quiz.score} /{len(question_bank)}")
# add new questions from OPEN TRIVIA DB