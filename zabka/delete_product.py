import tkinter as tk
import pandas as pd
from tkinter import messagebox



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

def delete_product(product_id, delete_window):
    try:
        if not product_id:
            messagebox.showerror("Błąd", "Musisz podać ID produktu")
            return

        data = pd.read_excel("Frog/products.xlsx")

        product_id = int(product_id)

        if product_id not in data['ID'].values:
            messagebox.showerror("Błąd", "Nie ma produktu o tym ID")
            return

        data = data[data['ID'] != product_id]
        data.to_excel("Frog/products.xlsx", index=False)

        messagebox.showinfo("Sukces", "Produkt został usunięty")

        delete_window.destroy()



    except Exception as e:
        messagebox.showerror("Błąd", f"{e}")
