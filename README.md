# Serverless Task Management System (AWS Cloud) ☁️

Ten projekt to w pełni funkcjonalna, serwerlessowa aplikacja chmurowa zbudowana na platformie AWS. Służy jako interaktywna baza 150 zadań z wbudowanym systemem progresji użytkownika (zdobywanie poziomów). 

Projekt został zrealizowany w ramach wdrożenia nowoczesnych praktyk **Cloud & DevOps**, z naciskiem na architekturę "Infrastruktura jako Kod" (IaC) oraz pełną automatyzację CI/CD.

🔗 **[Zobacz działającą aplikację]http://moje-chmurowe-zadania-2026-wojtek.s3-website.eu-north-1.amazonaws.com**

---

## 🏗️ Architektura Systemu

Aplikacja opiera się na rozproszonej architekturze Serverless:

1. **Frontend (Amazon S3):** Statyczna strona WWW (HTML/JS) hostowana w usłudze S3, zapewniająca wysoką dostępność i skalowalność od strony klienta.
2. **Routing (Amazon API Gateway):** Punkt wejścia dla zapytań z frontendu. Zarządza ruchem HTTP (metody GET dla pobierania zadań, POST dla awansu na wyższy poziom) i przekazuje je do warstwy obliczeniowej.
3. **Backend / Logika (AWS Lambda):** Bezserwerowe funkcje napisane w języku **Python 3.9**. Odpowiadają za weryfikację logiki biznesowej, bezpieczne przeliczanie poziomów i komunikację z bazą danych.
4. **Baza Danych (Amazon DynamoDB):** Nierelacyjna baza danych NoSQL. Bezpiecznie przechowuje pulę 150 ustrukturyzowanych zadań oraz aktualny stan konta użytkownika.

---

## 🛠️ Wykorzystane Technologie

* **Chmura publiczna:** Amazon Web Services (AWS)
* **Infrastruktura jako Kod (IaC):** AWS Serverless Application Model (AWS SAM) / CloudFormation
* **Język Backend-u:** Python (boto3)
* **Język Frontend-u:** HTML, CSS, Vanilla JavaScript
* **CI/CD:** GitHub Actions
* **Kontrola Wersji:** Git / GitHub

---

## ⚙️ Automatyzacja (CI/CD)

Projekt posiada wdrożony potok CI/CD za pomocą **GitHub Actions**. 
Każdy *push* do gałęzi `main` automatycznie uruchamia proces, który:
1. Autoryzuje bezpieczne połączenie z AWS przy użyciu poświadczeń zapisanych w GitHub Secrets.
2. Synchronizuje i aktualizuje najnowszą wersję frontendu w publicznym buckecie S3.
Dzięki temu każda zmiana w kodzie aplikacji jest widoczna na produkcji w kilkanaście sekund, bez konieczności ręcznej ingerencji.

---

## 🚀 Instalacja i Wdrożenie (Dla programistów)

Cała infrastruktura jest zarządzana przez kod. Aby wdrożyć kopię tego systemu na własnym koncie AWS:

1. Sklonuj repozytorium: `git clone <adres-repozytorium>`
2. Zbuduj aplikację za pomocą SAM CLI: `sam build`
3. Wdróż zasoby na konto AWS: `sam deploy --guided`
4. Uruchom skrypt ładujący 150 zadań do bazy DynamoDB: `python seed_database.py`
5. Zaktualizuj zmienną `API_URL` w pliku `index.html` adresem zwróconym przez instalator SAM.