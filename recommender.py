# recommender.py
# @arjunraghunandanan 2024 

# TO DO LIST

# Class Name: LaptopRecommender
# Function Names:
# __init__()
# greet_user()
# query_table()
# show_inventory_summary()
# get_user_budget()
# get_user_use_case()
# get_user_preferences()
# filter_laptops()
# display_lists()
# display_laptop_information()
# check_satisfaction()
# run()

# import needed libraries. # recommender.py
# @arjunraghunandanan 2024
import sqlite3

class LaptopRecommender:
    def __init__(self, db_path):
        self.db_path = db_path
        self.categories = []
        self.manufacturers = []
        self.operating_systems = []
        self.min_price = 0
        self.max_price = 0

    def query_table(self, query, params=None):
        if params is None:
            params = ()
        with sqlite3.connect(self.db_path) as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()

    def greet_user(self):
        print("Welcome to the Laptop Recommender!")
        print("This application will help you find the best laptop based on your preferences.\n")

    def show_inventory_summary(self):
        """
        This function displays a summary of the available laptops in the inventory.
        """
        self.manufacturers = [item[0] for item in self.query_table("SELECT DISTINCT name FROM manufacturers")]
        self.operating_systems = [item[0] for item in self.query_table("SELECT DISTINCT name FROM operating_systems")]
        self.categories = [item[0] for item in self.query_table("SELECT DISTINCT name FROM categories")]
        ram_sizes = [item[0] for item in self.query_table("SELECT DISTINCT ram FROM laptops")]
        # storage_sizes = [item[0] for item in self.query_table("SELECT DISTINCT storage FROM laptops")] # Too Many Options in Storage
        min_max_price = self.query_table("SELECT MIN(price_euros), MAX(price_euros) FROM laptops")[0]
        self.min_price = round(float(min_max_price[0]))
        self.max_price = round(float(min_max_price[1]))

        query = '''
                SELECT manufacturers.name, COUNT(laptops.id) AS total_laptops
                FROM laptops
                JOIN manufacturers ON laptops.manufacturer_id = manufacturers.id
                GROUP BY manufacturers.name
                '''
        result = self.query_table(query)

        print("\nAvailable Laptops in Inventory: \n ")
        for manufacturer, total in result:
            print(f"{manufacturer}: {total} models available")
        print("-" * 30)
        print("\nAvailable Category Values in Inventory: \n ")
        print("Manufacturers : ", self.manufacturers)
        print("OS : ", self.operating_systems)
        print("Category : ", self.categories)
        print("RAM Size : ", ram_sizes)
        print("Price Range", self.min_price, " - ", self.max_price)
        print("-" * 30)

    def get_user_budget(self):
        while True:
            try:
                budget = float(input(f"Please enter your budget (in Euros). Available range: {self.min_price} - {self.max_price} Euros: "))
                if self.min_price <= budget <= self.max_price:
                    return budget
                else:
                    print(f"Budget out of range. Please enter a value between {self.min_price} and {self.max_price}.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")

    def get_user_use_case(self):
        print("Select Your Preferred Laptop Use Case (or enter 0 for No Preference):")
        for idx, category in enumerate(self.categories):
            print(f"{idx + 1}. {category}")
        print("0. No Preference")
        while True:
            try:
                choice = int(input("Enter the number of your choice: ")) - 1
                if choice == -1:
                    return None
                return self.categories[choice]
            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")

    def get_user_preferences(self):
        print("Select Your Preferred Manufacturer (or enter 0 for No Preference):")
        for idx, manufacturer in enumerate(self.manufacturers):
            print(f"{idx + 1}. {manufacturer}")
        print("0. No Preference")
        while True:
            try:
                selected_idx = int(input("Enter the number of your choice: ")) - 1
                if selected_idx == -1:
                    selected_manufacturer = None
                else:
                    selected_manufacturer = self.manufacturers[selected_idx]

                print("Select Your Preferred Operating System (or enter 0 for No Preference):")
                for idx, os in enumerate(self.operating_systems):
                    print(f"{idx + 1}. {os}")
                print("0. No Preference")
                selected_idx = int(input("Enter the number of your choice: ")) - 1
                if selected_idx == -1:
                    selected_os = None
                else:
                    selected_os = self.operating_systems[selected_idx]

                return selected_manufacturer, selected_os

            except (ValueError, IndexError):
                print("Invalid choice. Please enter a valid number.")

    def filter_laptops(self, budget, use_case, manufacturer, os):
        query = '''
        SELECT laptops.id, laptops.model_name, laptops.price_euros
        FROM laptops
        JOIN manufacturers ON laptops.manufacturer_id = manufacturers.id
        JOIN operating_systems ON laptops.operating_system_id = operating_systems.id
        WHERE laptops.price_euros <= ?
        '''
        params = [budget]

        if manufacturer:
            query += ' AND manufacturers.name = ?'
            params.append(manufacturer)
        if os:
            query += ' AND operating_systems.name = ?'
            params.append(os)
        if use_case:
            # Filter by category if use_case is provided
            query += ' AND laptops.category_id = (SELECT id FROM categories WHERE name = ?)'
            params.append(use_case)

        result = self.query_table(query, tuple(params))
        return result


    def display_lists(self, laptops):
        print("\nAvailable Laptops:")
        if laptops:
            for laptop in laptops:
                print(f"ID: {laptop[0]}, Model: {laptop[1]}, Price: {laptop[2]} Euros")
        else:
            print("No laptops found matching your criteria.")
        print("-" * 30)

    def display_laptop_information(self, laptop_id):
        query = '''SELECT manufacturers.name, laptops.model_name, categories.name, laptops.screen_size, 
                        laptops.screen, laptops.cpu, laptops.ram, laptops.storage, laptops.gpu, 
                        operating_systems.name, laptops.weight, laptops.price_euros 
                FROM laptops
                JOIN manufacturers ON laptops.manufacturer_id = manufacturers.id
                JOIN categories ON laptops.category_id = categories.id
                JOIN operating_systems ON laptops.operating_system_id = operating_systems.id
                WHERE laptops.id = ?'''
        
        laptop = self.query_table(query, (laptop_id,))
        
        if laptop:
            laptop = laptop[0]
            print("\nLaptop Details:")
            print(f"Manufacturer: {laptop[0]}")
            print(f"Model Name: {laptop[1]}")
            print(f"Category: {laptop[2]}")
            print(f"Screen Size: {laptop[3]}")
            print(f"Screen: {laptop[4]}")
            print(f"CPU: {laptop[5]}")
            print(f"RAM: {laptop[6]}")
            print(f"Storage: {laptop[7]}")
            print(f"GPU: {laptop[8]}")
            print(f"Operating System: {laptop[9]}")
            print(f"Weight: {laptop[10]}")
            print(f"Price: {laptop[11]} Euros\n")
        else:
            print("No details available for this laptop ID.")


    def check_satisfaction(self, laptops):
        while True:
            satisfaction = input("Are you satisfied with the options? (Yes/No): ").strip().lower()
            if satisfaction == 'yes':
                print("Thank you for using the Laptop Recommender. Have a great day!")
                exit()
            elif satisfaction == 'no':
                print("\nHere are some other laptops you might consider:")
                self.display_lists(laptops)
                # You can implement further similarity logic here
                break
            else:
                print("Invalid response.")

    def run(self):
        self.greet_user()
        self.show_inventory_summary()
        budget = self.get_user_budget()
        use_case = self.get_user_use_case()
        manufacturer, os = self.get_user_preferences()
        laptops = self.filter_laptops(budget, use_case, manufacturer, os)
        
        if laptops:
            self.display_lists(laptops)
            self.check_satisfaction(laptops)

            while True:
                try:
                    laptop_id = int(input("Enter the ID of the laptop you want more details on, or 0 to skip: "))
                    if laptop_id == 0:
                        print("Exiting laptop details view.")
                        break
                    if any(laptop[0] == laptop_id for laptop in laptops):
                        self.display_laptop_information(laptop_id)
                        break
                    else:
                        print("Invalid ID. Please enter a valid laptop ID from the list.")
                except ValueError:
                    print("Invalid input. Please enter a numeric value.")
        else:
            print("No laptops match your preferences.")
            while True:
                proceed = input("Would you like to see all available laptops? (Yes/No): ").strip().lower()
                if proceed == 'yes':
                    all_laptops = self.query_table("SELECT laptops.id, laptops.model_name, laptops.price_euros FROM laptops")
                    self.display_lists(all_laptops)
                    self.check_satisfaction(all_laptops)
                    break
                elif proceed == 'no':
                    print("Thank you for using the Laptop Recommender. Goodbye!")
                    break
                else:
                    print("Invalid response. Please enter 'Yes' or 'No'.")


if __name__ == "__main__":
    recommender = LaptopRecommender('inventory_normalized/normalized_inventory.sqlite')
    recommender.run()