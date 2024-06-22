import sqlite3
#Σε όλη την κλάση έχει συναρτήσεις υπεύθυνες να μιλάνε με τη βάση δεδομένων
class RecipeRepository:
    def __init__(self, db_path):
        self.db_path = db_path

    def get_all_recipes(self):
        recipes = []
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Recipes")
                for row in cursor.fetchall():
                    recipes.append({
                        "Id": row[0],
                        "Name": row[1],
                        "Category": row[2],
                        "Effort": row[3],
                        "Ingredients": row[4]
                    })
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")
        return recipes

    #όταν ο χρήστης κάνει προσθήκη συνταγής και το αποθηκεύσει τότε θα αποθηκευτούν στη βάση δεδομένων
    #το όνομα της συνταγής, η κατηγορία, ο βαθμός δυσκολίας, τα υλικά στης συνταγής και μια λίστα
    #με τα βήματα της συνταγής με σειρά όπως η σειρά που αποθηκεύονται
    def add_recipe(self, name, category, effort, ingredients, steps):
        try:
            conn = sqlite3.connect(self.db_path)
            cursor = conn.cursor()

            # Εισαγωγή στον πίνακα Recipes
            cursor.execute("INSERT INTO Recipes (Name, Category, Effort, Ingredients) VALUES (?, ?, ?, ?)",
                           (name, category, effort, ingredients))
            recipe_id = cursor.lastrowid

            # Εισαγωγή στον πίνακα Steps για κάθε βήμα
            for step in steps:
                cursor.execute(
                    "INSERT INTO Steps (RecipeId, Title, Description, RequiredTimeSeconds, Ingredients) VALUES (?, ?, ?, ?, ?)",
                    (recipe_id, step["Title"], step["Description"], step["RequiredTimeSeconds"],
                     step["Ingredients"]))

            conn.commit()
            conn.close()
            return True, None #Επιστρέφουμε tuple (True, None) σε περίπτωση επιτυχίας
        except Exception as e:
            return False,str(e) #Επιστρεφουμε tuple (False, error message) σε περιπτωση αποτυχίας

    def get_recipe_by_id(self, recipe_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("Select * From Recipes Where Id=?", (recipe_id,))
                recipe = cursor.fetchone()
            return recipe
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def get_steps_by_recipe_id(self, recipe_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("Select Id, Title, Description, RequiredTimeSeconds, Ingredients From Steps Where RecipeId=? Order By Id", (recipe_id,))
                steps = cursor.fetchall()
            return steps
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def get_step_by_recipe_id2(self, step_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("Select Id, Title, Description, RequiredTimeSeconds, Ingredients From Steps Where Id=?", (step_id,))
                step = cursor.fetchone()
            return step
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def get_recipe_steps(self, recipe_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT Title, Description, RequiredTimeSeconds, Ingredients FROM Steps WHERE RecipeId = ? ORDER BY Id", (recipe_id,))
                steps = cursor.fetchall()
            return steps
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def search_recipe_by_name(self, name):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("SELECT * FROM Recipes WHERE Name LIKE ?", ('%' + name + '%',))
                results = cursor.fetchall()
            return results
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def update_recipe(self, recipe_id, name, category, effort, ingredients):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE Recipes
                    SET Name = ?, Category = ?, Effort = ?, Ingredients = ?
                    WHERE ID = ?
                """, (name, category, effort, ingredients, recipe_id))
                connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def update_step(self, step_id, title, description, requiredtime, ingredients):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("""
                    UPDATE Steps
                    SET Title = ?, Description = ?, RequiredTimeSeconds = ?, Ingredients = ?
                    WHERE Id = ?
                """, (title, description, requiredtime, ingredients, step_id))
                connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def delete_recipe(self, recipe_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("Delete From Recipes Where Id=?", (recipe_id,))
                cursor.execute("Delete From Steps Where RecipeId=?", (recipe_id,))
                connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

    def delete_step_recipe(self, step_id):
        try:
            with sqlite3.connect(self.db_path) as connection:
                cursor = connection.cursor()
                cursor.execute("Delete From Steps Where Id=?", (step_id,))
                connection.commit()
        except sqlite3.Error as e:
            print(f"An error occurred: {e}")

