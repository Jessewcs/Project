"""
Final Project: Inventory Managing Application
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Jesse Wojtanowicz

A comprehensive system designed to facilitate the management of stock keeping units (SKUs) in an inventory setting.
"""
from inventory_spec import InventoryItem


def get_option():
    """ Displays a menu of options and prompts the user to select one.

    Returns:
        str: The selected option as a string.
    """
    options = ("1", "2", "3", "4", "5")
    print("--------------------------------------------------------")
    print("--- Inventory Item Manager: Select one of the following:")
    print("1. Add & Save a Stock Keeping Unit (SKU)")
    print("2. Remove an existing Stock Keeping Unit")
    print("3. List all individual Stock Keeping Units")
    print("4. Summarize the quantity of SKUs by Category")
    print("5. Exit the Inventory Manager Application")
    print("--------------------------------------------------------")
    selected_index = input(f"Which option would you like to select? (1 - {len(options)}): ").strip()
    while selected_index not in options:
        selected_index = input(f"Invalid Option: Please enter a valid number! (1 - {len(options)}): ").strip()
    return selected_index


def get_sku():
    """ Prompts the user to enter an item name and a unique identifier to create an SKU.

    Returns:
        str: A string representing the SKU in the format ItemName-UniqueIdentifier.
    """
    while True:
        try:
            item = input("Enter the item name (e.g. 'Shirt'): ").strip()
            if item != "" and item.isalnum():
                unique_sku = input("Enter a unique identifier for this SKU (e.g. 'XYZ123'): ").strip()
                if len(unique_sku) == 6 and unique_sku.isalnum():
                    sku = f"{item}-{unique_sku[:3]}-{unique_sku[3:]}"
                    return sku
                else:
                    print("Invalid Input: Please enter a valid format for the unique identifier! (e.g. 'ABC123')")
            else:
                print("Invalid Input: Please enter a valid alphanumeric item name!")
        except ValueError:
            print("Error: Please try again!")


def get_sku_quantity():
    """ Gets the SKU from the user and then prompts for its quantity in stock.
        Validates the quantity.

    Returns:
        tuple: A tuple containing the SKU as a string and its quantity as an integer.
    """
    sku = get_sku()

    while True:
        try:
            quantity = input(f"Enter the quantity in stock for item, {sku}: ").strip()
            quantity = int(quantity)
            if quantity >= 0:
                return sku, quantity
            else:
                print("Invalid Input: Please provide a non-negative quantity!")
        except ValueError:
            print("Invalid Input: Please enter a valid numeric quantity amount!")


def list_sku_categories(sku_categories):
    """ Displays a list of categories for the user.

    Parameters:
        sku_categories (list): A list of available categories
    """
    print("----------------------------------")
    print("--- Select an Item (SKU) Category:")
    for index, category in enumerate(sku_categories, 1):
        print(f"{index}. {category}")
    print("----------------------------------")


def get_sku_category(sku_categories):
    """ Displays a list of categories and prompts the user to select one.

    Parameters:
        sku_categories (list): A list of available categories

    Returns:
        str: The selected category.
    """
    list_sku_categories(sku_categories)

    while True:
        try:
            selected_index = input(f"Enter the category where your SKU belongs to (1 - "
                                   f"{len(sku_categories)}): ").strip()
            selected_index = int(selected_index)
            if 1 <= selected_index <= len(sku_categories):
                selected_category = sku_categories[selected_index - 1]
                return selected_category
            else:
                print("Invalid Input: Please provide a valid category number!")
        except ValueError:
            print("Invalid Input: Please try again!")


def inventory_item_class(sku, category, quantity):
    """ Creates an instance of the InventoryItem Class.

    Parameters:
        sku (str): The SKU of the item.
        category (str): The category of the item.
        quantity (int): The quantity of the item.

    Returns:
        InventoryItem: An instance of the class InventoryItem.
    """
    inventory_item = InventoryItem(sku=sku, category=category, quantity_in_stock=quantity)
    return inventory_item


def write_inventory_to_file(inventory_item: InventoryItem, file_name):
    """ Writes an inventory item's information to a file.

    Parameters:
        inventory_item (InventoryItem): The item to write to the file.
        file_name (str): Te name of the file to with the item is written too.
    """
    try:
        with open(file_name, "a") as file:
            inventory_string = f"{inventory_item.sku}, {inventory_item.category}, {inventory_item.quantity_in_stock}"
            file.write(inventory_string)
            file.write("\n")
    except FileNotFoundError:
        print(f"Error: {file_name} was not found!")
    except OSError:
        print(f"Error: Something happened while writing to the file: {file_name}")


def summarize_inventory(file_name):
    """Reads inventory item information from a file and summarizes the quantity of items by category.

    Parameters:
        file_name (str): The name of the file from which inventory information is being read.
    """
    inventory_sum = {}
    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    dict_parts = line.strip().split(",")
                    category = dict_parts[1].strip()
                    quantity = int(dict_parts[2].strip())
                    if category in inventory_sum:
                        inventory_sum[category] += quantity
                    else:
                        inventory_sum[category] = quantity
                except IndexError:
                    print(f"Error: File not specified correctly, line: {line}")
            return inventory_sum
    except FileNotFoundError:
        print(f"{file_name} was not found!")
    except OSError:
        print(f"Error: Something happened while reading the file: {file_name}")


def list_skus(file_name):
    """ Reads and displays a list of SKUs from a file.

    Parameters:
        file_name (str): The name of the file from which SKUs are read from.

    Returns:
        list: A list of tuples containing the SKU, category, and the quantity in stock.
    """
    sku_list = []
    try:
        with open(file_name, "r") as file:
            for line in file:
                try:
                    line_parts = line.strip().split(",")
                    sku = line_parts[0].strip()
                    category = line_parts[1].strip()
                    quantity = line_parts[2].strip()
                    sku_list.append((sku, category, quantity))
                except IndexError:
                    print(f"Error: File not specified correctly, line: {line}")
            return sku_list
    except FileNotFoundError:
        print(f"Error: {file_name} was not found!")
    except OSError:
        print(f"Error: Something happened while reading the file: {file_name}")


def get_sku_to_remove(sku_list):
    """ Prompts the user to select an SKU to remove from a provided list.

    Parameters:
        sku_list (list): A list of SKUs from which the user can select from.

    Returns:
        str: The selected SKU to be removed.
    """
    while True:
        try:
            selected_index = input(f"Select the Stock Keeping Unit (SKU) that you wish to remove"
                                   f" (1 - {len(sku_list)}): ").strip()
            selected_index = int(selected_index)
            if 1 <= selected_index <= len(sku_list):
                sku_to_remove = sku_list[selected_index - 1][0]
                return sku_to_remove
            else:
                print("Invalid Selection: Please provide a valid option!")
        except ValueError:
            print("Invalid Input: Please try again")


def remove_sku(sku_to_remove, file_name):
    """ Removes a specified SKU from a file.

    Parameters:
        sku_to_remove (str): The SKU to be removed.
        file_name (str): The name of the file from which to remove the SKU.
    """
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

        with open(file_name, "w") as file:
            for line in lines:
                try:
                    cleaned_line = line.strip().split(",")
                    sku = cleaned_line[0]
                    if sku != sku_to_remove:
                        file.write(line)
                except IndexError:
                    print(f"Error: File not specified correctly, line: {line}")
    except FileNotFoundError:
        print(f"Error: {file_name} was not found!")
    except OSError:
        print(f"Error: Something happened while modifying the file: {file_name}")


def clear_inventory(file_name):
    """ Clears all inventory information from a file

    Parameters:
        file_name (str): The name of the file from which inventory is to be removed.
    """
    try:
        open(file_name, "w").close()
    except FileNotFoundError:
        print(f"Error: {file_name} was not found!")
    except OSError:
        print(f"Error: Something happened while modifying the file: {file_name}")


def main():
    """ The main driver of the program. Provides a menu to the user
    and executes the selected option.
    """
    file_name = "inventory.txt"

    while True:
        selected_option = get_option()

        if selected_option == "5":
            print("\nWe'll see you next time!")
            break

        elif selected_option == "1":
            print("\nWelcome to your Inventory Item Managing System:")
            print("----------------------------------------------")
            sku, quantity = get_sku_quantity()
            sku_categories = ["Raw Materials", "Consumer Goods", "Office Supplies", "Equipment", "Miscellaneous"]
            category = get_sku_category(sku_categories)
            inventory_item = inventory_item_class(sku, category, quantity)
            write_inventory_to_file(inventory_item, file_name)
            print(f"\nSaved! You have successfully added {inventory_item.sku} to {file_name}!\n")

        elif selected_option == "2":
            sku_list = list_skus(file_name)
            if not sku_list:
                print("\nThere are currently no saved Stock Keeping Units (SKUs) to be removed!\n")
            else:
                choices = ("1", "2")
                print("\n----------------------------------------------------------------------")
                print("--- Choose one of the following options to proceed:")
                print(f"1. Permanently remove a single Inventory Item (SKU) from {file_name}")
                print(f"2. Permanently remove ALL saved Inventory Items from {file_name}")
                print("----------------------------------------------------------------------")
                selected_choice = input(f"Which choice would you like to select? (1 - {len(choices)}): ").strip()
                while selected_choice not in choices:
                    selected_choice = input(f"Invalid Choice: Please enter a valid number! "
                                            f"(1 - {len(choices)}): ").strip()

                if selected_choice == "1":
                    print("\n--------------------------------------------------------")
                    print("--- Select an Inventory Item that you'd like to remove: ")
                    for index, item in enumerate(sku_list, 1):
                        print(f"{index}. {item[0]}, {item[1]}, {item[2]}")
                    print("--------------------------------------------------------")
                    sku_to_remove = get_sku_to_remove(sku_list)
                    if sku_to_remove:
                        remove_sku(sku_to_remove, file_name)
                        print(f"\nStock Keeping Unit: {sku_to_remove} has been successfully removed from inventory!\n")

                elif selected_choice == "2":
                    clear_inventory(file_name)
                    print(f"\nYou have permanently removed all Inventory Items from {file_name}!\n")
                else:
                    print(f"\nError: Something went wrong with, {selected_choice}")

        elif selected_option == "3":
            sku_list = list_skus(file_name)
            if not sku_list:
                print("\nThere are currently no saved Stock Keeping Units (SKUs) to be listed!\n")
            else:
                print("\n----------------------------------------------------------------")
                print(f"--- All individually saved Stock Keeping Units from {file_name}")
                for index, item in enumerate(sku_list, 1):
                    print(f"{index}. {item[0]}, {item[1]}, {item[2]}")
                print("----------------------------------------------------------------\n")

        elif selected_option == "4":
            sku_list = list_skus(file_name)
            if not sku_list:
                print("\nThere are currently no saved Inventory Items to be summarized!\n")
            else:
                print("\n--------------------------------------------------------")
                print(f"--- The Quantity in Stock by Category from {file_name}:")
                inventory_sum = summarize_inventory(file_name)
                for key, category in enumerate(inventory_sum, 1):
                    print(f"{key}. {category}, {inventory_sum[category]}")
                print("--------------------------------------------------------\n")

        else:
            print(f"\nError: Something went wrong with, {selected_option}")


if __name__ == "__main__":
    main()
