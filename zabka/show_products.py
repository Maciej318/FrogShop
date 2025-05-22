import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from zabka.Frog import get_products

def show_products(root):
    try:
        data = get_products()

        frame3 = tk.Frame(root, bg="#4e8c2a", width=800, height=280, highlightbackground="white", highlightthickness=2)
        frame3.place(x=350, y=120)

        tree = ttk.Treeview(frame3)
        tree.place(x=0, y=0, relwidth=0.965, relheight=1)

        scrollbar_y = ttk.Scrollbar(frame3, orient="vertical", command=tree.yview)
        scrollbar_y.place(relx=0.965, rely=0, relwidth=0.035, relheight=1)

        tree.configure(yscrollcommand=scrollbar_y.set)

        selected_columns = ["Name", "Price"]
        tree["columns"] = selected_columns
        tree["show"] = "headings"

        for col in selected_columns:
            tree.heading(col, text=col.capitalize())
            tree.column(col, anchor="center", width=150)

        for _, row in data.iterrows():
            values = [row[col] for col in selected_columns]
            tree.insert("", "end", values=values)

        return tree

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie można wczytać produktów: {str(e)}")
        return None