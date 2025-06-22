# app.py
import asyncio

from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import random
from utils.odczyt_rekordu_z_bazy import get_random_fiszka

# pip install python-dotenv
app = FastAPI()

# Konfiguracja ścieżki do szablonów HTML
templates = Jinja2Templates(directory="templates")


# Funkcja odczytująca fiszki z pliku tekstowego
def load_fiszki(filename):
    fiszki = []
    with open(filename, encoding='utf-8') as file:
        lines = file.readlines()
        # Zakładamy, że każda pierwsza linia to pytanie, a druga to odpowiedź
        for i in range(0, len(lines), 2):
            question = lines[i].strip()
            answer = lines[i + 1].strip() if i + 1 < len(lines) else "Brak odpowiedzi"
            fiszki.append({"question": question, "answer": answer})
    return fiszki


fiszki = load_fiszki("pytania.txt")


@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    # fiszka = random.choice(fiszki)
    fiszka = await get_random_fiszka()
    return templates.TemplateResponse("index.html", {"request": request, "fiszka": fiszka})
# uvicorn app:app --reload
# pip install fastapi uvicorn jinja2
# uvicorn app:app --host 0.0.0.0 --port 8000
# https://fiszkipythonfastapi.onrender.com/?
# http://frog02.mikr.us:42324/?
# https://frog02-42324.wykr.es
# sudo uvicorn app:app --host :: --port 80
# nc -vz serwer2348480.home.pl 3380