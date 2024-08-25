# Product Recommender Python Terminal App
 A basic CLI Product Recommender that uses a CLI conversational approach to narrow down user preferences for buying laptop.

### My Approach to Track Project Status:

| Task | Status |
|---|---|
| Define Basic Idea | Done |
| Set Up Github Repository | Done |
| Brainstorm Ideas into an Introduction File | Done |
| Gather Inventory Data for Recommendation | Done |
| Set Up Inventory | Done |
| Write Main Recommender Code | Done |
| Refactor | Done |
| Tidy Up Github Repo | Done |
| Write a Post About It | Skipped |

## Getting Started : Once Completed
1. Clone this repository.
2. Install the required Python libraries: `pip install -r requirements.txt`
3. Run the script: `python CSVtoNormalizedSQLiteDB.py` to ensure Inventory is populated from `raw_data`
3. Run the script: `python recommender.py`

### Expected User Story Steps:

1. **User opens the application.**
2. **The application greets the user and explains its purpose.**
3. **The application asks the user about their budget.**
4. **The user enters their budget.**
5. **The application asks the user about their preferred laptop use case (e.g., gaming, work, personal).**
6. **The user selects their preferred use case.**
7. **The application asks the user about their preferred laptop specifications.**
8. **The user enters their preferred specifications.**
9. **The application filters the laptop database based on the user's preferences and displays the results.**
10. **The user can refine their search by providing additional criteria.**
11. **The user can select a laptop to view more details.**
12. **The application provides detailed information about the selected laptop.**

### Tech Stack
``` 
Python, SQLite3 
```

###  PHASE 1 : Getting and Cleaning Inventory Data for Use. 

**Laptop Inventory Data**

The script relies on a pre-defined database of laptops to provide recommendations. I've searched and identified a suitable dataset  from @37Degrees containing laptop specifications. 

https://github.com/37Degrees/DataSets/blob/master/laptops.csv

While this dataset is from 5 Years ago, having a structured data like the above would help focus on the application function and less on data clearning. This dataset will be used to populate the application's internal laptop inventory for the recommendation.

The downloaded CSV is inside ```raw_data/``` by the name ```laptops.csv``` folder

###  PHASE 2 : CSV to SQLite Conversion:

The raw CSV data has been converted into a SQLite database for efficient querying and filtering. This should help with performance and querying options of the recommendation script. I created both a normalized DB version and a denormalized DB version. I may only use one for now. 

To Get Denormalized DB, run `[OLD]CSVtoSQLiteDB.py`. This creates `inventory.sqlite` in `inventory/`

To Get Normalized DB, run `CSVtoNormalizedSQLiteDB.py`. This creates `normalized_inventory.sqlite` in `inventory_normalized/`

| Before Conversion | After Conversion |
|---|---|
| ![Image of CSV file](media/CSVBeforeProcessing.png) | ![Image of SQLite database](media/CSVtoSQLiteDB.jpg) |

### PHASE 3 : Program Workflow Design [Expected]

| Task | Desciption| Status |
|---|---|---|
| LaptopRecommender | Class Definition | ✅ | 
| - __init__() | Initialize DB checks, data loading etc | ✅ | 
| - greet_user() | Greets the user |  ✅ | 
| - query_table() | An Abstraction to perform SQL Connections for Query |  ✅ | 
| - show_inventory_summary() |  Show an initial summary of inventory | ✅ | 
| - get_user_budget() | Asks the user for their budget  | ✅ | 
| - get_user_use_case() | Asks the user for their preferred laptop use case. | ✅ | 
| - get_user_preferences() | Prompts for details like preferred manufacturer, operating system, etc. | ✅ | 
| - filter_laptops() | Returns a list of matching laptops | -Minimal-  | 
| - display_lists() | Displays the list of filtered laptops maybe in a table | -Minimal- | 
| - display_laptop_information() | Provides detailed information about the selected laptop | -Minimal- | 
| - run() | Main method to run the CLI | ✅ | 

A Sample Program Run
```
Product-Recommendation-Python-Terminal-App$ python recommender.py 
Welcome to the Laptop Recommender!
This application will help you find the best laptop based on your preferences.

Available Laptops in Inventory: 
Acer: 76 models available
Apple: 8 models available
Asus: 141 models available
Chuwi: 3 models available
Dell: 260 models available
Fujitsu: 3 models available
HP: 258 models available
Huawei: 2 models available
LG: 3 models available
Lenovo: 245 models available
MSI: 54 models available
Mediacom: 7 models available
Microsoft: 6 models available
Razer: 7 models available
Samsung: 7 models available
Toshiba: 48 models available
Vero: 4 models available
Xiaomi: 1 models available
------------------------------

Available Category Values in Inventory: 
 
Manufacturers :  ['Acer', 'Apple', 'Asus', 'Dell', 'Lenovo', 'HP', 'Chuwi', 'MSI', 'Microsoft', 'Toshiba', 'Huawei', 'Vero', 'Razer', 'Mediacom', 'Fujitsu', 'Samsung', 'LG', 'Xiaomi']
OS :  ['Mac OS', 'Windows']
Category :  ['Notebook', 'Ultrabook', 'Netbook', 'Gaming', '2 in 1 Convertible', 'Workstation']
RAM Size :  ['4GB', '16GB', '8GB', '2GB', '12GB', '6GB', '32GB', '24GB', '64GB']
Price Range 192  -  6099
------------------------------
Please enter your budget (in Euros). Available range: 192 - 6099 Euros: 3000
Select Your Preferred Laptop Use Case (or enter 0 for No Preference):
1. Notebook
2. Ultrabook
3. Netbook
4. Gaming
5. 2 in 1 Convertible
6. Workstation
0. No Preference
Enter the number of your choice: 4
Select Your Preferred Manufacturer (or enter 0 for No Preference):
1. Acer
2. Apple
3. Asus
4. Dell
5. Lenovo
6. HP
7. Chuwi
8. MSI
9. Microsoft
10. Toshiba
11. Huawei
12. Vero
13. Razer
14. Mediacom
15. Fujitsu
16. Samsung
17. LG
18. Xiaomi
0. No Preference
Enter the number of your choice: 0
Select Your Preferred Operating System (or enter 0 for No Preference):
1. Mac OS
2. Windows
0. No Preference
Enter the number of your choice: 2

Available Laptops:
ID: 94, Model: GS63VR 7RG, Price: 2241.5 Euros
ID: 107, Model: FX753VD-GC086T (i5-7300HQ/8GB/1TB, Price: 938.0 Euros
ID: 116, Model: GE72MVR 7RG, Price: 2029.0 Euros
ID: 118, Model: Inspiron 5577, Price: 1249.26 Euros
ID: 1096, Model: GE62 Apache, Price: 1229.0 Euros
------------------------------
Are you satisfied with the options? (Yes/No): No

Here are some other laptops you might consider:

Available Laptops:
ID: 9, Model: Legion Y520-15IKBN, Price: 999.0 Euros
ID: 1096, Model: GE62 Apache, Price: 1229.0 Euros
---etc----
Enter the ID of the laptop you want more details on, or 0 to skip: 966

Laptop Details:
Manufacturer: Asus
Model Name: Rog GL552VW-CN470T
Category: Gaming
Screen Size: 15.6"
Screen: IPS Panel Full HD 1920x1080
CPU: Intel Core i7 6700HQ 2.6GHz
RAM: 16GB
Storage: 128GB SSD +  1TB HDD
GPU: Nvidia GeForce GTX 960M
Operating System: Windows
Weight: 2.59kg
Price: 1339.0 Euros
```

This is just a simple project to practice basic CLI programs hence may not be improved further for now. 

### Contributing:
Feel free to contribute to this project / use the in a part of your program etc if neeeded. 
Use code with caution.
