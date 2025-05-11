import tkinter as tk
from zabka.Frog import add_customer



def show_add_customer_window(root):
    add_window = tk.Toplevel(root)
    add_window.title("Dodaj użytkownika")
    add_window.geometry("400x300")
    add_window.configure(bg = "#569b31")

    #Etykieta input
    tk.Label(add_window, text = "Nazwa użytkownika", bg = "#569b31", fg = "white").pack(pady = 5)
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    tk.Label(add_window, text = "E-mail", bg = "#569b31", fg = "white").pack(pady = 5)
    entry_email = tk.Entry(add_window)
    entry_email.pack()

    tk.Label(add_window, text = "NR telefonu", bg = "#569b31", fg = "white").pack(pady = 5)
    entry_number = tk.Entry(add_window)
    entry_number.pack()



    tk.Button(
        add_window,
        text = "Dodaj użytkownika",
        command = lambda: add_customer(entry_name.get(),
                                       entry_email.get(),
                                       entry_number.get(),
                                       add_window),
        bg = "#4CAF50", fg = "white"
    ).pack(pady = 20)

