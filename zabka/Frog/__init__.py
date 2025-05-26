import os
import pandas as pd
from tkinter import messagebox
from datetime import datetime
import random


BASE_DIR = os.path.dirname(__file__)
database_dir = os.path.join(BASE_DIR, 'DATABASE')

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
        delete_window : Okno usuwania produktu
        
    Returns: 
        Otwiera okno do usuwania produktu
        zwraca błąd w przypadku podania złego id produktu
        jeżeli id poprwane usuwa produkt o podanym ID z pliku Excel 
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
        window : Okno dodawania produktu
        
    Returns: 
        Otwiera okno do dodania produktu
        wyświetla błąd jeżeli nie wypełniono każdego pola 
        dodaje produkt o podanych zmiennych do pliku Excel 
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

"""
    Dodawanie nowego użytkownika do pliku csv 
    
    Args:
        name(str) : Nazwa użytkownika
        email(str) : Email użytkownika
        number(int) : Numer telefonu użytkownika
        window : Okno dodania użytkownika
        
    Returns: 
        Otwiera okno do dodania użytkownika
        zwraca błąd jeżeli nie podano wszystkich pól lub jeżeli nr telefonu nie jest liczbą
        dodaje podanego użytkownika do pliku csv 
"""
def add_customer(name,email,number, window):
    created = datetime.now().strftime("%d/%m/%Y %H:%M")
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
            while True:
                new_id = random.randint(1000, 9999)
                if new_id not in customers['ID'].values:
                    break
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

        filename = f"{new_id}.txt"
        file_path = os.path.join(database_dir, filename)
        with open(file_path, "w"):
            pass

        messagebox.showinfo("Sukces", "Użytkownik został dodany pomyślnie")
        window.destroy()

    except Exception as e:
        messagebox.showerror("Błąd", f"Wystąpił błąd: {str(e)}")

"""
    Usuwanie użytkownika z pliku csv 
    
    Args:
        customer_name(str) : Nazwa użytkownika
        delete_window : Okno do usuwania użytkownika
        
    :Returns: 
        Otwiera okno do usuwania użytkownika
        jeżeli nie istnieje użytkownik o podanej nazwie lub puste pole wypisze błąd
        usuwa użytkownika z pliku csv
        
"""
def delete_customer(customer_name, delete_window):
    try:
        if not customer_name:
            messagebox.showerror("Błąd", "Musisz podać nazwe użytkownika")
            return

        customers = get_customers()
        customer_name = str(customer_name)
        customer_id = customers[customers["NAME"] == customer_name]["ID"].values[0]

        if customer_name not in customers["NAME"].values:
            messagebox.showerror("Błąd", "Nie ma użytkownika o takiej nazwie")
            return

        customers = customers[customers["NAME"] != customer_name]
        customers.to_csv("Frog/customer.csv", index=False)

        filename = f"{customer_id}.txt"
        file_path = os.path.join(database_dir, filename)

        if os.path.exists(file_path):
            os.remove(file_path)

        messagebox.showinfo("Sukces",f"Użytkownik {customer_name} został usunięty ")
        delete_window.destroy()

    except Exception as e:
        messagebox.showerror("Błąd",f"{e}")

""" 
    Zmiana danych użytkownika
    
    Args:
        name(str) : Nazwa użytkownika
        id(int) : ID użytkownika
        email(str) : Email użytkownika
        number(int) : Numer użytkownika
        window : Okno do zmiany danych użytkownika
    
    Returns: Użytkownik podaje Id użytkownika dla którego chce zmienić dane,
    i wpisuje na co chce zmienić podane dane.
    
"""
def update_customer(id ,name, email, number, window):

    try:
        customers = get_customers()

        try:
            id = int(id)
        except ValueError:
            messagebox.showerror("Error", "ID musi być liczbą")
            return

        if id not in customers["ID"].values:
            messagebox.showerror("Error", "Użytkownik o podanym id nie istnieje")
            return

        if not name and not email and not number:
            messagebox.showerror("Błąd", "Przynajmniej jedno pole musi być wypełnione")
            return False

        updated = datetime.now().strftime("%d/%m/%Y %H:%M")
        idx = customers[customers["ID"] == id].index[0]

        if name: customers.at[idx,"NAME"] = name
        if email: customers.at[idx,"E-MAIL"] = email

        if number:
            try:
                customers.at[idx,"PHONE"] = int(number)
            except ValueError:
                messagebox.showerror("Błąd", "Numer telefonu musi być liczbą")
                return

        customers.at[idx,"UPDATED"] = updated

        customers.to_csv("Frog/customer.csv",index = False)
        messagebox.showinfo("Sukces","Dane użytkownika zostały zaktualizowane")

        window.destroy()

    except Exception as e:
        messagebox.showerror("Error", f"Wystąpił błąd podczas aktualizacji {str(e)}")







