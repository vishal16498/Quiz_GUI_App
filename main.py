from data import Data
from quiz_logic import QuizLogic
from quiz_ui import QuizInterface

question_data = Data()
# question_data_list = question_data.questions()
# question_bank = []
#
# for question in question_data_list:
#     question_text = question["question"]
#     question_answer = question["correct_answer"]
#     new_question = Question(question_text, question_answer)
#     question_bank.append(new_question)

quiz = QuizLogic(question_data.questions())
quiz_gui = QuizInterface(quiz)


