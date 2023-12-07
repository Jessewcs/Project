# Final Project Report

* Student Name: Jesse Wojtanowicz
* Github Username: Jessewcs
* Semester: Fall 2023
* Course: CS5001



## Description
My project, an Inventory Item Manager, is a comprehensive system designed to facilitate the management of stock keeping units (SKUs) in an inventory setting. My motivation behind this project stems from my undergraduate degree, Supply Chain & Information Systems  and my experience as a Procurement & Logistics Analyst at Reliance Steel. I have a lot of knowledge in the logistics of tracking inventory items, and such that I was comfortable with that knowledge to build a simple yet effective tool in python to organize and track inventory items, particularly in small business environments. This specific application caters to basic inventory management needs, allowing users to add, remove, list, and summarize inventory items efficiently and effectively.

## Key Features
I believe this application provides a very clear and user-friendly interface for adding, removing, listing, and summarizing SKUs. This simplicity ensures that users with minimal technical expertise, especially those with small businesses, can effectively and efficiently interact with this system. One pretty neat feature is the ability to summarize SKUs by category. This functions offers the user valuable insights into their inventory stock by category, allowing for quick assessment and decision-making based on category stock levels and what the user might need to purchase in the near future. In addition to summarizing, the user is also able to list each individual SKU ever saved. This allows for great visual representation of what the user had saved in their inventory in the past, numerically in order with information of the SKU category and the quantity in stock. I have also implemented a key function that is essential for managing inventory levels, the ability to remove an individual SKU or perhaps clear their entire inventory file if needed when conducting inventory level measurements and such. By allowing the user the option to remove individual SKUs, they are able to efficiently track inventory item quantities and remove them as their inventory fluctuates and restore them with the appropriate quantity in stock representation. The process of removing inventory items and restoring them immediately is simple and easily accessible for the user.

## Guide
To use this project, the user must simply run the "main" function in the Inventory Manager Application. Upon execution, a menu will be displayed, prompting the user to select from various options. Each option available leads to a different functionality, facilitating an interactive experience for the user.

## Installation Instructions
No external APIs or dependencies are required for this version of the application. Ensure python is installed on your system. The user can then simply clone the repository from GitHub to their computer. This should include inventory_manager.py, inventory_spec.py, and inventory.txt. The text file's purpose is for tracking inventory levels as they fluctuate from being added and removed. The text file might already contain some inventory data which can be useful for testing purposes. Simply run the application and select the remove inventory item option from the prompted menu selection to clear the inventory data. Use the terminal to navigate to the directory. Once you are in the correct directory execute the "python inventory_manager.py" command if you are on windows or "python3 inventory_manager.py" if you are on Mac.
## Code Review

Key aspects of the Inventory Manager Application that I believe are integral parts of the application in order for the program to come together efficiently:
```python
def get_option():
    options = ("1", "2", "3", "4", "5")
    print("--------------------------------------------------------")
    print("--- Inventory Item Manager: Select one of the following:")
    print("1. Add & Save a Stock Keeping Unit (SKU)")
    print("2. Remove an existing Stock Keeping Unit")
    print("3. List all individual Stock Keeping Units")
    print("4. Summarize the quantity of SKUs by Category")
    print("5. Exit the Inventory Manager Application")
    print("--------------------------------------------------------")
    selected_index = input(f"Which option would you like to select? (1 - {len(options)}): ")
    selected_index = selected_index.strip()
    while selected_index not in options:
        selected_index = input(f"Invalid Option: Please enter a valid number! (1 - {len(options)}): ")
        selected_index = selected_index.strip()
    print()
    return selected_index
```
The function, get_option() is what provides the user an interface for selecting an action from a menu. This ensures that the user's input matches one of the valid options before proceeding.

```python
def get_sku():
    while True:
        try:
            sku = input("Enter the Stock Keeping Unit (SKU): ")
            if sku.strip():
                return sku
            else:
                print("Please enter a valid Stock Keeping Unit!", file=sys.stderr)
                print()
        except TypeError:
            print("Invalid Input: Please provide an SKU!", file=sys.stderr)
            print()
```
The function, get_sku() prompts the user for a valid SKU. An invalid input would essentially be no entry, whatsoever. SKUs should be specific and have a unique identifier.

```python
def get_sku_quantity():
    sku = get_sku()
    while True:
        try:
            quantity = int(input(f"Enter the quantity in stock for item, {sku}: "))
            if quantity >= 0:
                return sku, quantity
            else:
                print("Invalid Input: Please provide a non-negative quantity!", file=sys.stderr)
                print()
        except ValueError:
            print("Invalid Input: Please enter a valid number!", file=sys.stderr)
            print()
```
The function, get_ski_quantity() prompts the user for a valid integral value quantity for that specific SKU. 

```python    
def get_sku_category():
    print("----------------------------------")
    print("--- Select an Item (SKU) Category:")
    sku_categories = ["Raw Materials", "Consumer Goods", "Office Supplies", "Equipment", "Miscellaneous"]
    for index, category in enumerate(sku_categories):
        print(f"{index + 1}. {category}")
    print("----------------------------------")

    while True:
        try:
            selected_index = int(input(f"Enter the category where your SKU belongs to (1 - "
                                       f"{len(sku_categories)}): "))
            if 1 <= selected_index <= len(sku_categories):
                selected_category = sku_categories[selected_index - 1]
                return selected_category
            else:
                print("Invalid Input: Please provide a valid category number!", file=sys.stderr)
                print()
        except ValueError:
            print("Invalid Input: Please try again!", file=sys.stderr)
            print()
```
The function, get_sku_category() shows the user all available categories to label their most recent inputted SKU and returns the user's valid category selection. Since the list indices in Python start at 0 and the user is presented with choices starting at 1, we need to adjust for the user's selected category to match the correct index.

```python
def inventory_item_class(sku, category, quantity):
    inventory_item = InventoryItem(sku=sku, category=category, quantity_in_stock=quantity)
    return inventory_item
```
The function, inventory_item_class(sku, category, quantity) creates an instance of a class InventoryItem from the provided sku, category, and quantity so that it can be used to precisely store the data in the inventory file individually.

```python
def write_inventory_to_file(inventory_item: InventoryItem, file_name):
    try:
        with open(file_name, "a") as file:
            inventory_string = f"{inventory_item.sku}, {inventory_item.category}, {inventory_item.quantity_in_stock}"
            file.write(inventory_string)
            file.write("\n")
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while writing to the file: {file_name}", file=sys.stderr)
```
The function, write_inventory_to_file(inventory_item, file_name) takes in an InventoryItem object and adds it into a specified file accordingly to ensure the data will be added to the file, not written over and the information always be neat, concise, and persistent in the file.

```python
def summarize_inventory(file_name):
    inventory_sum = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                dict_parts = line.strip().split(",")
                category = dict_parts[1].strip()
                quantity = int(dict_parts[2].strip())
                if category in inventory_sum:
                    inventory_sum[category] += quantity
                else:
                    inventory_sum[category] = quantity
    except IndexError:
        print("File not specified correctly!", file=sys.stderr)
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while reading the file: {file_name}", file=sys.stderr)
    for key, value in inventory_sum.items():
        print(f"{key}: {value}")
```
The function, summarize_inventory(file_name) summarizes the data inserted to the file previously by category. It reads the file, breaks down each line in the file into individual parts to access the specific part, category name, in each line and then adds it into a dictionary, pairing it with the quantity in stock, and if there are multiple SKUs in the same category, their quantity will be summed.

```python
def clear_inventory(file_name):
    open(file_name, "w").close()
```
The function, clear_inventory(file_name) empties a given text file by opening the file in write mode and then immediately closing. If the file already exists, opening the file in write mode will erase its content. Inventory levels constantly fluctuate, quantities can be wrong, so the user has the option to reset their inventory and restart, usually at the beginning/end of the quarter to determine the exact quantity in stock for specific SKUs and categories.

### Major Challenges
The process of incorporating the option for a user to remove an inventory item was one of my bigger struggles throughout this project. I knew this had to be completed because of how essential it is to be able to remove and update SKUs by their quantity in stock.
```python
def list_skus(file_name):
    sku_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                line_parts = line.strip().split(",")
                sku = line_parts[0].strip()
                category = line_parts[1].strip()
                quantity = line_parts[2].strip()
                sku_list.append((sku, category, quantity))
            return sku_list
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while reading the file: {file_name}", file=sys.stderr)

```
The function, list_skus(file_name) is something I particularly struggled with. I was unable to print the data from the file accordingly, many issues rose from attempting to list, and it was difficult to format it in the way where the user interface looked the simplest. I needed to provide a list of all saved SKUs in order to allow the user to view them via console or terminal and prior to selecting an index, so this was extremely important to me that it worked. I tried incorporating this as a dictionary, but I was unable to successfully do that. Instead, I decided to use a counter as my index and loop through each line in the file, assign each individual part in the line, and append it to sku_list, which is essentially a list of tuples. Each tuple represents a SKU and its associated details category and quantity in stock. This function also proved indeed useful as it allowed me to  give the user an additional option in the menu to simply list all of their individual inventory they've saved.

```python
def get_sku_to_remove(sku_list):
    while True:
        try:
            selected_index = int(input(f"Select the Stock Keeping Unit (SKU) that you wish to remove"
                                       f" (1 - {len(sku_list)}): "))
            if 1 <= selected_index <= len(sku_list):
                sku_to_remove = sku_list[selected_index - 1][0]
                return sku_to_remove
            else:
                print("Invalid Selection: Please try again!", file=sys.stderr)
                print()
        except ValueError:
            print("Invalid Input: Please try again", file=sys.stderr)
            print()
```
The function, get_sku_to_remove(sku_list) facilitates the removal of a specific SKU by letting the user choose from a provided SKU list, which is printed prior to selection. The user will be unable to remove a SKU from an empty inventory. Since the list indices in Python start at 0 and the user is presented with choices starting at 1, we need to adjust for the user's choice to match the correct index in sku_list. We then have to return the selected SKU from the list of tuples. This function is essential to manage inventory levels, and by efficiently providing a list of SKUs to choose from, the user-friendly interface will allow the user to easily select the SKU and permanently remove it.

```python
def remove_sku(sku_to_remove, file_name):
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        with open(file_name, "w") as file:
            for line in lines:
                cleaned_line = line.strip().split(",")
                sku = cleaned_line[0]
                if sku != sku_to_remove:
                    file.write(line)
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while modifying the file: {file_name}", file=sys.stderr)

```
The function, remove_sku(sku_to_remove, file_name) receives the specified valid SKU to remove from the file. We'll first have to open the inventory file and read through all the lines of the file and store them in lines. The function then opens the same file and attempts to write over the original contents of the file. This is particularly useful here because the function will iterate over each line, then split the line into individual parts. Since we know  the SKU is always precisely first in each line, we can use that to compare it with the user's sku_to_remove selection. If the SKU in the current line does not match the user's selected SKU, then the line is written back to the file which is exactly what we want it to do. This will effectively remove the user's selected SKU from the inventory file.

## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
A key feature that I had envisioned from the beginning of developing the Inventory Item Manager, but could not unfortunately implement due to time constraints and the need for much more learning was to be able to integrate some sort of Python Library that provides a GUI for the user. This would allow users to manage this inventory through a visually appealing and user-friendly interface, with buttons they can click such as add, remove, list, summarize, or exit. These features would have probably made my application much more appealing and robust, however, I look forward to revising this project in the future and incorporating such a GUI to significantly enhance the user experience to make it more intuitive and accessible. 

## Final Reflection
Reflecting on my experience in this course, I believe I have learned so many valuable lessons. The intensive curriculum has been instrumental in enhancing my understanding of the Python language and in honing my computational thinking skills. Initially, I struggled with grasping new concepts; I was slow in understanding new topics and hesitant to practice problems on my own. Eventually, I took more time to practice and attempt to solve things on my own. These steps were crucial in solidifying my understanding of the material.

Two key takeaways that I have personally gained from this course is one, the importance of testing your code. The significance needed for thorough testing and considering all possible ege cases has instilled in me the best practices that are vital in real-world software engineering. I am very grateful to be incorporating these habits early into my coding career in order to be successful and confident in the near future. The second key takeaway is the importance of writing clean, simple, yet well-documented code. The emphasis on documentation in this course has shown me how important it is to be able to understand exactly what your code is doing, what task your function has, and a better understanding of how it all comes together at the end.

Moving forwards with future classes, I now fully understand and recognize the necessity to continuously learn and adapt. I must embrace a lifelong learning journey as I will never fully understand each project or assignment that is given to me either by my professors or my superiors. I need to begin to leave my comfort zone, delve deeper in Python and other languages, exploring new libraries and frameworks, and staying persistent with practicing my knowledge and keeping my coding skills sharp. This course has not only equipped me with a very solid foundation of Python programming but it has also sparked an eagerness and excitement to explore beyond Python and what is being taught, and I am more nervous and curious than ever to learn more.