# Django React Combination
Single-page forum application built in ReactJS and Django Rest Framework.

## Frontend
> The frontend is a fast, interactive and simple Single-Page-Application (SPA), written in ES6 Javascript and built with following technologies:
> * [React v16](https://facebook.github.io/react/)
> * [Redux v4](http://redux.js.org/)
> * [React Router v4](https://github.com/ReactTraining/react-router)
> * [Redux Thunk v2](https://github.com/gaearon/redux-thunk)
> * [Redux Persist v5.9](https://github.com/rt2zz/redux-persist)



## Backend
> The backend is a scalable system that provides data through its RESTful API (browseable API available), written in Python and built with following technologies:
> * [Django v2.0](https://www.djangoproject.com/)
> * [Djangorestframework v3.7](http://www.django-rest-framework.org/)


## Installation

Make sure you have following software installed in your system:
* Python 3
* Node.js
* NPM / Yarn
* Git


Install all required dependencies in an isolated environment

```
cd ./backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Copy the `.env.example` as `.env` in `backend` folder
```
cp .env.example .env
```

Install all required dependencies for frontend in rengorum/frontend folder by typing
```
cd ../frontend
yarn
```

Copy the `.env.example` as `.env` in `frontend` folder
```
cp .env.example .env
```

## Running Backend on Local Server

Activate virtual environment

```
cd backend
source venv/bin/activate
```

(Optional) Run test
```
python manage.py test
```

Then run the server, api endpoint should be available on http://localhost:8000/api

```
python manage.py runserver
```

## Running Frontend on Local Server

Start development server

```
cd frontend
yarn start
```

Frontend should be available on http://localhost:3000/

### Test User
By default, the database for development server in `backend/db.sqlite3` is already filled with some data for ease of development. The superuser id is `irene` and password is `irene` as well.

If you want to start clean. Delete `db.sqlite3` and follow this step in `backend folder`
```py
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser
```
