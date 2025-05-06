import tkinter as tk
from tkinter import ttk
import pandas as pd
from PIL import Image, ImageTk
from tkinter import messagebox



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

#Ekran logowania
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

#Panel klienta
def show_client_panel(root, login):
    clear_screen(root)

    tk.Label(root, text="Panel Klienta",
             fg="white", font=("Helvetica", 30, "bold"), bg="#569b31").pack(pady=20)

    tk.Label(root, text=f"Witaj, {login}!",
             fg="white", font=("Helvetica", 16), bg="#569b31").pack()
    # Przycisk wyloguj
    tk.Button(
        root,
        text="Wyloguj",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_login_screen(root)
    ).place(x=10, y=460)

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

#Panel admina
def show_admin_panel(root, login):
    clear_screen(root)

    tk.Label(root, text="Panel Administratora",
             fg="white", font=("Helvetica", 30, "bold"), bg="#569b31").pack(pady=20)

    tk.Label(root, text=f"Witaj, Administratorze {login}!",
             fg="white", font=("Helvetica", 16), bg="#569b31").pack()

    # Ramka z przyciskami
    button_frame = tk.Frame(root, bg="#569b31")
    button_frame.pack(pady=20)

    # Przycisk pokazujący produkty w nowym oknie
    tk.Button(
        button_frame,
        text="Pokaż produkty",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_products_window()
    ).pack(side=tk.LEFT, padx=10)

    # Przycisk dodawania produktu
    tk.Button(
        button_frame,
        text="Dodaj produkt",
        font=("Helvetica", 12, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_add_product_window(root)
    ).pack(side=tk.LEFT, padx=10)

    # Przycisk wyloguj
    tk.Button(
        root,
        text="Wyloguj",
        font=("Helvetica", 10, "bold"),
        bg="#4CAF50", fg="white", width=20,
        command=lambda: show_login_screen(root)
    ).place(x=10, y=460)

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

#Pokazuje liste produktów w oknie
def show_products_window():
    try:
        data = pd.read_excel("products.xlsx", engine="openpyxl")

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

#Dodawanie produktu
def show_add_product_window(root):
    add_window = tk.Toplevel(root)
    add_window.title("Dodaj nowy produkt")
    add_window.geometry("400x300")
    add_window.configure(bg="#569b31")

    # Etykiety input
    tk.Label(add_window, text="Nazwa produktu:", bg="#569b31", fg="white").pack(pady=5)
    entry_name = tk.Entry(add_window)
    entry_name.pack()

    tk.Label(add_window, text="Cena:", bg="#569b31", fg="white").pack(pady=5)
    entry_price = tk.Entry(add_window)
    entry_price.pack()

    tk.Label(add_window, text="Ilość:", bg="#569b31", fg="white").pack(pady=5)
    entry_quantity = tk.Entry(add_window)
    entry_quantity.pack()

    tk.Label(add_window, text="Kategoria:", bg="#569b31", fg="white").pack(pady=5)
    entry_category = tk.Entry(add_window)
    entry_category.pack()

    # Przycisk dodaj
    tk.Button(
        add_window,
        text="Dodaj produkt",
        command=lambda: add_product(entry_name.get(), entry_price.get(), entry_quantity.get(), entry_category.get(),
                                    add_window),
        bg="#4CAF50", fg="white"
    ).pack(pady=20)

#Dodawanie do pliku
def add_product(name, price, quantity, category, window):
    try:
        if not name or not price or not quantity or not category:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione")
            return

        try:
            price = float(price)
            quantity = int(quantity)
        except ValueError:
            messagebox.showerror("Błąd", "Cena i ilość muszą być liczbami")
            return

        try:
            df = pd.read_excel("products.xlsx", engine="openpyxl")
            new_id = df['ID'].max() + 1
        except:
            df = pd.DataFrame(columns=['ID', 'Name', 'Price', 'Quantity', 'Category'])
            new_id = 1

        # Dodanie produktu
        new_product = {
            'ID': new_id,
            'Name': name,
            'Price': price,
            'Quantity': quantity,
            'Category': category
        }

        df = pd.concat([df, pd.DataFrame([new_product])], ignore_index=True)
        df.to_excel("products.xlsx", index=False)

        messagebox.showinfo("Sukces", "Produkt został dodany pomyślnie")
        window.destroy()
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")
