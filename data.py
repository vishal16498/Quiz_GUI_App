import requests
from question_model import Question


class Data:
    def __init__(self):
        self.parameters = {
            "amount": 10,
            "type": "boolean"
        }

    def questions(self):
        questions = requests.get(url="https://opentdb.com/api.php", params=self.parameters)
        question_dict = questions.json()["results"]
        question_bank = []

        for question in question_dict:
            question_text = question["question"]
            question_answer = question["correct_answer"]
            new_question = Question(question_text, question_answer)
            question_bank.append(new_question)
        return question_bank
# print(question_data)
