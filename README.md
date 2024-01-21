<div align="center">
  <h1 align="center">Flask Sqlite API</h1>
  
  <img height="130" src="https://github.com/pabloluceroschneider/flask-sqlite-api/assets/43233080/b479adbd-cf7a-42b4-bc09-e2375f376114" alt="tech" />  
</div>
<hr/>

## 📃 Description

This is a project that follows [this freecodecamp tutorial](https://youtu.be/74NW-84BqbA?si=iniSY8VVZaj4otWT).

## ⚙️ Set up

### Activate the virtual environment

Run the following command:

```bash
python3 -m venv venv
. venv/bin/activate
```

### Install the dependencies

```bash
pip install -r requirements.txt
```

### Set up the DB

```bash
python3
from server import app, db
app.app_context().push()
db.create_all()
exit()
```

### Run the server

```bash
python3 .
```
