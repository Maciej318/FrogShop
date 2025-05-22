from session import *
from tkinter import messagebox
from zabka.Frog import get_customers


# Logowanie uzytkownika
def client_login(name_entry):
    username = name_entry.get()
    try:
        if not username :
            messagebox.showerror("Błąd", "Musisz wprowadzić login")
            return False

        data = get_customers()

        if username.lower() in data['NAME'].str.lower().values:
            login(username)
            return True
        else:
            messagebox.showerror("Błąd","Nie poprawny login")
            return False


    except Exception as e:
        messagebox.showerror("Błąd", f"{e}")
        return False


# Logowanie jako admin
def admin_login(name_entry):
    if name_entry.get().lower() == "admin":
        return True
    else:
        messagebox.showerror("Błąd", "Nie można zalogować jako admin")
        return False

# Sprawdzenie aktualnego uzytkownika
# def spr():
#     if is_logged_in():
#         messagebox.showinfo("Status:", f"zalogowany jako: {get_current_user()}")
#     else:
#         messagebox.showinfo("Status:", "Nikt nie jest zalogowany")
#
