import tkinter as tk
from itertools import product
from tkinter import ttk
from tkinter import messagebox
from zabka.Frog import get_customers




def show_customer_list():
    try:
        customers = get_customers()

        # Tworzenie nowego okna
        customers_window = tk.Toplevel()
        customers_window.title("Lista użytkowników")
        customers_window.geometry("800x600")
        customers_window.configure(bg = "#569b31")

        # Nagłówek
        tk.Label(customers_window, text = "Lista użytkowników",
            fg = "white", font = ("Helvetica", 20, "bold"), bg = "#569b31").pack(pady=10)


        # Ramka z tabela
        frame = tk.Frame(customers_window, bg="#fffa0b", bd = 2, relief="groove", padx=5, pady=5)
        frame.pack(pady = 10, padx = 10, fill = tk.BOTH, expand = True)

        #Tworzenie tabeli
        tree = ttk.Treeview(frame)
        tree.pack(fill = tk.BOTH, expand = True)

        # Konfiguracja kolumn
        tree["columns"] = list(customers.columns)
        tree["show"] = "headings"

        for col in customers.columns:
            tree.heading(col, text = col)
            tree.column(col, anchor = "center" ,width = 100)


        # Dodawanie danych
        for _, row in customers.iterrows():
            tree.insert("", "end", values = list(row))

        # Pasek przewijania

        scrollbar = ttk.Scrollbar(frame, orient = "vertical", command = tree.yview)
        scrollbar.pack(side = tk.RIGHT, fill = tk.Y)
        tree.configure(yscrollcommand = scrollbar.set)

    except Exception as e:
        messagebox.showerror("Błąd", f"Nie można wczytać użytkowników: {str(e)}")
