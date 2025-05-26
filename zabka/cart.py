import tkinter as tk
import os
from tkinter import messagebox
import pandas as pd

from session import get_current_user


def dodaj_do_koszyka(tree, koszyk_listbox, save_in_file = False):
    selected_item = tree.focus()
    if not selected_item:
        messagebox.showwarning("Brak wyboru", "Wybierz produkt z listy.")
        return

    item_values = tree.item(selected_item, "values")
    produkt = f"{item_values[0]} - {item_values[1]} zł"
    koszyk_listbox.insert(tk.END, produkt)

    if save_in_file:
        save_cart_items(koszyk_listbox)


def save_cart_items(koszyk_listbox):

    username = get_current_user()

    if not username:
        messagebox.showwarning("Błąd", "Nie jesteś zalogowany!")
        return

    try:

        customers = pd.read_csv("Frog/customer.csv")
        user_data = customers[
            customers['NAME'].str.strip().str.lower() == username.strip().lower()
        ]

        if user_data.empty:
            messagebox.showerror("Błąd", "Nie znaleziono użytkownika w bazie!")

        user_id = user_data.iloc[0]['ID']
        database_dir = "Frog/DATABASE"
        file_path = os.path.join(database_dir, f"{user_id}.txt")

        with open(file_path, "a", encoding="utf-8") as f:
            for i in range(koszyk_listbox.size()):
                f.write(f"{koszyk_listbox.get(i)}\n")


        messagebox.showinfo("Sukces", "Produkty zostały zapisane!")
        return

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił nieoczekiwany błąd: {str(e)}")

