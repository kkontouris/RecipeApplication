from tkinter import messagebox, ttk
from ExecuteRecipeForm import *
from EditRecipeForm import EditRecipeForm
from DeleteStepForm import DeleteStepForm
from AddRecipeForm import AddRecipeForm
from RecipeRepository import RecipeRepository

#Κλάση που εμφανίζεται πρώτη μόλις εγκατασταθεί η εφαρμογή
class Dashboard:
    def __init__(self, master):
        self.master = master
        self.master.title("Welcome! Let's cook together!")
        self.master.geometry('1500x800')

        # Δημιουργία καμβά
        self.image = Canvas(self.master, width=1500, height=800)
        self.image.pack()

        # Προσθήκη φόντου στον καμβά
        self.photo_start = PhotoImage(file="photos/συνταγές.gif")
        self.image.create_image(0, 0, anchor=NW, image=self.photo_start)

        # Προσθήκη κειμένου και κουμπιού στον καμβά
        self.text = self.image.create_text(750, 100, text="Καλωσήρθατε! Ελάτε να μαγειρέψουμε παρέα!", fill="light blue",
                         font=("Arial", 50, "bold"), anchor=CENTER)
        #όταν πατήσει είσοδο ο χρήστης καλείται η συνάρτηση open_new_page
        self.register_button = Button(self.master, text="Είσοδος", width=10, height=1, font=("Arial", 18, "bold"),
                                      bg='yellow', command=self.open_new_page)
        self.register_button.place(x=650, y=700)

    #η συνάρτηση καλεί την κλάση RecipePage
    def open_new_page(self):
        new_window = Toplevel(self.master)
        RecipePage(new_window)


class RecipePage:
    def __init__(self, master):
        self.master=master
        self.master.title("New Page")
        self.master.geometry("1500x800")
        self.master.configure(bg='light green')

        # Προσθήκη τίτλου στην κορυφή της σελίδας
        self.create_title()

    def create_title(self):
        # Δημιουργία ετικέτας τίτλου
        self.title_label = tk.Label(self.master, text="Συνταγές Μαγειρικής", font=("Rockwell Extra Bold", 45),
                                    bg='light green')
        # Τοποθέτηση ετικέτας στην κορυφή της σελίδας
        self.title_label.place(x=450, y=20)

        self.repository = RecipeRepository("RecipeDb.sqlite")

        photo1 = PhotoImage(file="photos/makaronia-me-kima.gif")
        image1 = Label(self.master, image=photo1)
        image1.image = photo1
        title_label1 = Label(self.master, text="Μακαρόνια με κιμά", font=("Arial", 18))
        image1.place(x=100, y=100)
        title_label1.place(x=100, y=300)

        photo2 = PhotoImage(file="photos/kalamarakia.gif")
        image2 = Label(self.master, image=photo2)
        image2.image = photo2
        title_label2 = Label(self.master, text="Καλαμαράκια τηγανητά", font=("Arial", 18))
        image2.place(x=600, y=100)
        title_label2.place(x=600, y=300)

        photo3 = PhotoImage(file="photos/laxanika-atmou.gif")
        image3 = Label(self.master, image=photo3)
        image3.image = photo3
        title_label3 = Label(self.master, text="Λαχανικά ατμού", font=("Arial", 18))
        image3.place(x=1000, y=100)
        title_label3.place(x=1000, y=300)

        # Προσθήκη πεδίου αναζήτησης και κουμπιού
        self.search_frame = Frame(self.master)
        self.search_frame.place(x=400, y=380)
        self.search_label = Label(self.search_frame, text="Αναζήτηση Συνταγής:", font=("Arial", 14, "bold"),bg='light green')
        self.search_label.pack(side=LEFT, padx=5)
        self.search_entry = Entry(self.search_frame, font=("Arial", 14))
        self.search_entry.pack(side=LEFT, padx=5)
        self.search_button = Button(self.search_frame, text="Αναζήτηση", command=self.search_recipes,bg='yellow',
                                    font=("Arial", 14, "bold"))
        self.search_button.pack(side=LEFT, padx=5)

        # Προσθήκη του Treeview σε ένα Frame
        self.tree_frame = Frame(self.master)
        self.tree_frame.place(x=200, y=450)

        self.recipe_tree = ttk.Treeview(self.tree_frame, columns=("ID", "Name", "Category", "Effort", "Ingredients"), show="headings")

        self.recipe_tree.heading("ID", text="ID")
        self.recipe_tree.heading("Name", text="Name")
        self.recipe_tree.heading("Category", text="Category")
        self.recipe_tree.heading("Effort", text="Effort")
        self.recipe_tree.heading("Ingredients", text="Ingredients")
        self.recipe_tree.pack(fill="both", expand=True)

        # Εμφάνιση των συνταγών στο Treeview
        self.load_recipes()

        # Προσθήκη του Frame για το κουμπί "Εμφάνιση Βημάτων" και "Εκτέλεση Συνταγής" και "Επεξεργασία Συνταγής"
        button_frame = Frame(self.master)
        button_frame.place(x=300, y=700)

        # Δημιουργία του κουμπιού "Εμφάνιση Βημάτων"
        self.run_recipe_button = Button(button_frame, text="Εκτέλεση Συνταγής",font=("Arial", 12, "bold"),
                                        bg='yellow', command=self.run_recipe)
        self.run_recipe_button.pack(side=LEFT, padx=30)

        # Κουμπί για προσθήκη συνταγής
        self.add_recipe_button = Button(button_frame, text="Προσθήκη Συνταγής",font=("Arial", 12, "bold"),
                                        bg='yellow', command=self.open_add_recipe_form)
        self.add_recipe_button.pack(side=LEFT, padx=30)

        # Κουμπί για "Επεξεργασία Συνταγής"
        self.edit_recipe_button=tk.Button(button_frame, text="Επεξεργασία Συνταγής",
                                      font=("Arial", 12, "bold"), bg="yellow", command=self.run_edit_recipe)
        self.edit_recipe_button.pack(side=RIGHT, padx=30)

        # Κουμπί διαγραφής συνταγής
        self.delete_button = tk.Button(button_frame, text="Διαγραφή Συνταγής", bg='yellow', font=("Arial", 12, "bold"),
                                       command=self.delete_recipe)
        self.delete_button.pack(side=RIGHT, padx=30)

    #συνάρτηση υπεύθυνη για το άνοιγμα της συνάρτησης open_execute_recipe_form(μόλις
    # επιλέξει ο χρήστης εκτέλεση συνταγής)
    def run_recipe(self):
        selected_item=self.recipe_tree.selection()[0]
        recipe_id=self.recipe_tree.item(selected_item,"values")[0]
        self.open_execute_recipe_form(recipe_id)

    #συνάρτηση υπεύθυνη για το άνοιγμα της συνάρτησης open_edit_recipe_form(μόλις επιλέξει
    # ο χρήστης επεξεργασία συνταγής)
    def run_edit_recipe(self):
        #διαλέγει ο χρήστης μια συνταγή και αποθηκεύεται το id της συνταγής
        selected_item = self.recipe_tree.selection()[0]
        recipe_id = self.recipe_tree.item(selected_item, "values")[0]
        self.open_edit_recipe_form(recipe_id)

    #συνάρτηση υπεύθυνη αν επιλέξει ο χρήστης αναζήτηση συνταγης
    def search_recipes(self):
        searched_name=self.search_entry.get()
        recipes=self.repository.search_recipe_by_name(searched_name)
        # Καθαρισμός του Treeview πριν από την εισαγωγή νέων αποτελεσμάτων
        self.recipe_tree.delete(*self.recipe_tree.get_children())
        # Εισαγωγή των αποτελεσμάτων αναζήτησης από τη βάση δεδομένων στο Treeview
        for recipe in recipes:
            self.recipe_tree.insert("", "end", values=(recipe[0], recipe[1], recipe[2], recipe[3], recipe[4]))

    #συνάρτηση που εμφανίζει στο treeview τις συνταγές από τη βάση δεδομένων
    def load_recipes(self):
        for row in self.recipe_tree.get_children():
            self.recipe_tree.delete(row)
        # παίρνω όλες τις συνταγών από τη βάση δεδομένων
        recipes=self.repository.get_all_recipes()
        #εμφανιση των συνταγών στο tree view
        for recipe in recipes:
            self.recipe_tree.insert("", "end", values=(recipe["Id"], recipe["Name"], recipe["Category"], recipe["Effort"], recipe["Ingredients"]))

    #συνάρτηση υπεύθυνη για την προσθήκη συνταγής ανοίγει το αντίστοιχο παράθυρο
    def open_add_recipe_form(self):
        add_recipe_window = tk.Toplevel(self.master)
        add_recipe_form = AddRecipeForm(add_recipe_window)

    #συνάρτηση υπεύθυνη για να ανοίξει τη φόρμα εκτέλεση συγκεκριμένης συνταγής
    def open_execute_recipe_form(self, recipe_id):
        execute_recipe_window=Toplevel(self.master)
        ExecuteRecipeForm(execute_recipe_window,recipe_id,self.repository)

    #συνάρτηση υπεύθυνη για να ανοίξει τη φόρμα επεξεργασία συνταγής
    def open_edit_recipe_form(self, recipe_id):
        edit_recipe_window = Toplevel(self.master)
        EditRecipeForm(edit_recipe_window,recipe_id,self.repository)

    #συνάρτηση υπεύθυνη για την διαγραφή συνταγής ή βημάτων
    def delete_recipe(self):
        selected_item = self.recipe_tree.selection()[0]
        if selected_item:
            recipe_id = self.recipe_tree.item(selected_item, "values")[0]
            answer=messagebox.askyesno("Επιβεβαίωση", "Θέλεις να διαγράψεις όλη τη συνταγή ή μόνο κάποια βήματα;"
                                                  "\n\n Ναι για διαγραφή όλης της συνταγής \nΟχι, θέλω να διαγράψω κάποια βήματα")
            if answer:
                answer2=messagebox.askyesno("Επιβεβαίωση", "Είσαι σίγουρος/η ότι θέλεις να διαγραφεί η συνταγή;")
                if answer2:
                    self.repository.delete_recipe(recipe_id)
                    messagebox.showinfo("Επιτυχία", "Η συνταγή διαγράφηκε επιτυχώς")
            else:
                self.open_delete_step_form(recipe_id)
        else:
            messagebox.showerror("Σφάλμα", "Παρακαλώ επιλέξτε μια συνταγη")

    #Συνάρτηση υπεύθυνη για να ανοίξει τη φόρμα για διαγραφή κάποιου βήματος συνταγής
    def open_delete_step_form(self, recipe_id):
        delete_step_form = tk.Toplevel(self.master)
        DeleteStepForm(delete_step_form, self.repository, recipe_id)



