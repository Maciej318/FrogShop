import pandas as pd
from tkinter import messagebox
import tkinter as tk

def show_add_product_window(root):
    add_window = tk.Toplevel(root)
    add_window.title("Dodaj nowy produkt")
    add_window.geometry("400x300")
    add_window.configure(bg="#569b31")

    # Etykiety input
    tk.Label(add_window, text="Nazwa produktu:", bg="#569b31", fg="white").pack(pady=5)
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    tk.Label(add_window, text="Cena:", bg="#569b31", fg="white").pack(pady=5)
    entry_price = tk.Entry(add_window)
    entry_price.pack()

    tk.Label(add_window, text="Ilość:", bg="#569b31", fg="white").pack(pady=5)
    entry_quantity = tk.Entry(add_window)
    entry_quantity.pack()

    tk.Label(add_window, text="Kategoria:", bg="#569b31", fg="white").pack(pady=5)
    entry_category = tk.Entry(add_window)
    entry_category.pack()

    # Przycisk dodaj
    tk.Button(
        add_window,
        text="Dodaj produkt",
        command=lambda: add_product(entry_name.get(),
                                    entry_price.get(),
                                    entry_quantity.get(),
                                    entry_category.get(),
                                    add_window),
        bg="#4CAF50", fg="white"
    ).pack(pady=20)

def add_product(name, price, quantity, category, window):
    try:
        if not name or not price or not quantity or not category:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione")
            return

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Błąd", "Cena i ilość muszą być liczbami")
            return

        try:
            data = pd.read_excel("Frog/products.xlsx", engine="openpyxl")
            new_id = data['ID'].max() + 1
        except:
            data = pd.DataFrame(columns=['ID', 'Name', 'Price', 'Quantity', 'Category'])
            new_id = 1

        # Dodanie produktu
        new_product = {
            'ID': new_id,
            'Name': name,
            'Price': price,
            'Quantity': quantity,
            'Category': category
        }

        data = pd.concat([data, pd.DataFrame([new_product])], ignore_index=True)
        data.to_excel("Frog/products.xlsx", index=False)

        messagebox.showinfo("Sukces", "Produkt został dodany pomyślnie")
        window.destroy()
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")
