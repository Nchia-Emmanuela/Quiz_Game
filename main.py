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
quiz.next_question()