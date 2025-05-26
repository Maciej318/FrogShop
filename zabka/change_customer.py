import tkinter as tk
from zabka.Frog import update_customer


def update_change_customer_window(root):
    change_window = tk.Toplevel(root)
    change_window.title("Zmień dane użytkownika")
    change_window.geometry("400x300")
    change_window.configure(bg="#569b31")

    tk.Label(change_window, text="Id użytkownika do zmiany ", bg="#569b31", fg="white", font="bold").pack(pady=10)
    entry_id = tk.Entry(change_window)
    entry_id.pack()

    tk.Label(change_window, text="Nowa nazwa użytkownika", bg="#569b31", fg="white").pack(pady=5)
    entry_name = tk.Entry(change_window)
    entry_name.pack()

    tk.Label(change_window, text="Nowy e-mail", bg="#569b31", fg="white" ).pack(pady=5)
    entry_email = tk.Entry(change_window)
    entry_email.pack()

    tk.Label(change_window, text="Nowy nr telefonu", bg="#569b31", fg="white").pack(pady=5)
    entry_number = tk.Entry(change_window)
    entry_number.pack()

    tk.Button(
        change_window,
        text = "Zmień dane",
        bg = "#4CAF50", fg = "white",
        command = lambda : update_customer(entry_id.get(),
                                           entry_name.get(),
                                           entry_email.get(),
                                           entry_number.get(),
                                           change_window),
    ).pack(pady = 20)

