from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)

        # Label
        self.score_label = Label(text=f"Score : 0", fg="white", bg=THEME_COLOR)
        self.score_label.grid(row=0, column=1)

        # Canvas
        self.canvas = Canvas(height=250, width=300, bg="White")
        self.question_text = self.canvas.create_text(150, 125, text=f"Hello",
                                                     font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        check_img = PhotoImage(file="./images/true.png")
        cross_img = PhotoImage(file="./images/false.png")

        # Buttons
        self.check_button = Button(image=check_img, highlightthickness=0, command=self.true_answer)
        self.check_button.grid(row=2, column=0)

        self.cross_button = Button(image=cross_img, highlightthickness=0, command=self.false_answer)
        self.cross_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score : {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_answer(self):
        self.give_feedback(self.quiz.check_answer(user_answer="True"))
    #     The code above is the same as the one below, just different syntax.

    def false_answer(self):
        is_right = self.quiz.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            color = "green"
        else:
            color = "red"
        self.canvas.config(bg=color)
        self.window.after(1000, self.get_next_question)

