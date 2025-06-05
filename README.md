
# Vibe Check App

A real-time web app that lets users take a short quiz to check their current vibe. Built using Django, Django Channels, HTML/CSS/JS, and deployed on Render.

---

## Features

- A 4–5 question quiz to analyze your vibe
- Real-time result updates using Django Channels (WebSockets)
- Simple, responsive frontend with HTML, CSS, and JavaScript
- Live deployment using Daphne + ASGI on Render
- Shareable frontend experience

---

## Tech Stack

- Backend: Django, Django Channels, Daphne
- Frontend: HTML, CSS, JavaScript
- Real-time: WebSockets
- Deployment: Render.com (Free Web Service)
- Version Control: Git + GitHub

---

## How to Run Locally

1. Clone the repository

```
git clone https://github.com/<your-username>/vibechek.git
cd vibechek
```

2. Create a virtual environment

```
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

3. Install dependencies

```
pip install -r requirements.txt
```

4. Run migrations

```
python manage.py migrate
```

5. Run the development server

```
python manage.py runserver
```

6. To enable WebSockets (real-time support), run using Daphne:

```
daphne vibechek.asgi:application
```

---

## Deployment on Render

1. Push code to GitHub.
2. Create a **Web Service** on Render.
3. Set the **Start Command**:

```
daphne -b 0.0.0.0 -p $PORT vibechek.asgi:application
```

4. Add environment variables:

```
DEBUG=False
SECRET_KEY=<your-secret-key>
ALLOWED_HOSTS=vibechek.onrender.com
```

5. Make sure the `requirements.txt` and `asgi.py` files are present.

---

## Project Structure

```
vibechek/
├── vibechek/              # Django project root
│   ├── asgi.py
│   ├── settings.py
│   └── urls.py
├── core/                  # Main app
│   ├── consumers.py
│   ├── views.py
│   ├── templates/
│   ├── static/
│   └── routing.py
├── requirements.txt
└── README.md
```

---

## Screenshots

(Add screenshots or demo video link here)

---

## Contributing

Pull requests are welcome. Fork the repository and submit your improvements.

---

## License

MIT License

---

## Live Demo

https://vibechek.onrender.com
