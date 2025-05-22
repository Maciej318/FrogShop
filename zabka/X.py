import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def usun_produkt(koszyk_listbox):
    liczba_elementow = koszyk_listbox.size()

    if liczba_elementow == 0:
        messagebox.showinfo("Koszyk pusty", "Brak produktów do usunięcia.")
    else:
        koszyk_listbox.delete(tk.END)
