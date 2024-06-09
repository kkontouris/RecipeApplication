import tkinter as tk
from tkinter import ttk, messagebox
from EditStepForm import EditStepForm

class EditRecipeForm:
    def __init__(self, master, recipe_id, repository):
        self.master = master
        self.recipe_id = recipe_id
        self.repository = repository
        self.master.title("Επεξεργασία Συνταγής")
        self.master.geometry("1150x450")
        self.master.configure(bg="light green")

        self.open_edit_recipe_ui()
        self.load_recipe()
        self.load_steps()

    def open_edit_recipe_ui(self):
        # Συνταγή
        # Δεδομένα του ονόματος προς επεξεργασία ρ=της συνταγής που διάλεξε ο χρήστης
        self.name_label = tk.Label(self.master, text="Όνομα:", bg='light green')
        self.name_label.place(x=10, y=10)
        self.name_entry = tk.Entry(self.master)
        self.name_entry.place(x=100, y=10)

        # Δεδομένα της κατηγορίας της συνταγής προς επεξεργασία που διάλεξε ο χρήστης
        self.category_label = tk.Label(self.master, text="Κατηγορία:", bg='light green')
        self.category_label.place(x=10, y=40)
        self.category_entry = tk.Entry(self.master)
        self.category_entry.place(x=100, y=40)

        # ο βαθμός δυσκολίας της συνταγής που διάλεξε ο χρήστης να επεξεργαστεί
        self.effort_label = tk.Label(self.master, text="Βαθμός Δυσκολίας:", bg='light green')
        self.effort_label.place(x=10, y=70)
        self.effort_entry = tk.Entry(self.master)
        self.effort_entry.place(x=120, y=70)

        # τα υλικά της συνταγής που διάλεξε ο χρήστης να επεξεργαστεί
        self.ingredients_label = tk.Label(self.master, text="Υλικά:", bg='light green')
        self.ingredients_label.place(x=10, y=100)
        self.ingredients_entry = tk.Entry(self.master)
        self.ingredients_entry.place(x=80, y=100)

        # Βήματα Συνταγής
        self.steps_frame = tk.LabelFrame(self.master, text="Βήματα Συνταγής")
        self.steps_frame.place(x=300, y=10, width=800, height=400)

        self.steps_tree = ttk.Treeview(self.steps_frame, columns=("Id", "Title", "Description", "RequiredTime", "Ingredients"), show="headings")
        self.steps_tree.heading("Id", text="Id")
        self.steps_tree.heading("Title", text="Τίτλος")
        self.steps_tree.heading("Description", text="Περιγραφή")
        self.steps_tree.heading("RequiredTime", text="Χρόνος")
        self.steps_tree.heading("Ingredients", text="Υλικά")
        self.steps_tree.pack(fill="both", expand=True)

        #Κουμπί για Επεξεργασία Βημάτων
        self.edit_step_button=tk.Button(self.steps_frame,text="Επεξεργασία Βημάτων", command=self.edit_step, bg='yellow')
        self.edit_step_button.pack(pady=5)

        #Κουμπί για αποθήκευση αλλαγών στα βήματα της συνταγής
        self.save_step_button=tk.Button(self.steps_frame,text="Αποθήκευση Συνταγής", command=self.save_recipe, bg='yellow')
        self.save_step_button.pack(pady=5)

    #Φορτώνει τα στοιχεία της συνταγής από τη βάση δεδομένων και τα εισάγει στα αντίστοιχα πεδία εισαγωγής.
    def load_recipe(self):
        recipe=self.repository.get_recipe_by_id(self.recipe_id)
        self.name_entry.insert(0, recipe[1])
        self.category_entry.insert(0,recipe[2])
        self.effort_entry.insert(0,recipe[3])
        self.ingredients_entry.insert(0,recipe[4])

    #συνάρτηση υπεύθυνη για εμφάνιση βημάτων στο treeview
    def load_steps(self):
        steps=self.repository.get_steps_by_recipe_id(self.recipe_id)
        for step in steps:
            self.steps_tree.insert("", "end", values=step)

    #Επεξεργάζεται το επιλεγμένο βήμα από το Treeview.
    def edit_step(self):
        selected_item=self.steps_tree.selection()[0]
        if not selected_item:
            messagebox.showwarning("Προειδοποίηση", "Παρακαλώ επιλέξτε ένα βήμα για την επεξεργασία")
            return
        step_id=self.steps_tree.item(selected_item, "values")[0]
        self.open_step_form(step_id)

    #συνάρτηση υπεύθυνη για άνοιγμα φόρμας επεξεργασίας βημάτων για το επιλεγμένο βήμα
    def open_step_form(self, step_id):
        edit_step_window=tk.Toplevel(self.master)
        EditStepForm(edit_step_window, step_id, self.repository)

    #συνάρτηση υπεύθυνη να κάνει αποθήκευση τις αλλαγες του χρήστη
    def save_recipe(self):
        name=self.name_entry.get()
        category=self.category_entry.get()
        effort=self.effort_entry.get()
        ingredients=self.ingredients_entry.get()

        if not name or not category or not effort or not ingredients:
            tk.messagebox.showerror("Σφάλμα", "Όλα τα πεδία είναι υποχρεωτικά")
            return

        self.repository.update_recipe(self.recipe_id, name, category, effort, ingredients )

        tk.messagebox.showinfo("Επιτυχία", "Η συνταγή και τα βήματα ενημερώθηκαν")
        self.master.destroy()









