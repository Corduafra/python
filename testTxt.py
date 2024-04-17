import os
from openpyxl import Workbook

# Definisci la cartella contenente i file .txt
cartella = 'C:\\Users\\Francesco\\Desktop\\chekerCpu\\'

# Lista dei file nella cartella
files = os.listdir(cartella)

# Inizializza una lista vuota per memorizzare tutte le righe
all_rows = []

# Itera attraverso ciascun file nella cartella
for file in files:
    if file.endswith('.txt'):  # Assicurati che il file sia un file .txt
        file_path = os.path.join(cartella, file)  # Percorso completo del file
        try:
            # Apre il file .txt in modalità di lettura
            with open(file_path, 'r', encoding='UTF-16-LE') as f:
                # Legge ciascuna riga del file
                for line in f:
                    # Suddivide la riga in base agli spazi e/o tabulazioni
                    row = line.strip().split()
                    # Aggiunge la riga alla lista di tutte le righe
                    all_rows.append(row)
        except Exception as e:
            print(f"Errore durante la lettura del file {file}: {e}")

# Crea un nuovo file Excel e aggiungi i dati
excel_file_path = 'output.xlsx'
try:
    # Crea un nuovo foglio di lavoro Excel
    wb = Workbook()
    ws = wb.active

    # Aggiungi i dati al foglio di lavoro Excel
    for row in all_rows:
        ws.append(row)

    # Salva il foglio di lavoro Excel
    wb.save(excel_file_path)
    print("Dati scritti con successo su", excel_file_path)
except Exception as e:
    print("Errore durante la scrittura su file Excel:", e)

# Apre il file Excel con l'applicazione predefinita
try:
    os.system("start excel.exe {}".format(excel_file_path))
except Exception as e:
    print("Errore durante l'apertura del file Excel:", e)
