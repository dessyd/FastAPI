# FastAPI

## FastAPI details

### Training References

- YouTube link: <https://www.youtube.com/watch?v=0sOvCWFmrtA>
- Repo: <https://github.com/Sanjeev-Thiyagarajan/fastapi-course.git>

### Packages Used

- FastAPI doc: <https://fastapi.tiangolo.com/tutorial/> and: <https://fastapi.tiangolo.com/tutorial/sql-databases/>
- CORS: <https://fastapi.tiangolo.com/tutorial/cors/>
- JWT Decoder: <https://jwt.io/>
- Postgres Tutorial : <https://www.postgresqltutorial.com/install-postgresql-linux/>
- SQLAlchemy doc: <https://docs.sqlalchemy.org/en/14/>
- Alembic: <https://alembic.sqlalchemy.org/en/latest/tutorial.html>
- Heroku: <https://devcenter.heroku.com/articles/getting-started-with-python>

### Local Setup

```bash
# Create virtual environment
python3 -m venv .venv
# Activate it
source .venv/bin/activate
# make sure pip is up to date
pip install --upgrade pip
# install project's requirements
pip install -r requirements.txt
# install Git pre-commit hooks
pre-commit install
# Have a first run
pre-commit run --all-files
# start database engine
docker compose up -d
# Initialize alembic file structure
alembic init alembic
# copy the project ini file
cp app/alembic.env.py alembic/env.py
# Autogenerate the database schema creation file
alembic revision --autogenerate -m "Application schema"
# Execute the schema creation
alembic upgrade head
# Start Web server:
uvicorn app.main:app --reload
```

## Heroku setup

```bash
# heroku login via cli
# Email: your email
# Password: heroku generated token
heroku login -i
# Create app with global name. Only do this once
heroku apps:create fastapi-dessyd
# push content to herou
git push heroku main
# Access the app
# go to https://fastapi-dessyd.herokuapp.com/

# Add postgres
heroku addons:create heroku-postgresql:hobby-dev
```

## Environment variables

All environment variables are stored in a `.env` file having the following structure:

```bash
# DB section
DATABASE_DRIVER=postgresql
DATABASE_HOSTNAME=<target host>
DATABASE_PORT=5432
DATABASE_NAME=<DB name>

DATABASE_USERNAME=<db user>
DATABASE_PASSWORD=<db password

# oauth section
# to get a SECRET_KEY string run:
# openssl rand -hex 32
SECRET_KEY=<oauth session secret key>
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
```

## Ubuntu

Set environment from .env syntax ( no export)

```bash
set -o allexport; source ~/.env ; set +o allexport
```

## OpenAPI

In oder to generate the OpenAPI description file `openapi.json`issue the following:

```bash
wget http://localhost:8000/openapi.json
# Optional add it to the repo
git add openapi.json
```

---
