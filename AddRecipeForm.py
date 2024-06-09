import tkinter as tk
from tkinter import ttk, messagebox
from RecipeRepository import RecipeRepository  # Εισαγωγή του RecipeRepository
class AddRecipeForm:
    def __init__(self, master):
        self.master = master
        master.title("Προσθήκη Συνταγής")
        master.configure(bg='light green')  # προσθήκη χρώματος
        master.geometry('500x600')  # προσθήκη διαστάσεων

        # Ετικέτα και πεδίο κειμένου για το όνομα της συνταγής
        self.label_recipe_name = tk.Label(master, text="Όνομα Συνταγής:", font=("Arial", 14, "bold"))
        self.label_recipe_name.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.entry_recipe_name = tk.Entry(master)
        self.entry_recipe_name.grid(row=0, column=1, padx=10, pady=10)

        # Ετικέτα και combobox για την κατηγορία
        self.label_category = tk.Label(master, text="Κατηγορία:", font=("Arial", 14, "bold"))
        self.label_category.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.combobox_category = ttk.Combobox(master,
        values=["Σνακ", "Γλυκό", "Ζυμαρικά", "Όσπρια", "Σαλάτες", "Θαλασσινά", "Κρέας"])
        self.combobox_category.grid(row=1, column=1, padx=10, pady=10)

        # Ετικέτα και combobox για το βαθμό δυσκολίας
        self.label_effort = tk.Label(master, text="Δυσκολία:", font=("Arial", 14, "bold"))
        self.label_effort.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.combobox_effort = ttk.Combobox(master, values=["Χαμηλή", "Μέτρια", "Υψηλή"])
        self.combobox_effort.grid(row=2, column=1, padx=10, pady=10)

        # Ετικέτα και πεδίο κειμένου για τα συστατικά
        self.label_recipe_ingredients = tk.Label(master, text="Υλικά:", font=("Arial", 14, "bold"))
        self.label_recipe_ingredients.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.text_recipe_ingredients = tk.Text(master, height=5, width=30)
        self.text_recipe_ingredients.grid(row=3, column=1, padx=10, pady=10)

        # Κουμπί για προσθήκη βήματος
        self.button_add_step = tk.Button(master, text="Προσθήκη Βήματος", bg='yellow', font=("Arial", 14, "bold"),
                                         command=self.open_add_step_form)
        self.button_add_step.grid(row=4, columnspan=2, pady=10)

        # Κουμπί για αποθήκευση της συνταγής
        self.button_save_recipe = tk.Button(master, text="Αποθήκευση Συνταγής", bg='yellow', font=("Arial", 14, "bold"),
                                            command=self.save_recipe)
        self.button_save_recipe.grid(row=5, columnspan=2, pady=10)

        # Λίστα βημάτων της συνταγής κενή
        self.steps_recipe = []

        # Δημιουργία αντικειμένου RecipeRepository
        self.repository = RecipeRepository("RecipeDb.sqlite")

    def open_add_step_form(self):
        from AddStepForm import AddStepForm  # Καθυστερημένη εισαγωγή
        add_step_form = tk.Toplevel(self.master)
        # εντολή να ανοιξει η κλάση AddStepForm
        AddStepForm(add_step_form, self.steps_recipe)
    def save_recipe(self):
        name = self.entry_recipe_name.get()
        category = self.combobox_category.get()
        effort = self.combobox_effort.get()
        ingredients = self.text_recipe_ingredients.get("1.0", tk.END).strip()
        # αμυντικός προγραμματισμός
        if name == "" or category == "" or effort == "":
            messagebox.showerror("Error", "Λείπουν πληροφορίες!")
            return
        success, error_message = self.repository.add_recipe(name, category, effort, ingredients, self.steps_recipe)

        if success:
            messagebox.showinfo("Success", "Recipe Added Successfully!")
            self.clear_fields()
        else:
            messagebox.showerror("Error", error_message)

#όταν ο χρήστης αποθηκεύσει την συνταγή τότε αυτή η συνάρτηση αδειάζει τα πεδία εισαγωγής κειμένου
    def clear_fields(self):
        self.entry_recipe_name.delete(0, tk.END)
        self.combobox_category.set("")
        self.combobox_effort.set("")


