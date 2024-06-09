import tkinter as tk
from tkinter import messagebox


class AddStepForm:
    def __init__(self, master, steps_recipe):
        self.master = master
        self.steps_recipe = steps_recipe
        master.title("Προσθήκη Βήματος")
        master.configure(bg='light green')
        master.geometry('500x500')

        # Ετικέτες και πεδία κειμένου για τον τίτλο, την περιγραφή, τον χρόνο και τα συστατικά του βήματος
        self.label_title = tk.Label(master, text="Τίτλος:", font=("Arial", 14, "bold"))
        self.label_title.grid(row=0, column=0, sticky="w", padx=10, pady=10)
        self.entry_title = tk.Entry(master)
        self.entry_title.grid(row=0, column=1, padx=10, pady=10)

        self.label_description = tk.Label(master, text="Περιγραφή :", font=("Arial", 14, "bold"))
        self.label_description.grid(row=1, column=0, sticky="w", padx=10, pady=10)
        self.entry_description = tk.Text(master,height=5,width=30)
        self.entry_description.grid(row=1, column=1, padx=10, pady=10)

        self.label_time = tk.Label(master, text="Χρόνος Εκτέλεσης:", font=("Arial", 14, "bold"))
        self.label_time.grid(row=2, column=0, sticky="w", padx=10, pady=10)
        self.entry_time = tk.Entry(master)
        self.entry_time.grid(row=2, column=1, padx=10, pady=10)

        self.label_ingredients = tk.Label(master, text="Υλικά:", font=("Arial", 14, "bold"))
        self.label_ingredients.grid(row=3, column=0, sticky="w", padx=10, pady=10)
        self.entry_ingredients = tk.Text(master,height=5,width=30)
        self.entry_ingredients.grid(row=3, column=1, padx=10, pady=10)

        # Κουμπί για προσθήκη βήματος
        self.button_add_step = tk.Button(master, text="Προσθήκη Βήματος",bg='yellow',font=("Arial", 14, "bold"), command=self.add_step)
        self.button_add_step.grid(row=4, columnspan=2, pady=10)

        # Κουμπί για κλείσιμο φόρμας
        self.button_close = tk.Button(master, text="Κλείσιμο",bg='yellow',font=("Arial", 14, "bold"), command=self.close_form)
        self.button_close.grid(row=5, columnspan=2, pady=10)

    def close_form(self):
        self.master.destroy()

    def add_step(self):
        title = self.entry_title.get()
        description = self.entry_description.get("1.0", tk.END).strip()
        time = self.entry_time.get()
        ingredients = self.entry_ingredients.get("1.0", tk.END).strip()
        if time == "":
            time = 0  # Ορίζουμε τον χρόνο σε μηδέν αν δεν έχει εισαχθεί τιμή

        # Δοκιμάζουμε να μετατρέψουμε τον χρόνο σε δεκαδικό αριθμό - αμυντικός προγραμματισμός
        try:
            time = float(time)
        except ValueError:
            messagebox.showerror("Error", "Invalid time format. Please enter a valid number.")
            return

        # Δημιουργία ενός νέου βήματος
        step = {
            "Title": title,
            "Description": description,
            "RequiredTimeSeconds": float(time),
            "Ingredients": ingredients
            }
        # Προσθήκη του βήματος στη λίστα βημάτων της συνταγής
        self.steps_recipe.append(step)

        # Κλείσιμο της φόρμας
        self.master.destroy()
