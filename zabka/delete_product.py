import tkinter as tk
from zabka.Frog import delete_product

def show_delete_product_window(root):
    delete_window = tk.Toplevel(root)
    delete_window.title("Usuń produkt")
    delete_window.geometry("300x200")
    delete_window.configure(bg="#569b31")

    tk.Label(delete_window, text="ID produktu do usunięcia:", bg="#569b31", fg="white").pack(pady=20)
    entry_id = tk.Entry(delete_window)
    entry_id.pack()

    tk.Button(
        delete_window,
        text="Usuń",
        bg="#4CAF50", fg="white",
        command=lambda: delete_product(entry_id.get(), delete_window)
    ).pack(pady=20)
