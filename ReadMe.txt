# FrogShop
Python project about polish shop named 'żabka'

Środowisko Technologiczne: Pycharm,
Język Programowania: Python (wersja 3.10+),
Biblioteki: Pandas, Pillow, openpyxl,
Środowisko Uruchomieniowe: Windows 10/11
Autorzy: Maciej Brzozowski, Kacper Breczko, Stanisław Chociej

Dokumentacja Systemu Sklepu Żabka
1. Ekran Logowania
Opis: Główny ekran umożliwiający logowanie do systemu jako administrator lub klient.

Elementy interfejsu:
Pole tekstowe:

Login – wprowadź nazwę użytkownika (dla klienta) lub admin (dla administratora).
Przyciski wyboru typu logowania:
Zaloguj jako Klient – przekierowuje do panelu użytkownika.
Zaloguj jako ADMIN – przekierowuje do panelu administratora (wymaga uprawnień).

2. Panel Administratora
Opis: Panel zarządzania sklepem dostępny po zalogowaniu jako administrator.

Funkcje:
Przycisk	        Opis
Pokaż produkty	    	-Wyświetla listę wszystkich produktów w sklepie.
Usuń produkt	      	-Usuwa wybrany produkt (po ID lub nazwie).
Dodaj produkt	      	-Otwiera formularz dodawania nowego produktu.
Użytkownicy	        -Przenosi do podsekcji zarządzania użytkownikami.
Wyloguj	            	-Wylogowuje administratora i wraca do ekranu logowania.

3. Panel Użytkowników (Administracja)
Opis: Sekcja zarządzania kontami użytkowników, dostępna z poziomu panelu administratora.

Funkcje:
Przycisk	        Opis
Pokaż użytkowników	-Wyświetla listę zarejestrowanych użytkowników.
Dodaj użytkownika	-Otwiera formularz rejestracji nowego użytkownika.
Usuń użytkownika	-Usuwa konto użytkownika (po ID).
Edytuj użytkownika	-Umożliwia modyfikację danych wybranego użytkownika.
Cofnij	             	-Powrót do głównego panelu administratora.

4. Interfejs Użytkownika (Koszyk i Produkty)

Elementy Interfejsu:
1. Górny pasek nawigacyjny:
"Witaj, [imię]!" – wyświetla nazwę zalogowanego użytkownika (np. Maciej).

Przycisk	      Opis
Historia              –pokazuje historię zakupów użytkownika (zapisane w pliku/systemie).
Wyloguj               –wylogowuje użytkownika i przekierowuje do ekranu logowania.

2. Tabela produktów:
Wyświetla liste dostępnych produktów

3. Koszyk:
Wyświetla produkty dodane przez użytkownika. Dla każdego produktu dostępne są przyciski:

Przycisk              Opis
Dodaj do koszyka      –dodaje wybrany produkt do koszyka.
Kup                   –finalizuje zakup, zapisuje dane transakcji (np. do pliku historii).
X                     –usuwa produkt z koszyka.

4. Filtrowanie kategorii:
Przycisk              Opis
Pole tekstowe         –umożliwia wpisanie nazwy kategorii (np. Napoje).
Filtruj               –pokazuje tylko produkty z wybranej kategorii.
Wyczyść filtr         –resetuje filtry i wyświetla wszystkie produkty.