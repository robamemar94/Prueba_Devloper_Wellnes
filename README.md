### Microframework Web

- **Flask**

### Base de datos

- **Flask-SQLAlchemy**: ORM

### API Rest

- **Flask-restful**: Para ayudar con las peticiones.
- **Flask-JWT**: Identificación básica.
- **Flask-marshmallow**: Convertirá los objetos ORM en JSON.
- **Flask-caching**. Caché para las consultas.


### Instalación

```
$ git clone <Project A>  # Cloning project repository
```
```
$ cd <Project A> # Enter to project directory
```
```
$ python3 -m venv my_venv # If not created, creating virtualenv
```
```
$ source ./my_venv/bin/activate # Activating virtualenv
```
```
(my_venv)$ pip3 install -r ./requirements.txt # Installing dependencies
```

### Ejecución

```bash

pipenv run python3 app.py
```

## Peticiones

### GET

```bash
http GET localhost:5000/api/actual-status
```

```bash
http GET localhost:5000/api/actual-reactive-month
```

```bash
http GET localhost:5000/api/actual-power-month
```

```bash
http GET localhost:5000/api/power-series/<init_date>/<final_date>
```

```bash
http GET localhost:5000/api/daily-power/<init_date>/<final_date>
```

