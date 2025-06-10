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
    "port": int(os.getenv("DB_PORT"))
}

# Połącz z bazą
conn = mysql.connector.connect(**config)
cursor = conn.cursor()

create = """ 
CREATE TABLE fiszki (
 id INT AUTO_INCREMENT PRIMARY KEY,
 pytanie TEXT,
 odpowiedz TEXT
);
"""

cursor.execute(create)
conn.commit()
print("Tabela została utworzona!")

cursor.close()
conn.close()
