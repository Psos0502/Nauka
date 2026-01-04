## Wymagania
- Python 3.10+

## Instalacja i uruchomienie

git clone https://github.com/Psos0502/Nauka.git
cd Nauka (Przejdź do folderu w którym znajdziesz core/manage.py/requirements.txt/)
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver

Aplikacja powinna być dostępna pod adresem
http://127.0.0.1:8000/

STRUKTURA PROJEKTU

Nauka/
├── core/
│   ├── views.py
│   ├── urls.py
│   └── templates/
├── manage.py
├── requirements.txt
└── README.md
