import tkinter as tk
from tkinter import *
import random
import string

# Creazione della finestra principale
window = tk.Tk()
window.geometry("700x600")  # Dimensione finestra
window.title("Generatore by Sunaldo")  # Titolo della finestra
window.resizable(False, False)  # Disabilita la possibilità di ridimensionare la finestra

# Variabili per i checkbutton
var = tk.IntVar()  # Minuscole
var2 = tk.IntVar()  # Maiuscole
var3 = tk.IntVar()  # Numeri
var4 = tk.IntVar()  # Simboli

# Creazione delle liste di caratteri
minuscole = list(string.ascii_lowercase)  # Lista di lettere minuscole
maiuscole = list(string.ascii_uppercase)  # Lista di lettere maiuscole
numeri = list(string.digits)  # Lista di numeri
simboli = list(string.punctuation)  # Lista di simboli

# Configurazione delle colonne per l'allineamento degli elementi
window.grid_columnconfigure(0, weight=1)

# Funzione per la generazione della password
def creapass():
    # Ottieni la lunghezza della password dal campo di input
    lunghezza = int(lunghezzap.get())  
    password = []  # Lista che conterrà i caratteri della password
    l1 = l2 = l3 = l4 = 0  # Variabili di controllo per i checkbutton (minuscole, maiuscole, numeri, simboli)
    
    # Controlla se i checkbutton sono selezionati e aggiorna le variabili di controllo
    if var.get() == 0:
        print("Checkbutton minuscole non premuto")
    else:
        print("Checkbutton minuscole premuto")
        l1 = 1

    if var2.get() == 0:
        print("Checkbutton maiuscole non premuto")
    else:
        print("Checkbutton maiuscole premuto")
        l2 = 1
    
    if var3.get() == 0:
        print("Checkbutton numeri non premuto")
    else:
        print("Checkbutton numeri premuto")
        l3 = 1

    if var4.get() == 0:
        print("Checkbutton simboli non premuto")
    else:
        print("Checkbutton simboli premuto")
        l4 = 1

    # Inizializza il ciclo per la generazione della password
    i = 0
    while i < lunghezza:
        # Scegli un numero casuale tra 1 e 4 per determinare il tipo di carattere
        listasc = random.randint(1, 4)
        
        # Seleziona il tipo di carattere da aggiungere alla password
        match listasc:
            case 1:
                if l1 == 1:
                    password.append(random.choice(minuscole))  # Aggiungi una minuscola
                else:
                    i = i - 1  # Se non è selezionato, ripeti l'iterazione senza incrementare 'i'
            case 2:
                if l2 == 1:
                    password.append(random.choice(maiuscole))  # Aggiungi una maiuscola
                else:
                    i = i - 1
            case 3:
                if l3 == 1:
                    password.append(random.choice(numeri))  # Aggiungi un numero
                else:
                    i = i - 1
            case 4:
                if l4 == 1:
                    password.append(random.choice(simboli))  # Aggiungi un simbolo
                else:
                    i = i - 1
        i = i + 1  # Incrementa il contatore per uscire dal ciclo quando la lunghezza è raggiunta

    # Se la password è stata generata, visualizzala nel campo di output
    if password:
        password_text.set("".join(password))  # Imposta il testo nel campo di input "readonly"

# Creazione di etichette e campi di input per l'interfaccia grafica
benvenuto = tk.Label(window, text="Ciao, benvenuto in crea password", padx=10, font=("helvetica", 25))
benvenuto.grid(row=0, column=0, sticky="N", pady=10)

lunghezza = tk.Label(window, text="Inserisci la lunghezza della password", padx=10, font=("helvetica", 20))
lunghezza.grid(row=1, column=0, pady=10)

lunghezzap = tk.Entry()  # Campo di input per la lunghezza della password
lunghezzap.grid(row=2, column=0, padx=10)

selezione = tk.Label(window, text="Scegli i campi da attivare", padx=10, font=("helvetica", 20))
selezione.grid(row=3, column=0, pady=10)

# Checkbutton per selezionare le opzioni
R1 = tk.Checkbutton(window, text="Minuscole", variable=var, font=("helvetica", 15))
R1.grid(row=4, column=0, pady=10)

R2 = tk.Checkbutton(window, text="Maiuscole", variable=var2, font=("helvetica", 15))
R2.grid(row=5, column=0, pady=10)

R3 = tk.Checkbutton(window, text="Numeri", variable=var3, font=("helvetica", 15))
R3.grid(row=6, column=0, pady=10)

R4 = tk.Checkbutton(window, text="Simboli", variable=var4, font=("helvetica", 15))
R4.grid(row=7, column=0, pady=10)

# Campo di output per visualizzare la password generata
password_text = tk.StringVar()
password_entry = tk.Entry(window, textvariable=password_text, font=("helvetica", 15), state="readonly", width=30)
password_entry.grid(row=10, column=0, pady=10)

# Pulsante per avviare la generazione della password
invio = tk.Button(text="INVIO", padx=10, font=("helvetica", 15), command=creapass)
invio.grid(row=9, column=0, pady=10, padx=10)

# Avvio della finestra
window.mainloop()
