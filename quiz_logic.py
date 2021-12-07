import html
# from data import Data


class QuizLogic:
    def __init__(self, question_list):
        self.question_list = question_list
        self.question_number = 0
        self.score = 0
        # self.current_question = None
        self.current_question = self.question_list[self.question_number]

    def still_has_questions_left(self):
        return self.question_number < len(self.question_list)

    def next_question(self):
        if self.still_has_questions_left():
            self.current_question = self.question_list[self.question_number]
            self.question_number += 1
            question_from_list = html.unescape(self.current_question.question)   # recently added using API database to correct html entities
            return f"Q.{self.question_number}: {question_from_list}"
        # user_answer = input(f"Q.{self.question_number}: {question_from_list} (True/False): ")
        # self.check_answer(user_answer, current_question.correct_answer)

    def check_answer(self, user_answer):
        answer = self.current_question.correct_answer
        if user_answer == answer:
            self.score += 1
            return True
        else:
            return False

    # def replay(self):
    #     new_list = Data()
    #     self.question_list = new_list.questions
    #     print(type(self.question_list))
    #     self.score = 0
    #     self.question_number = 0
    #     self.current_question = self.question_list[self.question_number]
