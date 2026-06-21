# Landing Page

Make a Landing Page for your Business with Django and Postgres.

## 📦 Screenshots:

<img src="https://github.com/Arvind-4/Landing-Page-in-Django/blob/main/.github/static/homepage.png?raw=true" alt="Home Page" />

## 📦 Tech Stack:

- [Django](https://www.djangoproject.com) - Django makes it easier to build better web apps more quickly and with less code.
- [Bootstrap](https://getbootstrap.com/) - Build fast, responsive sites with Bootstrap.
- [Postgres](https://www.postgresql.org/) - The World's Most Advanced Open Source Relational Database.

Deployed on [Vercel](https://vercel.com/). <br/>
Click Here for [Live Preview.](https://landing-django.vercel.app/)

## Deploy Now:

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/Arvind-4/Landing-Page-in-Django)

## Getting Started:

- Clone Repo

```bash
cd /path/to/folder
mkdir landing
cd landing
git clone https://github.com/Arvind-4/Landing-Page-in-Django.git .
```

- Create a Virtual Environment

```bash
pip3 install virtualenv
cd landing
python3.9 -m virtualenv .
source bin/activate
```

**For Windows use:** `.\Scripts\activate`

- Install Dependencies

```bash
pip install -r requirements.txt
```

Add Your Environment variable to `.env`.
Refer `.sample.env` file.

- Make Migrations

```bash
cd /path/to/folder/landing
python manage.py makemigrations
python manage.py migrate
```

- Run Dev Server

```bash
python manage.py runserver localhost:8000
```

Open [localhost:8000](http://localhost:8000/) in Browser.

## License

This Project is [MIT Licensed](https://github.com/Arvind-4/Landing-Page-in-Django/blob/main/LICENSE).

## Change Log

[Logs](https://github.com/Arvind-4/Landing-Page-in-Django/commits/main)
