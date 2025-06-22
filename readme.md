Super! Twoja lista pokazuje, że masz dwa aktywne pliki konfiguracyjne Nginx:
	•	/etc/nginx/sites-enabled/default  (symlink do /etc/nginx/sites-available/default)
	•	/etc/nginx/sites-enabled/naukajava.online  (symlink do /etc/nginx/sites-available/naukajava.online)

To oznacza, że możesz edytować którykolwiek z tych plików (najlepiej ten, który obsługuje odpowiednią domenę lub port).

⸻

Co dalej zrobić?
	1.	Zdecyduj, który plik edytować:
	•	Jeśli chcesz dodać proxy np. dla domeny naukajava.online, edytuj:

/etc/nginx/sites-available/naukajava.online


	•	Jeśli chcesz dodać coś na “domyślny” serwer (np. dla adresów IP), edytuj:

/etc/nginx/sites-available/default


	2.	Otwórz plik w edytorze:

nano /etc/nginx/sites-available/naukajava.online
# lub
nano /etc/nginx/sites-available/default


	3.	Znajdź sekcję server { ... } i dodaj (lub zmień) np. taką sekcję reverse proxy:

server {
    listen 8001;
    listen [::]:8001;
    server_name naukajava.online;

    location / {
        proxy_pass http://127.0.0.1:8001;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
    }
}

Uwaga:
Jeśli chcesz, aby domena pod portem 8001 była widoczna po IPv6, kluczowe są linie:

listen 8001;
listen [::]:8001;


	4.	Po edycji sprawdź konfigurację:

sudo nginx -t


	5.	I przeładuj nginx:

sudo systemctl reload nginx



⸻

Chcesz sprawdzić aktualną zawartość pliku?
Wklej tu fragment z server { ... }, a powiem Ci, gdzie dokładnie dodać ustawienia dla nowego portu lub proxy!

⸻

Podsumowanie:
	•	Edytujesz plik z /etc/nginx/sites-available/
	•	Upewniasz się, że masz odpowiednie wpisy listen dla IPv4 i IPv6
	•	Dodajesz/zamieniasz sekcję proxy_pass dla portu 8001

Jeśli potrzebujesz konkretnego przykładu pod swoją domenę lub sytuację – daj znać!