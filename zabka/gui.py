import tkinter as tk
from PIL import Image, ImageTk
from add_product import show_add_product_window
from delete_product import show_delete_product_window
from product_list import show_products_window
from customer_list import show_customer_list
from add_customer import show_add_customer_window


def start_gui():
    root = tk.Tk()
    root.title("Żabka - Mały Wielki Sklep")
    root.config(bg="#569b31")
    root.geometry("1200x500")

    show_login_screen(root)
    root.mainloop()

#Usuwa wszystko
def clear_screen(root):
    for widget in root.winfo_children():
        widget.destroy()

#Ekran logowania -----------------------------------
def show_login_screen(root):
    clear_screen(root)

    title = tk.Label(root, text="Zaloguj Się Do Sklepu Żabka",
                     fg="white", font=("Helvetica", 30, "bold"), bg="#569b31")
    title.pack(pady=20)

    frame1 = tk.LabelFrame(root, text="Logowanie", padx=10, pady=10,
                           fg="white", font=("Helvetica", 20, "bold"), bg="#569b31")
    frame1.pack(padx=50, pady=100, fill="x")

    tk.Label(frame1, text="Login:", fg="white",
             font=("Helvetica", 10, "bold"), bg="#569b31").grid(row=0, column=0)
    entry_name = tk.Entry(frame1)
    entry_name.grid(row=0, column=1, padx=5, pady=5)

    tk.Button(
        frame1,
        text="Zaloguj Jako Klient",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_client_panel(root, entry_name.get())
    ).grid(row=2, columnspan=2, pady=10)

    tk.Button(
        frame1,
        text="Zaloguj Jako ADMIN",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_admin_panel(root, entry_name.get())
    ).grid(row=3, columnspan=2, pady=10)

    #LOGO
    try:
        image = Image.open("Assets/logo.png")
        imageResized = image.resize((100, 100))
        logo = ImageTk.PhotoImage(imageResized)

        label = tk.Label(root, image=logo, bd=0, highlightthickness=0)
        label.place(x=60, y=60, anchor="center")
        label.image = logo
    except Exception as e:
        print(f"Błąd ładowania obrazu: {e}")

#Panel klienta ---------------------------------------
def show_client_panel(root, login):
    clear_screen(root)

    # tk.Label(root, text="Panel Klienta",
    #          fg="white", font=("Helvetica", 30, "bold"), bg="#569b31").pack(pady=20)
    #
    # tk.Label(root, text=f"Witaj, {login}!",
    #          fg="white", font=("Helvetica", 16), bg="#569b31").pack()


    frame2 = tk.Frame(root, bg="#4e8c2a", width=300, height=350, highlightbackground="white", highlightthickness=2)
    frame2.place(x=30, y=120)
    tk.Label(root, text="Koszyk",
                      fg="white", font=("Helvetica", 25, "bold"), bg="#569b31").place(x=120, y=130)

    frame3 = tk.Frame(root, bg="#4e8c2a", width=800, height=280, highlightbackground="white", highlightthickness=2)
    frame3.place(x=350, y=120)
    tk.Label(root, text="Dostępne Produkty",
             fg="white", font=("Helvetica", 25, "bold"), bg="#569b31").place(x=585, y=130)

    frame4 = tk.Frame(root, bg="#4e8c2a", width=800, height=60, highlightbackground="white", highlightthickness=2)
    frame4.place(x=350, y=50)

    frame5 = tk.Frame(root, bg="#4e8c2a", width=800, height=60, highlightbackground="white", highlightthickness=2)
    frame5.place(x=350, y=410)
    tk.Label(root, text="Filtr Produktów",
             fg="white", font=("Helvetica", 25, "bold"), bg="#569b31").place(x=585, y=420)

    # Przycisk kup
    tk.Button(
        root,
        text="Kup",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
    ).place(x=105, y=420)

    # Przycisk historia
    tk.Button(
        root,
        text="Historia",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
    ).place(x=775, y=65)

    # Przycisk wyloguj
    tk.Button(
        root,
        text="Wyloguj",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_login_screen(root)
    ).place(x=950, y=65)

    # LOGO
    try:
        image = Image.open("Assets/logo.png")
        imageResized = image.resize((100, 100))
        logo = ImageTk.PhotoImage(imageResized)

        label = tk.Label(root, image=logo, bd=0, highlightthickness=0)
        label.place(x=180, y=60, anchor="center")
        label.image = logo
    except Exception as e:
        print(f"Błąd ładowania obrazu: {e}")

#Panel admina --------------------------------------
def show_admin_panel(root, login):
    clear_screen(root)

    tk.Label(root, text="Panel Administratora",
             fg="white", font=("Helvetica", 30, "bold"), bg="#569b31").pack(pady=20)

    tk.Label(root, text=f"Witaj, Administratorze {login}!",
             fg="white", font=("Helvetica", 16), bg="#569b31").pack()

    # Ramka z przyciskami
    button_frame = tk.Frame(root, bg="#569b31")
    button_frame.pack(pady=20)

    # Przycisk pokazujący produkty
    tk.Button(
        button_frame,
        text="Pokaż produkty",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_products_window()
    ).pack(side=tk.LEFT, padx=10)

    tk.Button(
        button_frame,
        text="Usuń produkt",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_delete_product_window(root)
    ).pack(side=tk.LEFT, padx=10)

    # Przycisk dodawania produktu
    tk.Button(
        button_frame,
        text="Dodaj produkt",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_add_product_window(root)
    ).pack(side=tk.LEFT, padx=10)

    # Użytkownicy
    tk.Button(
        button_frame,
        text="Użytkownicy",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_users_panel(root,login)
    ).pack(side=tk.LEFT, padx=10)

    # Przycisk wyloguj
    tk.Button(
        root,
        text="Wyloguj",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_login_screen(root)
    ).place(x=10, y=460)

    try:
        image2 = Image.open("Assets/computer.png")
        imageResized2 = image2.resize((320, 320))
        comp = ImageTk.PhotoImage(imageResized2)

        label = tk.Label(root, image=comp, bd=0, highlightthickness=0)
        label.place(x=610, y=350, anchor="center")
        label.image = comp
    except Exception as e:
        print(f"Błąd ładowania obrazu: {e}")

    # LOGO
    try:
        image = Image.open("Assets/logo.png")
        imageResized = image.resize((100, 100))
        logo = ImageTk.PhotoImage(imageResized)

        label = tk.Label(root, image=logo, bd=0, highlightthickness=0)
        label.place(x=60, y=60, anchor="center")
        label.image = logo
    except Exception as e:
        print(f"Błąd ładowania obrazu: {e}")


# Panel uzytkownikow -----------------------------------------
def show_users_panel(root, login):
    clear_screen(root)

    tk.Label(root, text="Panel Użytkowników",
             fg="white", font=("Helvetica", 30, "bold"), bg="#569b31").pack(pady=20)

    # Ramka z przyciskami
    button_frame = tk.Frame(root, bg="#569b31")
    button_frame.pack(pady=20)

    # Przycisk pokazujący uzytkownikow
    tk.Button(
        button_frame,
        text="Pokaż użytkowników",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_customer_list()
    ).pack(side=tk.LEFT, padx=10)

    # Okno dodania uzytkownika
    tk.Button(
        button_frame,
        text="Dodaj użytkownika",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_add_customer_window(root)
    ).pack(side=tk.LEFT, padx=10)

    tk.Button(
        button_frame,
        text="Usuń użytkownika",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
    ).pack(side=tk.LEFT, padx=10)

    tk.Button(
        button_frame,
        text="Edytuj użytkownika",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
    ).pack(side=tk.LEFT, padx=10)

    tk.Button(
        root,
        text = "Cofnij",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_admin_panel(root, login)
    ).place(x=10, y=460)

    try:
        image2 = Image.open("Assets/computer.png")
        imageResized2 = image2.resize((320, 320))
        comp = ImageTk.PhotoImage(imageResized2)

        label = tk.Label(root, image=comp, bd=0, highlightthickness=0)
        label.place(x=610, y=350, anchor="center")
        label.image = comp
    except Exception as e:
        print(f"Błąd ładowania obrazu: {e}")

    # LOGO
    try:
        image = Image.open("Assets/logo.png")
        imageResized = image.resize((100, 100))
        logo = ImageTk.PhotoImage(imageResized)

        label = tk.Label(root, image=logo, bd=0, highlightthickness=0)
        label.place(x=60, y=60, anchor="center")
        label.image = logo
    except Exception as e:
        print(f"Błąd ładowania obrazu: {e}")

