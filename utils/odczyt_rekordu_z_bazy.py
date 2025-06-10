import os

import mysql.connector
import asyncio
import aiomysql
from dotenv import load_dotenv

load_dotenv()


# pip install aiomysql
async def get_connection():
    conn = await aiomysql.connect(
        host=os.getenv("DB_HOST"),
        port=int(os.getenv("DB_PORT")),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        db=os.getenv("DB_NAME")
    )
    return conn


# Konfiguracja bazy
async def get_random_fiszka():
    conn = await get_connection()

    # conn = await aiomysql.connect(**config)
    async with conn.cursor() as cursor:
        await cursor.execute("SELECT pytanie, odpowiedz FROM fiszki ORDER BY RAND() LIMIT 1")
        row = await cursor.fetchone()
    conn.close()
    if row:
        return {"question": row[0], "answer": row[1]}
    else:
        return None


# Możesz zostawić to do testowania (nie przeszkadza importom)
if __name__ == "__main__":
    async def test():
        wynik = await get_random_fiszka()
        print(wynik)


    asyncio.run(test())

if __name__ == '__main__':
    # Uruchomienie funkcji
    asyncio.run(get_random_fiszka())
