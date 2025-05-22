import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def dodaj_do_koszyka(tree, koszyk_listbox):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Brak wyboru", "Wybierz produkt z listy.")
        return

    item_values = tree.item(selected_item, "values")
    produkt = f"{item_values[0]} - {item_values[1]} zł"
    koszyk_listbox.insert(tk.END, produkt)
