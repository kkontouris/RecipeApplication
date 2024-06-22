import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class DeleteStepForm:
    def __init__(self, master, repository, recipe_id):
        self.master= master
        self.repository= repository
        self.recipe_id= recipe_id
        self.master.title("Διαγραφή Βήματος")
        self.master.geometry("1150x450")
        self.master.configure(bg="light green")

        # Βήματα Συνταγής
        self.steps_frame = tk.LabelFrame(self.master, text="Βήματα Συνταγής")
        self.steps_frame.place(x=300, y=10, width=800, height=400)

        #Treeview
        self.steps_tree = ttk.Treeview(self.steps_frame,
                                       columns=("Id", "Title", "Description", "RequiredTime", "Ingredients"),
                                       show="headings")
        self.steps_tree.heading("Id", text="Id")
        self.steps_tree.heading("Title", text="Τίτλος")
        self.steps_tree.heading("Description", text="Περιγραφή")
        self.steps_tree.heading("RequiredTime", text="Χρόνος")
        self.steps_tree.heading("Ingredients", text="Υλικά")
        self.steps_tree.pack(fill=tk.BOTH, expand=True)

        self.load_steps()

        self.delete_step_button = tk.Button(master, text="Διαγραφή Βήματος", bg='red', font=("Arial", 14, "bold"),
                                            command=self.delete_step)
        self.delete_step_button.place(x=580, y=350)

    #συνάρτηση υπεύθυνη για να εμφανίσει τα βήματα προς διαγραφή στο treeview
    def load_steps(self):
            #λιστα με τα βήματα
            for step in self.repository.get_steps_by_recipe_id(self.recipe_id):
                self.steps_tree.insert("", "end", values=step)

    #συνάρτηση υπεύθυνη που ανοίγει το παράθυρο για να ρωτήσει το χρήστη αν είναι
    # σίγουρος και αν απαντήσει ναι κάνει τη διαγραφή από τη βάση δεδομένων
    def delete_step(self):
        selected_step=self.steps_tree.selection()[0]
        if selected_step:
            step_id=self.steps_tree.item(selected_step, "values")[0]
            answer = messagebox.askyesno("Επιβεβαίωση", "Είσαι σίγουρος ότι θέλεις να διαγράψεις αυτό το βήμα;")
            if answer:
                self.repository.delete_step_recipe(step_id)
                messagebox.showinfo("Επιβεβαίωση", "Το βήμα που επιλέξατε διαγραφηκε με επιτυχία")
        else:
            messagebox.showwarning("Προειδοποίηση", "Παρακαλώ επιλέξτε ένα βήμα για την επεξεργασία")
            return
