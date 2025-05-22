import tkinter as tk
from zabka.Frog import delete_customer


def show_delete_customer_window(root):
    delete_window = tk.Toplevel(root)
    delete_window.title("Usuń użytkownika")
    delete_window.geometry("300x200")
    delete_window.configure(bg="#569b31")

    tk.Label(
        delete_window,
        text = "Nazwa użytkownika do usunięcia:",
        bg = "#569b31",
        fg = "white",
    ).pack(pady=20)

    entry_name = tk.Entry(delete_window)
    entry_name.pack()

    tk.Button(
        delete_window,
        text = "Usuń",
        bg = "#4CAF50",
        fg = "white",
        command = lambda: delete_customer(entry_name.get(), delete_window),

    ).pack(pady=20)

