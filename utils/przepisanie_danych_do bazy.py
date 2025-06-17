import os

import mysql.connector
from dotenv import load_dotenv

load_dotenv()
# Konfiguracja bazy
config = {
    'host': os.getenv("DB_HOST"),
    'user': os.getenv("DB_USER"),
    'password': os.getenv("DB_PASSWORD"),
    'database': os.getenv("DB_NAME"),
    "port" : int(os.getenv("DB_PORT"))
}

# Połącz z bazą
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

# Otwórz plik z pytaniami i odpowiedziami
with open('../pytania2.txt', encoding='utf-8') as f:
    lines = [line.strip() for line in f if line.strip()]  # pomija puste linie

# Sprawdź, czy liczba wierszy jest parzysta
if len(lines) % 2 != 0:
    raise ValueError("Nieparzysta liczba linii – plik musi mieć pary pytanie-odpowiedź")

# Wstaw pytania i odpowiedzi do bazy
for i in range(0, len(lines), 2):
    pytanie = lines[i]
    odpowiedz = lines[i + 1]
    cursor.execute(
        "INSERT INTO fiszki (pytanie, odpowiedz) VALUES (%s, %s)",
        (pytanie, odpowiedz)
    )

# Zatwierdź i zamknij połączenie
conn.commit()
cursor.close()
conn.close()

print("Zakończono dodawanie fiszek do bazy.")
