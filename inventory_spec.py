"""
Final Project: Inventory Managing Application
===========================
Course:   CS 5001
Semester: Fall 2023
Student:  Jesse Wojtanowicz

A comprehensive system designed to facilitate the management of stock keeping units (SKUs) in an inventory setting.
"""


class InventoryItem:
    def __init__(self, sku, category, quantity_in_stock):
        self.sku = sku
        self.category = category
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        return f"SKU: {self.sku}, Category: {self.category}, Quantity in Stock: {self.quantity_in_stock}"
