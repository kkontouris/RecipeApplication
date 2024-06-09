import tkinter as tk
from tkinter import *
from tkinter import messagebox

class ExecuteRecipeForm:
    def __init__(self, master, recipe_id, repository):
        self.master = master
        self.master.title("Εκτέλεση Συνταγής")
        self.master.geometry("600x300")
        self.master.configure(bg='light green')

        self.recipe_id=recipe_id
        self.current_step_index=0
        self.repository=repository

        self.recipe_steps=self.repository.get_recipe_steps(self.recipe_id)

        if not self.recipe_steps:
            messagebox.showerror("Σφάλμα", "Δεν βρέθηκαν βήματα για αυτή τη συνταγή.")
            self.master.destroy()
            return

        # Ετικέτα για την εμφάνιση του τρέχοντος βήματος
        self.step_text = StringVar()
        self.step_label = Label(self.master, textvariable=self.step_text, wraplength=580, justify="left", font = ("Arial",14))
        self.step_label.pack(pady=20)

        # Κουμπί "Επόμενο"
        self.next_button = Button(self.master, text="Επόμενο", bg ='yellow', font = ("Arial",14), command=self.show_next_step)
        self.next_button.pack()
        # Κουμπί για την κλείσιμο της φόρμας
        self.close_button = Button(self.master, text="Κλείσιμο", bg= 'yellow', font = ("Arial",14), command=self.master.destroy)
        self.close_button.pack()

        # Εμφάνιση του πρώτου βήματος κατά την αρχικοποίηση της φόρμας
        self.show_step()

    #Εμφανίζει το τρέχον βήμα της συνταγής στο GUI.
    #Υπολογίζει και εμφανίζει το ποσοστό ολοκλήρωσης και τον απαιτούμενο χρόνο για το τρέχον βήμα.
    def show_step(self):
            if self.current_step_index < len(self.recipe_steps):
                step = self.recipe_steps[self.current_step_index]
                title, description,requiredtime, ingredients = step
                elapsed_time = sum(step[2] for step in self.recipe_steps[:self.current_step_index])
                total_time = sum(step[2] for step in self.recipe_steps)
                completion_percentage = (elapsed_time / total_time) * 100
                time=requiredtime
                self.step_text.set(f"Βήμα {self.current_step_index+1}:\n Τίτλος:{title}\n\nΠεριγραφή:{description}\nΧρόνος Εκτέλεσης(λεπτά):{time}\nΣυστατικά:{ingredients}\nΠοσοστό Ολοκλήρωσης(%){completion_percentage:.2f}%")
            else:
                self.step_text.set("Δεν υπάρχουν άλλα βήματα.")
                self.next_button.config(state="disabled")

    #Αυξάνει τον δείκτη του τρέχοντος βήματος και καλεί τη show_step για να εμφανίσει το επόμενο βήμα.
    def show_next_step(self):
            self.current_step_index += 1
            self.show_step()

