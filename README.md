# Python Quiz Game

A command-line trivia quiz game built in Python using Object-Oriented Programming principles. This application presents users with true/false questions, evaluates answers, and tracks scores.

## 📝 Overview

This Python Quiz Game displays trivia questions to users who must answer with "True" or "False". The game tracks correct answers, provides immediate feedback, and displays the final score upon completion.

## ✨ Features

- True/False question format
- Score tracking during gameplay
- Question counter
- Interactive command-line interface
- Immediate feedback on answers
- Final score report

## 🏗️ Project Structure

The project follows object-oriented design with three main classes:

```
python-quiz-game/
├── main.py           # Entry point and game execution
├── data.py           # Question data storage
├── question_model.py # Question class definition
├── quiz_brain.py     # Quiz logic implementation
└── README.md         # Project documentation
```

## 🧩 Components

### Question Model (`question_model.py`)
- Defines the `Question` class
- Stores question text and correct answer

### Quiz Brain (`quiz_brain.py`)
- Manages quiz functionality
- Tracks question number and score
- Presents questions and evaluates answers
- Provides feedback on user responses

### Data (`data.py`)
- Contains the question bank as a list of dictionaries
- Each question has "text" and "answer" keys

### Main (`main.py`)
- Creates question objects from data
- Initializes the quiz
- Runs the quiz loop
- Displays final results

## 🚀 How to Run

1. Clone the repository:
```bash
git clone https://github.com/yourusername/python-quiz-game.git
cd python-quiz-game
```

2. Run the quiz:
```bash
python main.py
```

3. Answer the questions by typing "True" or "False" (case-insensitive)

## 📋 Gameplay

1. A question is presented with its number
2. User inputs "True" or "False"
3. Feedback is provided on answer correctness
4. Current score is displayed
5. Next question is presented
6. Upon completion, final score is displayed

Example interaction:
```
Q.1: A slug's blood is green? (True/False): True
You got it!
The correct answer is True.
Your current score is 1/1

Q.2: The loudest animal is the African Elephant? (True/False): True
Sorry! It is Wrong
The correct answer is False.
Your current score is 1/2

...

You have completed the quiz!
Your final score is: 8/12
```

## 💻 Technical Implementation

### Question Bank Creation
```python
question_bank = []
for key in question_data:
    question_bank.append(Question(key["text"], key["answer"]))
```

### Quiz Logic
The quiz runs while there are still questions remaining:
```python
while quiz.still_has_questions():
    user_answer = quiz.next_question()
```

### Answer Checking
```python
def check_answer(self, user_input, correct_answer):
    if user_input.lower() == correct_answer.lower():
        print(f"You got it!")
        self.score += 1
    else:
        print("Sorry! It is Wrong")
```

## 🔧 Customization

### Adding New Questions
To add more questions, modify the `question_data` list in `data.py`:
```python
question_data = [
    {"text": "Your question here", "answer": "True/False"},
    # Add more questions here
]
```

### Using Open Trivia DB
As noted in the code comment, you can integrate with the Open Trivia Database API to source additional questions.

## 🛠️ Future Improvements

- Add multiple-choice questions
- Implement difficulty levels
- Add timer functionality
- Create categories for questions
- Save high scores
- Implement a GUI version
- Add support for fetching questions from Open Trivia DB API

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
