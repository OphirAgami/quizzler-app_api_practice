from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class QuizInterFace:
    def __init__(self,quiz: QuizBrain):
        self.quiz = quiz
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)
        #Canvas
        self.canvas = Canvas(width=300,height=250)
        self.canvas.grid(column=0,row=1,columnspan=2,pady=50)
        self.question_next = self.canvas.create_text(
            150,
            125,
            width=250,
            text="Some question text",
            fill=THEME_COLOR,
            font = ("ariel", 20, "italic"))
        #Lable
        self.label_score = Label(text="Score: 0",fg="white",bg=THEME_COLOR,font=("ariel",20,"bold"))
        self.label_score.grid(column=1,row=0)

        #Vi Button
        vi_button_image = PhotoImage(file="images/true.png")
        self.vi_button = Button(image=vi_button_image,highlightthickness=0,command=self.true_pressed)
        self.vi_button.grid(column=0,row=2)
        #Nope Button
        nope_button_image = PhotoImage(file="images/false.png")
        self.nope_button = Button(image=nope_button_image,highlightthickness=0,command=self.false_pressed)
        self.nope_button.grid(column=1,row=2)
        self.next_question()
        self.window.mainloop()

    def next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.label_score.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_next,text=q_text)
        else:
            self.canvas.itemconfig(self.question_next,text="The End")
            self.vi_button.config(state="disabled")
            self.nope_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("True")
        self.give_feedback(is_right)

    def false_pressed(self) :
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000,self.next_question)







