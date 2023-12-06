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

`def get_option():
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
    return selected_index`

This function, get_option() is what provides the user an interface for selecting an action from a menu. This ensures that the user's input matches one of the valid options before proceeding.

    
`def get_sku_category():
    print("----------------------------------")
    print("--- Select an Item (SKU) Category:")
    sku_categories = ["Raw Materials", "Consumer Goods", "Office Supplies", "Equipment", "Miscellaneous"]
    for index, category in enumerate(sku_categories):
        print(f"{index + 1}. {category}")
    print("----------------------------------")
    while True:
        try:
            selected_index = int(input(f"Enter the category where your SKU belongs to (1 - "
                                       f"{len(sku_categories)}): ")) - 1
            if selected_index in range(len(sku_categories)):
                selected_category = sku_categories[selected_index]
                return selected_category
            else:
                print("Invalid Input: Please provide a valid category number!", file=sys.stderr)
                print()
        except ValueError:
            print("Invalid Input: Please try again!", file=sys.stderr)
            print()`

This function, get_sku_category() shows the user all available categories to label their most recent inputted SKU and returns the user's valid category selection.

`def write_inventory_to_file(inventory_item: InventoryItem, file_name):
    try:
        with open(file_name, "a") as file:
            inventory_string = f"{inventory_item.sku}, {inventory_item.category}, {inventory_item.quantity_in_stock}"
            file.write(inventory_string)
            file.write("\n")
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while writing to the file: {file_name}", file=sys.stderr)
    print(f"--- Saved! You have successfully added {inventory_item.sku} to {file_name}!")`

The function, write_inventory_to_file(inventory_item, file_name) takes in an InventoryItem object and write it into a specified file accordingly to ensure the data will always be persistent and concise in the file.

`def summarize_inventory(file_name):
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
        print(f"{key}: {value}")`

The function, summarize_inventory(file_name) summarizes the data inserted to the file previously by category. It reads the file, breaks down each line in the file into individual parts to access the specific part in each line and then adds it into a dictionary, pairing it with the quantity in stock, and if there are multiple SKUs in the same category, their quantity will be summed.
### Major Challenges
Key aspects could include pieces that your struggled on and/or pieces that you are proud of and want to show off.


## Example Runs
Explain how you documented running the project, and what we need to look for in your repository (text output from the project, small videos, links to videos on youtube of you running it, etc)

## Testing
How did you test your code? What did you do to make sure your code was correct? If you wrote unit tests, you can link to them here. If you did run tests, make sure you document them as text files, and include them in your submission. 

> _Make it easy for us to know you *ran the project* and *tested the project* before you submitted this report!_


## Missing Features / What's Next
Focus on what you didn't get to do, and what you would do if you had more time, or things you would implement in the future. 

## Final Reflection
Write at least a paragraph about your experience in this course. What did you learn? What do you need to do to learn more? Key takeaways? etc.