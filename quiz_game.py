import tkinter as tk
from tkinter import messagebox
import random

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.root.geometry("400x300")
        self.root.configure(bg="#f0f0f0")
        self.current_question_index = 0
        self.score = 0
        self.questions = self.load_questions()

        self.title_label = tk.Label(root, text="Quiz Game", font=("Helvetica", 18, "bold"), bg="#f0f0f0")
        self.title_label.pack(pady=10)

        self.question_label = tk.Label(root, text="", font=("Helvetica", 14), bg="#f0f0f0", wraplength=350)
        self.question_label.pack(pady=10)

        self.choices_frame = tk.Frame(root, bg="#f0f0f0")
        self.choices_frame.pack(pady=10)

        self.input_frame = tk.Frame(root, bg="#f0f0f0")
        self.input_frame.pack(pady=10)

        self.answer_entry = tk.Entry(self.input_frame, width=30)
        self.answer_entry.pack(pady=2)
        self.answer_entry.bind("<Return>", self.check_fill_in_blank)

        self.next_button = tk.Button(root, text="Next", command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=10)

        self.display_question()

    def load_questions(self):
        return [
            {
                'type': 'mc',
                'question': 'What is the capital of France?',
                'choices': ['A. Paris', 'B. Berlin', 'C. Madrid', 'D. Rome'],
                'answer': 'A'
            },
            {
                'type': 'mc',
                'question': 'What is 2 + 2?',
                'choices': ['A. 3', 'B. 4', 'C. 5', 'D. 6'],
                'answer': 'B'
            },
            {
                'type': 'mc',
                'question': 'Which planet is known as the Red Planet?',
                'choices': ['A. Earth', 'B. Mars', 'C. Jupiter', 'D. Saturn'],
                'answer': 'B'
            },
            {
                'type': 'mc',
                'question': 'Who wrote "To Kill a Mockingbird"?',
                'choices': ['A. Harper Lee', 'B. Mark Twain', 'C. J.K. Rowling', 'D. Ernest Hemingway'],
                'answer': 'A'
            },
            {
                'type': 'mc',
                'question': 'What is the largest ocean on Earth?',
                'choices': ['A. Atlantic Ocean', 'B. Indian Ocean', 'C. Arctic Ocean', 'D. Pacific Ocean'],
                'answer': 'D'
            },
            {
                'type': 'fill',
                'question': 'The largest mammal is the _____.',
                'answer': 'blue whale'
            },
            {
                'type': 'fill',
                'question': 'The chemical symbol for gold is _____.',
                'answer': 'Au'
            }
        ]

    def display_question(self):
        q = self.questions[self.current_question_index]
        self.choices_frame.pack_forget()
        self.input_frame.pack_forget()

        self.question_label.config(text=q['question'])
        
        if q['type'] == 'mc':
            self.display_multiple_choice()
        elif q['type'] == 'fill':
            self.display_fill_in_blank()

    def display_multiple_choice(self):
        self.choices_frame.pack(pady=10)
        
        for widget in self.choices_frame.winfo_children():
            widget.destroy()

        q = self.questions[self.current_question_index]
        for choice in q['choices']:
            btn = tk.Button(self.choices_frame, text=choice, width=30, command=lambda c=choice: self.check_answer(c))
            btn.pack(pady=2)
        
        self.next_button.config(state=tk.DISABLED)

    def display_fill_in_blank(self):
        self.input_frame.pack(pady=10)
        self.answer_entry.delete(0, tk.END)
        self.next_button.config(state=tk.NORMAL)

    def check_answer(self, selected_choice):
        q = self.questions[self.current_question_index]
        correct_answer = q['answer']
        if selected_choice.startswith(correct_answer):
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer was {correct_answer}.")
        self.next_button.config(state=tk.NORMAL)

    def check_fill_in_blank(self, event):
        q = self.questions[self.current_question_index]
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = q['answer'].lower()
        
        if user_answer == correct_answer:
            self.score += 1
            messagebox.showinfo("Result", "Correct!")
        else:
            messagebox.showinfo("Result", f"Incorrect. The correct answer was {correct_answer}.")
        
        self.next_button.config(state=tk.NORMAL)

    def next_question(self):
        self.current_question_index += 1
        if self.current_question_index >= len(self.questions):
            self.display_results()
        else:
            self.display_question()

    def display_results(self):
        result_message = f"Quiz Over! Your final score is {self.score}/{len(self.questions)}."
        if self.score == len(self.questions):
            result_message += "\nExcellent! You got all the questions right!"
        elif self.score >= len(self.questions) / 2:
            result_message += "\nGood job! You got more than half right."
        else:
            result_message += "\nKeep trying! Better luck next time."
        
        messagebox.showinfo("Final Results", result_message)
        
        play_again = messagebox.askyesno("Play Again", "Do you want to play again?")
        if play_again:
            self.current_question_index = 0
            self.score = 0
            random.shuffle(self.questions)
            self.display_question()
        else:
            self.root.quit()

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()
