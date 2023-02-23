# restfulapi-with-tests

## Architecture du projet

```
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   └── server/
│       ├── __init__.py
│       ├── app.py
│       ├── database.py
│       ├── models/
│       │    └── student.py
│       ├── routes/
│       │    └── student.py
│       └── templates/
│            ├── home.hmtl
│            ├── test.hmtl
│            ├── 404.hmtl
│            └── 500.hmtl
│
├── requirements.txt
│
├── public/
│   ├── assets/
│   │    ├── styles.css
│   │    └── hightlightjs-dark.css
│   │
│   ├── js/
│   │    └── script.js
│   │
│   └── static/
│         └── images/
│              ├── logo.png
│              └── postman-icon.webp
│
├── test/
│    └── unit/
│         └── app/
│              ├── __init__.py
│              └── api_test.py
│
├── json/
│    └── data.json
```

## Pré-requis

Vous avez besoin de MongoBD pour faire marcher cette API. Une fois le serveur FastAPI lancé, la database va se créer et se remplir toute seule.

## Installation

Exécuter cette commande afin d'avoir toutes les librairies utilise :
```bash
pip install -r requirements.txt
```

## Utilisation

Enfin l'installation finit, vous devez exécuter cette commande pour lancer le serveur :

```python
python app/main.py
```

Rendez-vous sur le site une fois le serveur lancée a fin de voir les requêtes possibles à faire avec leur données à donner

```link
http://127.0.0.1:8000/
```

## Unit-Test

Pour executer les tests de l'api, suivez les intructions suivantes :

```bash
cd test/unit/app
python -m unittest -v api_test
```