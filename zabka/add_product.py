import tkinter as tk
from zabka.Frog import add_product

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
