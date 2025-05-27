import os
import pandas as pd
from tkinter import messagebox
from session import get_current_user
import tkinter as tk

def show_history():
    username = get_current_user()

    if not username:
        messagebox.showwarning("Błąd", "Nie jesteś zalogowany!")
        return

    try:
        customers = pd.read_csv("Frog/customer.csv")
        user_data = customers[
            customers['NAME'].str.strip().str.lower() == username.strip().lower()
            ]

        if user_data.empty:
            messagebox.showerror("Błąd", "Nie znaleziono użytkownika w bazie!")
            return

        user_id = user_data.iloc[0]['ID']
        file_path = os.path.join("Frog/DATABASE", f"{user_id}.txt")

        if not os.path.exists(file_path):
            messagebox.showinfo("Historia zakupów", "Brak zapisanych zakupów.")
            return

        with open(file_path, "r", encoding="utf-8") as f:
            produkty = [line.strip() for line in f if line.strip()]

        if not produkty:
            messagebox.showinfo("Historia zakupów", "Brak zapisanych zakupów.")
            return

        # Nowe okno
        historia_window = tk.Toplevel()
        historia_window.title("Historia zakupów")
        historia_window.geometry("360x420")
        historia_window.configure(bg="#569b31")

        # Ramka
        historia_frame = tk.Frame(historia_window, bg="#569b31", width=300, height=350,
                                  highlightbackground="white", highlightthickness=2)
        historia_frame.place(x=30, y=30)

        # Tytuł
        tk.Label(historia_frame, text="Historia zakupów", font=("Helvetica", 16, "bold"),
                 bg="#569b31", fg="white").place(x=60, y=10)

        # Scrollbar
        historia_scrollbar = tk.Scrollbar(historia_frame, orient="vertical")

        # Listbox
        historia_listbox = tk.Listbox(historia_frame, width=40, height=15,
                                      yscrollcommand=historia_scrollbar.set, bg="white", fg="black")
        historia_listbox.place(x=8, y=50, width=260, height=260)
        historia_scrollbar.place(x=268, y=50, width=12, height=260)

        historia_scrollbar.config(command=historia_listbox.yview)

        for produkt in produkty:
            historia_listbox.insert(tk.END, produkt)

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd podczas odczytu historii: {str(e)}")
