## Prueba_Devloper_Wellnes

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

Desde la consola del sistema vamos a la ubicación donde queremos guardar el
 repositorio localmente y clonamos.
```
$ git clone https://github.com/robamemar94/Prueba_Devloper_Wellnes.git  
```
```
$ cd Prueba_Devloper_Wellnes 
```
```
$ python -m venv venv 
```
```
$ path_to_my_venv/venv/bin/activate # Activamos el VENV
```
```
(my_venv)$ pip install -r ./requirements.txt #instalamos los paquetes 
```

### Ejecución
En primer lugar cargaremos los datos del csv en la BBDD. Para ello
 ejecutamos el archivo build_database.py.
```
(my_venv)$ python app/build_database.py
```
Iniciamos la API mediante entrypoint.py.
```
(my_venv)$ python app/entrypoint.py
```

## Peticiones

Se han implementado las siguientes entradas a la API (en la imagen dashboard
.png se identifican dentro del mockup). 

* **actual-status:** Obtiene el estado actual (voltage, intensidad, potencia
 activa y
 reactiva y factor de potencia) del
 elemento a partir del último
 registro. 
```bash
http GET localhost:5000/api/actual-status
```
Esta entrada ha sido  protegida mediante token. Para acceder a ella debe
 realizarse la petición:
```
POST /auth HTTP/1.1
Host: localhost:5000
Content-Type: application/json

{
    "username": "user1",
    "password": "abcxyz"
}
```
Se obtiene el token para el acceso.
```
GET /api/actual-status HTTP/1.1
Authorization: jwt token-obtenido
```
* **actual-reactive-month:** Obtiene el valor de energía reactiva del mes en
 curso 
```bash
http GET localhost:5000/api/actual-reactive-month
```
* **actual-energy-month:** Obtiene el valor de energía activa del mes en
 curso 
```bash
http GET localhost:5000/api/actual-energy-month
```
* **power-series:** Obtiene los regitros quinceminutales de potencia entre las
 fechas
 indicadas:
 
    Formato de los parámetros fechas: %Y-%m-%d ej: 2019-08-24 
```bash
http GET localhost:5000/api/power-series/<init_date>/<final_date>
```
*** No se han implementado para el resto de variables, siendo la mecánica la
 misma. Variando la columna de interés en la consulta a la BBDD

* **daily-power:** Obtiene los regitros de energía consumida **diaria** entre
 las
 fechas indicadas:
 
     Formato de los parámetros fechas: %Y-%m-%d ej: 2019-08-24 
```bash
http GET localhost:5000/api/daily-power/<init_date>/<final_date>
```
*** No se han implementado para la energía reactiva como se observa en el
 mockup, pero su implentación sería la misma.

## Testing
Se ha creado el fichero test/test.py. Se realizan las pruebas unitarias
 de todas las  vistas creadas. Además del testeo del sistema de autentificación
  mediante tokens.
  
 
### Desiciones técnicas
Se ha estructurado con la siguiente estructura:
* api: Blueprint donde se guardan los módelos, esquemas y las
 funcionalidades para consultas a la bbdd.
* config:guarda el fichero de configuración.
* extension: guarda diferentes extensiones (bbdd, cache...).
* test: donde se realizan distintos test unitarios.

Los valores han sido almacenados en una base de datos relacional, en una
 modelo de
 tabla única (energía) con las diferentes variables.
 
 Se utiliza las librerías flask restful, para ayudar con las peticiones y
  flask-marsmallow para la serialización de los objetos ORM.

Se ha implementado un sistema de autentificación mediante JWT. Se ha
 protegido una de las vistas para ejemplificarlo. Para acceder a ella se ha
  creado el
  usuario
  ficticio, que permite obtener el token para esta vista:
  * username: user1
  * password: abcxyz
  
Se ha impementado un sistema de cache haciendo uso de la librería Flask
-caching.

## Siguientes pasos
* Mejora del sistema de autentificación, mediante un registro de usuarios en
 la BBDD.
 
 * Manejo de errores. Por ejemplo, no se ha implementado una solución para
  que te avise si los parámetros de una petición tienen un formato válido.
   