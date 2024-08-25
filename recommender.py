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
# run()

# import needed libraries. 

class LaptopRecommender:
    def __init__(self, db_path):
        self.db_path = db_path
        # To be done: Load unique values from database tables

    def query_table(self, query, params=None):
        # To be done: Just a SQLite3 Query Abstraction to call everytime I need to connect to DB. Avoiding multiple connection definition lines. 
        pass

    def greet_user(self):
        # To be done: Welcome User, Provide a basic workflow understanding. 
        pass

    def show_inventory_summary(self):
        # To be done: Query database to get manufacturer names and total laptops per manufacturer
        pass

    def get_user_budget(self):
        # To be done :
        pass

    def get_user_use_case(self):
        # To be done: Retrieve list of use cases from database
        pass

    def get_user_preferences(self):
        # Get user preference 1 by 1 for manufacturer, OS, RAM, Storage. 
        pass

    def filter_laptops(self, budget, use_case, specifications):
        # To be done: Build query to filter laptops based on budget, use case, and specifications
        pass

    def display_lists(self, spec_type, options):
        # To be Done : Show a list of laptops that match the preference. maybe use some Table views. Yet To Decide. 
        pass

    def display_laptop_information(self, laptop_id):
        # To be done: Query database to get details of a specific laptop
        pass

    def run(self):
        self.greet_user()
        self.show_inventory_summary()
        budget = self.get_user_budget()
        use_case = self.get_user_use_case()
        specifications = self.get_user_preferences()
        laptops = self.filter_laptops(budget,use_case,specifications)
        laptop_id = self.display_lists(laptops)
        if laptop_id:
            self.display_laptop_information()

if __name__ == "__main__":
    recommender = LaptopRecommender('inventory_normalized/normalized_inventory.sqlite')
    recommender.run()