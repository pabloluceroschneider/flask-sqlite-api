<div align="center">
  <h1 align="center">Flask Sqlite API</h1>
  
  <img height="130" src="https://github.com/pabloluceroschneider/flask-sqlite-api/assets/43233080/b479adbd-cf7a-42b4-bc09-e2375f376114" alt="tech" />  
</div>
<hr/>

## 📃 Description

This is a project that follows [this freecodecamp tutorial](https://youtu.be/74NW-84BqbA?si=iniSY8VVZaj4otWT).

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
flask db init
flask db migrate
flask db upgrade
```

### Run the server

```bash
cd src && flask run
```

Watch for changes

```bash
cd src && FLASK_DEBUG=1 flask run
```
