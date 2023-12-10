"""
Final Project: Inventory Managing Application
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Jesse Wojtanowicz

A comprehensive system designed to facilitate the management of stock keeping units (SKUs) in an inventory setting.
"""
from inventory_spec import InventoryItem
import sys


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
    selected_index = input(f"Which option would you like to select? (1 - {len(options)}): ")
    selected_index = selected_index.strip()
    while selected_index not in options:
        selected_index = input(f"Invalid Option: Please enter a valid number! (1 - {len(options)}): ")
        selected_index = selected_index.strip()
    print()
    return selected_index


def get_sku():
    """ Prompts the user to enter a Stock Keeping Unit (SKU)

    Returns:
        str: A valid SKU entered by the user.
    """
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


def get_sku_quantity():
    """ Gets the SKU from the user and then prompts for its quantity in stock.
        Validates the quantity.

    Returns:
        tuple: A tuple containing the SKU as a string and its quantity as an integer.
    """
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


def get_sku_category():
    """ Displays a list of categories and prompts the user to select one.

    Returns:
        str: The selected category.

    """
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
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while writing to the file: {file_name}", file=sys.stderr)


def summarize_inventory(file_name):
    """Reads inventory item information from a file and summarizes the quantity of items by category.

    Parameters:
        file_name (str): The name of the file from which inventory information is being read.
    """
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
            return inventory_sum
    except IndexError:
        print("File not specified correctly!", file=sys.stderr)
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while reading the file: {file_name}", file=sys.stderr)


def list_skus(file_name):
    """ Reads and displays a list of SKUs from a file.

    Parameters:
        file_name (str): The name of the file from which SKUs are read from.

    Returns:
        list: A list of tuples containing the SKU, category, and the quantity in stock.
    """
    sku_dict = {}
    try:
        with open(file_name, "r") as file:
            lines = file.readlines()

            for index, line in enumerate(lines):
                cleaned_line = line.strip()
                sku_dict[index + 1] = cleaned_line
                return sku_dict
    except FileNotFoundError:
        print("error")


def get_sku_to_remove(sku_list):
    """ Prompts the user to select an SKU to remove from a provided list.

    Parameters:
        sku_list (list): A list of SKUs from which the user can select from.

    Returns:
        str: The selected SKU to be removed.
    """
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
                cleaned_line = line.strip().split(",")
                sku = cleaned_line[0]
                if sku != sku_to_remove:
                    file.write(line)
    except FileNotFoundError:
        print(f"{file_name} was not found!", file=sys.stderr)
    except OSError:
        print(f"Something happened while modifying the file: {file_name}", file=sys.stderr)


def clear_inventory(file_name):
    """ Clears all inventory information from a file

    Parameters:
        file_name (str): The name of the file from which inventory is to be removed.
    """
    open(file_name, "w").close()


def main():
    """ The main driver of the program. Provides a menu to the user
    and executes the selected option.
    """
    file_name = "inventory.txt"

    while True:
        selected_option = get_option()

        if selected_option == "5":
            print()
            print("We'll see you next time!")
            break

        elif selected_option == "1":
            print("Welcome to your Inventory Item Managing System:")
            print("----------------------------------------------")
            sku, quantity = get_sku_quantity()
            category = get_sku_category()
            inventory_item = inventory_item_class(sku, category, quantity)
            write_inventory_to_file(inventory_item, file_name)
            print(f"Saved! You have successfully added {inventory_item.sku} to {file_name}!")

        elif selected_option == "2":
            sku_list = list_skus(file_name)
            if not sku_list:
                print("There are currently no saved Stock Keeping Units (SKUs) to be removed!", file=sys.stderr)
                print()
            else:
                choices = ("1", "2")
                print("----------------------------------------------------------------------")
                print("--- Choose one of the following options to proceed:")
                print(f"1. Permanently remove a single Inventory Item (SKU) from {file_name}")
                print(f"2. Permanently remove ALL saved Inventory Items from {file_name}")
                print("----------------------------------------------------------------------")
                selected_choice = input(f"Which choice would you like to select? (1 - {len(choices)}): ")
                selected_choice = selected_choice.strip()
                while selected_choice not in choices:
                    selected_choice = input(f"Invalid Choice: Please enter a valid number! (1 - {len(choices)}): ")
                    selected_choice = selected_choice.strip()

                if selected_choice == "1":
                    print("--------------------------------------------------------")
                    print("--- Select an Inventory Item that you'd like to remove: ")
                    for index, item in enumerate(sku_list, 1):
                        print(f"{index}. {item[0]}, {item[1]}, {item[2]}")
                    print("--------------------------------------------------------")
                    sku_to_remove = get_sku_to_remove(sku_list)
                    if sku_to_remove:
                        remove_sku(sku_to_remove, file_name)
                        print(f"Stock Keeping Unit: {sku_to_remove} has been successfully removed from inventory!")

                elif selected_choice == "2":
                    clear_inventory(file_name)
                    print(f"You have permanently removed all Inventory Items from {file_name}!")
                else:
                    print(f"Error! Something went wrong with, {selected_choice}")

        elif selected_option == "3":
            sku_list = list_skus(file_name)
            if not sku_list:
                print("There are currently no saved Stock Keeping Units (SKUs) to be listed!", file=sys.stderr)
                print()
            else:
                print("----------------------------------------------------------------")
                print(f"--- All individually saved Stock Keeping Units from {file_name}")
                for key, value in sku_list.items():
                    print(f"{key}. {value}")


        elif selected_option == "4":
            sku_list = list_skus(file_name)
            if not sku_list:
                print("There are currently no saved Inventory Items to be summarized!", file=sys.stderr)
                print()
            else:
                print("--------------------------------------------------------")
                print(f"--- The Quantity in Stock by Category from {file_name}:")
                inventory_sum = summarize_inventory(file_name)
                for key, category in enumerate(inventory_sum, 1):
                    print(f"{key}. {category}, {inventory_sum[category]}")
                print("--------------------------------------------------------")

        else:
            print(f"Error! Something went wrong with, {selected_option}")


if __name__ == "__main__":
    main()