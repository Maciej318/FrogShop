import tkinter as tk
from tkinter import ttk
import pandas as pd
from tkinter import messagebox


def show_products_window():
    try:
        data = pd.read_excel("Frog/products.xlsx", engine="openpyxl")

        # Tworzenie nowego okna
        products_window = tk.Toplevel()
        products_window.title("Lista produktów")
        products_window.geometry("800x600")
        products_window.configure(bg="#569b31")

        # Nagłówek
        tk.Label(products_window, text="Lista produktów",
                 fg="white", font=("Helvetica", 20, "bold"), bg="#569b31").pack(pady=10)

        # Ramka z tabelą
        frame = tk.Frame(products_window, bg="#fffa0b", bd=2, relief="groove", padx=5, pady=5)
        frame.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

        # Tworzenie Tabeli
        tree = ttk.Treeview(frame)
        tree.pack(fill=tk.BOTH, expand=True)

        # Konfiguracja kolumn
        tree["columns"] = list(data.columns)
        tree["show"] = "headings"

        for col in data.columns:
            tree.heading(col, text=col)
            tree.column(col, anchor="center", width=100)

        # Dodawanie danych
        for _, row in data.iterrows():
            tree.insert("", "end", values=list(row))

        # Pasek przewijania
        scrollbar = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.configure(yscrollcommand=scrollbar.set)

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie można wczytać produktów: {str(e)}")
