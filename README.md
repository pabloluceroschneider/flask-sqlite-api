<div align="center">
  <h1 align="center">Flask Sqlite API</h1>
  
  <img height="130" src="https://github.com/pabloluceroschneider/flask-sqlite-api/assets/43233080/b479adbd-cf7a-42b4-bc09-e2375f376114" alt="tech" />  
</div>
<hr/>

## 📃 Description

I built this project following [this freecodecamp tutorial](https://youtu.be/74NW-84BqbA?si=iniSY8VVZaj4otWT) and [this blog](https://medium.com/@yahiaqous/how-to-build-a-crud-api-using-python-flask-and-sqlalchemy-orm-with-postgresql-7869517f8930)

## ⚙️ Set up

### Virtual environment

Create venv

```bash
python3 -m venv venv
```

Activate venv

```bash
source venv/bin/activate
```

### Install the dependencies

```bash
pip install -r src/requirements.txt
```

### DB Setup

Run this commands one by one

```bash
cd src
flask db init
flask db migrate
flask db upgrade
```

### Run the server

```bash
flask run
```

Watch for changes

```bash
FLASK_DEBUG=1 flask run
```
