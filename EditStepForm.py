import tkinter
from tkinter import messagebox
from tkinter import Label, Entry, Text, Button
import tkinter as tk


class EditStepForm:
    def __init__(self, master, step_id, repository):
        self.master= master
        self.step_id=step_id
        self.repository=repository
        self.master.title("Επεξεργασία Βήματος")
        self.master.geometry("500x450")
        self.master.configure(bg='light green')

        self.setup_ui()
        self.load_step()
    def setup_ui(self):
        self.title_window_label = Label(self.master, text="Επεξεργασία Βήματος", width=20, font=("bold", 18), bg='light green')
        self.title_window_label.place(x=75, y=50)

        self.title_label = Label(self.master, text="Τίτλος", font=("bold", 14), bg='light green')
        self.title_label.place(x=50, y=130)
        self.title_entry = Entry(self.master)
        self.title_entry.place(x=200, y=130, width=180)

        self.description_label = Label(self.master, text="Περιγραφή", font=("bold", 14), bg='light green')
        self.description_label.place(x=50, y=180)
        self.description_entry = Entry(self.master)
        self.description_entry.place(x=200, y=180, width=180)

        self.requiredTime_label = Label(self.master, text="Απαιτούμενος Χρόνος",font=("bold", 14), bg='light green')
        self.requiredTime_label.place(x=50, y=230)
        self.requiredTime_entry = Entry(self.master)
        self.requiredTime_entry.place(x=250, y=230, width=180)

        self.ingredients_label = Label(self.master, text="Υλικά",font=("bold", 14), bg='light green')
        self.ingredients_label.place(x=50, y=280)
        self.ingredients_entry = Text(self.master, height=5, width=23)
        self.ingredients_entry.place(x=200, y=280, width=180)

        #Κουμπί για αποθήκευση των αλλαγών στο βήμα
        self.save_edit_step_button=Button(self.master, text='Αποθήκευση Βήματος', height=2, width=23, bg='yellow', font=("bold", 12), command=self.save_step)
        self.save_edit_step_button.place(x=150, y=380)

    #συνάρτηση υπεύθυνη να αποθηκεύσει τις αλλαγές στα βήματα που έκανε ο χρήστης
    def save_step(self):
        title=self.title_entry.get()
        description=self.description_entry.get()
        requiredTime=self.requiredTime_entry.get()
        ingredients=self.ingredients_entry.get("1.0", tk.END).strip()

        if not title or not description or not requiredTime or not ingredients:
            tkinter.messagebox.showerror("Σφάλμα", "Όλα τα πεδιά είναι υποχρεωτικά")
            return

        self.repository.update_step(self.step_id, title, description, requiredTime, ingredients)
        messagebox.showinfo("Επιτυχία", "Η συνταγή ενημερώθηκε επιτυχώς")
        self.master.destroy()

    #φορτώνει τις πληροφορίες από τη βάση δεδομένων στο entry
    def load_step(self):
        try:
            step = self.repository.get_step_by_recipe_id2(self.step_id)
            if not step:
                messagebox.showerror("Error", "Το βήμα δεν βρέθηκε")
                return
            self.title_entry.insert(0, step[1])
            self.description_entry.insert(0, step[2])
            self.requiredTime_entry.insert(0, step[3])
            self.ingredients_entry.insert("1.0", step[4])
        except Exception as e:
            messagebox.showerror("Error", str(e))



