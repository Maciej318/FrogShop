import os
import pandas as pd
from tkinter import messagebox
from datetime import datetime

BASE_DIR = os.path.dirname(__file__)

""" Pobiera dane produktow z pliku Excel """
def get_products():
    return pd.read_excel(os.path.join(BASE_DIR,"products.xlsx"), engine="openpyxl")

""" Pobiera dane uzytkownikow z pliku Excel """
def get_customers():
    return pd.read_csv(os.path.join(BASE_DIR, "customer.csv"),)


"""
    Usuwa produkt o podanym ID z pliku Excel 
    
    Args:
        product_id(str/int) : ID produktu do usuniecia
        delete_window : Zamkniecie okna po usunieciu produktu
"""
def delete_product(product_id, delete_window):
    try:
        if not product_id:
            messagebox.showerror("Błąd", "Musisz podać ID produktu")
            return

        data = get_products()
        product_id = int(product_id)

        if product_id not in data['ID'].values:
            messagebox.showerror("Błąd", "Nie ma produktu o tym ID")
            return

        data = data[data['ID'] != product_id]
        data.to_excel("Frog/products.xlsx", index=False)

        messagebox.showinfo("Sukces", "Produkt został usunięty")

        delete_window.destroy()



    except Exception as e:
        messagebox.showerror("Błąd", f"{e}")


"""
    Dodaje produkt o podany przez admina do pliku Excel 

    Args:
        name(str) : Nazwa produktu
        price(float) : Cena produktu
        quantity(int) : Ilosc produktu
        category(str) : Kategoria produktu 
        window : Zamkniecie okna po dodaniu produktu
"""

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
            data = get_products()
            new_id = data['ID'].max() + 1
        except:
            data = pd.DataFrame(columns=['ID', 'Name', 'Price', 'Quantity', 'Category'])
            new_id = 1

        # Dodanie produktu
        new_product = {
            'ID': new_id,
            'Name': name,
            'Price': price,
            'Quantity': quantity,
            'Category': category
        }

        data = pd.concat([data, pd.DataFrame([new_product])], ignore_index=True)
        data.to_excel("Frog/products.xlsx", index=False)

        messagebox.showinfo("Sukces", "Produkt został dodany pomyślnie")
        window.destroy()
    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")


def add_customer(name,email,number, window):
    created = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    updated = None
    try:
        if not name or not email or not number:
            messagebox.showerror("Błąd", "Wszystkie pola muszą być wypełnione")
            return

        try:
            number = int(number)
        except ValueError:
            messagebox.showerror("Błąd", "Numer telefonu musi być liczbą")
            return

        try:
            customers = get_customers()
            new_id = customers['ID'].max() + 1
        except:
            customers = pd.DataFrame(columns = ['ID', 'Name','E-MAIL','PHONE', 'CREATED', 'UPDATED'])
            new_id = 1

        # Dodanie użytkownika
        new_customer = {
            'ID': new_id,
            'NAME': name,
            'E-MAIL': email,
            'PHONE': number,
            'CREATED': created,
            'UPDATED': updated,
        }

        customers = pd.concat([customers, pd.DataFrame([new_customer])], ignore_index = True)
        customers.to_csv("Frog/customer.csv", index = False)

        messagebox.showinfo("Sukces", "Użytkownik został dodany pomyślnie")
        window.destroy()

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")


