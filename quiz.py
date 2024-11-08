import tkinter as tk
from tkinter import messagebox

class Question:
    def __init__(self, question, options, answer):
        self.question = question
        self.options = options
        self.answer = answer


class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Application")
        self.root.geometry("400x500")
        self.root.config(bg="#f3e5f5")  # Light lavender background for the window

        # List of questions
        self.questions = [
            Question("What is the tallest mountain in the world?", ["K2", "Everest", "Kangchenjunga", "Makalu"], "Everest"),
            Question("What is the main ingredient in guacamole?", ["Tomato", "Potato", "Avocado", "Pepper"], "Avocado"),
            Question("What is the capital of France?", ["Berlin", "Madrid", "Paris", "Lisbon"], "Paris"),
            Question("Which planet is known as the Red Planet?", ["Earth", "Mars", "Jupiter", "Venus"], "Mars"),
            Question("Which element has the chemical symbol 'O'?", ["Osmium", "Oxygen", "Gold", "Lead"], "Oxygen"),
        ]

        self.score = 0
        self.current_question_index = 0

        # Question Progress Label
        self.progress_label = tk.Label(self.root, text="", font=("Arial", 12), bg="#f3e5f5", fg="#6a1b9a")  # Dark purple text
        self.progress_label.pack(pady=10)

        # Question Label
        self.question_label = tk.Label(self.root, text="", wraplength=300, font=("Arial", 16, "bold"), bg="#f3e5f5", fg="#4a148c")  # Darker purple text
        self.question_label.pack(pady=20)

        # Options Frame
        self.var = tk.StringVar()
        self.options_frame = tk.Frame(self.root, bg="#f3e5f5")
        self.options_frame.pack(pady=10)

        # Option Buttons
        self.option_buttons = []
        for i in range(4):
            button = tk.Radiobutton(self.options_frame, text="", variable=self.var, value="", font=("Arial", 14), bg="#f3e5f5", fg="#7b1fa2", activebackground="#d1c4e9", selectcolor="#d1c4e9")  # Lavender tones for options
            button.pack(anchor='w', padx=20, pady=5)
            self.option_buttons.append(button)

        # Submit Button
        self.submit_button = tk.Button(self.root, text="Submit", command=self.submit_answer, font=("Arial", 14), bg="#8e24aa", fg="white", activebackground="#6a1b9a", activeforeground="white")  # Bright purple button
        self.submit_button.pack(pady=20)

        # Load first question
        self.load_question()

    def load_question(self):
        # Update question progress
        self.progress_label.config(text=f"Question {self.current_question_index + 1} of {len(self.questions)}")

        # Load current question and options
        question = self.questions[self.current_question_index]
        self.question_label.config(text=question.question)

        for i, option in enumerate(question.options):
            self.option_buttons[i].config(text=option, value=option)

        self.var.set(None)  # Reset the selected option

    def submit_answer(self):
        selected_answer = self.var.get()
        correct_answer = self.questions[self.current_question_index].answer

        if selected_answer == correct_answer:
            self.score += 1

        self.current_question_index += 1

        if self.current_question_index < len(self.questions):
            self.load_question()
        else:
            self.show_results()

    def show_results(self):
        messagebox.showinfo("Quiz Completed", f"Your score is: {self.score}/{len(self.questions)}")
        self.root.quit()  # Close the application

if __name__ == "__main__":
    root = tk.Tk()
    quiz_app = QuizApp(root)
    root.mainloop()
