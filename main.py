from dataclasses import dataclass
from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
for questions in question_data:
    questions_text = questions['text']
    question_answer = questions['answer']
    new_question = Question(questions_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score is: {quiz.score}/{quiz.question_number}")