from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for key in question_data:
    question_bank.append(Question(key["text"],key["answer"]))

quiz = QuizBrain(question_bank)


quiz_size = len(question_bank)
score=0
while(quiz_size!=0):#could put while true...

    user_answer = quiz.next_question()
    if(user_answer==quiz[score]["answer])
        if(score+1==len(question_bank)):
        	print(f"Well done passanger, you passed the Test! {score}/{score+1}")
            break
    	else:
        	print(f"good job, score: {score+1}/{score+1}")
    else:
    	print(f"wrong, Final score: {score}/{score+1}")
    score+=1    
    quiz_size-=1#myb a bit usless

# fix the issues