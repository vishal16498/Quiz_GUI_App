from tkinter import *
from quiz_logic import QuizLogic
# from tkinter import messagebox
from data import Data

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:
    def __init__(self, quiz_data: QuizLogic, ):    # setting the attribute to QuizBrain data type
        self.quiz = quiz_data
        self.data = Data()
        self.window = Tk()
        self.window.title("Welcome to Trivia Quiz")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.label = Label(text="Score: 0", font=FONT, bg=THEME_COLOR)
        self.label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, text="", fill=THEME_COLOR, font=FONT,
                                                     width=280)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=25)

        self.right_image = PhotoImage(file="./images/true.png")
        self.right_button = Button(image=self.right_image, highlightthickness=0, command=self.right)
        self.right_button.grid(column=0, row=2)

        self.wrong_image = PhotoImage(file="./images/false.png")
        self.wrong_button = Button(image=self.wrong_image, highlightthickness=0, command=self.wrong)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="White")
        if self.quiz.still_has_questions_left():
            self.label.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()      # can access all the methods and attributes from quiz_brain module
            self.canvas.itemconfig(self.question_text, text=q_text)     # changing the canvas text
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached end of Quiz.Thanks for playing")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")
            # self.should_continue()

    # def should_continue(self):
    #     message = messagebox.askyesno(title="Replay",message="Do you want to play another round?")
    #     if message:
    #         # self.quiz.replay()
    #         self.label.config(text=f"Score: {self.quiz.score}")
    #         self.canvas.itemconfig(self.question_text, text=f"Q.{self.quiz.question_number+1}: {self.quiz.current_question.question}")
    #         self.quiz.next_question()

    def right(self):
        self.feedback(self.quiz.check_answer("True"))

    def wrong(self):
        self.feedback(self.quiz.check_answer("False"))

    def feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="Green")
        else:
            self.canvas.config(bg="Red")
        self.window.after(1000, self.get_next_question)
