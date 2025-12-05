## 🛸 **Challenge Back-End – LQN**

### **API GraphQL en Django para fanáticos de Star Wars**

Este proyecto consiste en construir una **API GraphQL** utilizando **Django** y **Graphene**, proporcionando información relevante del universo de **Star Wars**.
El objetivo es exponer un endpoint que permita consultar personajes, planetas y peliculas claves de esta saga.

---

## 🎯 **Objetivo del proyecto**

Desarrollar una API GraphQL funcional que:

- Exponga datos relacionados con el universo de Star Wars.
- Permita realizar consultas y mutaciones según los requerimientos.
- Siga buenas prácticas de arquitectura, seguridad y manejo de dependencias.
- Sea fácil de instalar, ejecutar y extender.

---

## 🧩 **Tecnologías utilizadas**

- **Python 3.10+**
- **Django 4+**
- **Graphene-Django**
- **SQLite / PostgreSQL** (según preferencia)
- **Virtualenv / Pipenv**
- **Pytest**
- **Docker** (opcional)

---

## 📁 **Estructura del proyecto**

```
project/
│── ChallengeBackEndLQN/
│   ├── settings.py
│   ├── settings_test.py
│   ├── urls.py
│   └── ...
│── docker-prod/
│   └── docker-compose.yml
│── staticfiles/
│── apps/
│   │
│   ├── character/
│   │   ├── models/
│   │   │   └── character.py
│   │   ├── tests/
│   │   │   ├── test_character_graphql.py
│   │   │   └── test_character_model.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── schema.py
│   │
│   ├── core/
│   │   ├── models/
│   │   │   └── base_model.py
│   │   ├── apps.py
│   │   └── schema.py
│   │
│   ├── film/
│   │   ├── models/
│   │   │   └── film.py
│   │   ├── tests/
│   │   │   ├── test_film_graphql.py
│   │   │   └── test_film_model.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   └── schema.py
│   │
│   └── planet/
│       ├── models/
│       │   └── planet.py
│       ├── tests/
│       │   ├── test_planet_graphql.py
│       │   └── test_planet_model.py
│       ├── admin.py
│       ├── apps.py
│       └── schema.py
│── requirements.txt
│── Dockerfile
│── gunicorn_config.py
│── manage.py
│── README.md
```

---

## 🚀 **Cómo ejecutar el proyecto**

### 1️⃣ Clonar el repositorio

```bash
git clone https://github.com/fabioCordoba/ChallengeBackEndLQN.git
cd lqn-challenge-backend
```

### 2️⃣ Crear y activar entorno virtual

```bash
python -m venv env
source env/bin/activate  # Linux/Mac
env\Scripts\activate     # Windows
```

### 3️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4️⃣ Realizar migraciones

```bash
python manage.py migrate
```

### 5️⃣ Ejecutar el servidor

```bash
python manage.py runserver
```

## Levanta el proyecto usando Docker

## Requisitos previos

- [Docker](https://www.docker.com/get-started) instalado
- [Docker Compose](https://docs.docker.com/compose/install/) instalado

---

## 1. Clonar el repositorio

```bash
git clone https://github.com/fabioCordoba/ChallengeBackEndLQN.git
cd ChallengeBackEndLQN
```

---

## 2. Crear archivo `.env`

Copia el ejemplo y ajusta los valores según tu entorno:

```bash
cp .env.example .env
```

Variables típicas:

```
DEBUG=True
SECRET_KEY=tu_secreto_aqui
POSTGRES_DB=starwars
POSTGRES_USER=usuario
POSTGRES_PASSWORD=contraseña
DB_HOST=db
DB_PORT=5432
```

---

## 3. Levantar los contenedores

```bash
docker-compose up -d --build
```

Esto hará:

- Crear contenedores de Django
- Instalar dependencias
- Ejecutar migraciones iniciales

---

## 4. Ejecutar migraciones

```bash
docker-compose exec web python manage.py migrate
```

Opcional: crear superusuario

```bash
docker-compose exec web python manage.py createsuperuser
```

---

## 5. Acceder al proyecto

- API GraphQL: [http://localhost:8000/graphql](http://localhost:8000/graphql)
- Admin Django: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 6. Comandos útiles

- Ver logs de los contenedores:

```bash
docker-compose logs -f
```

- Detener contenedores:

```bash
docker-compose down
```

- Reiniciar contenedores:

```bash
docker-compose restart
```

---

## 7. Notas

- Asegúrate de que los puertos `8000` (Django) y `5432` (PostgreSQL) estén libres en tu máquina.
- Para desarrollo, `DEBUG=True` está habilitado. Para producción, configurar variables de entorno adecuadas.

Con esto, el proyecto debería estar listo para correr localmente usando Docker.

---

## 8. Ejecutar tests

El proyecto incluye **tests para modelos y GraphQL**. Para correrlos dentro del contenedor Docker:

### 8.1 Ejecutar todos los tests

```bash
docker-compose exec web python manage.py test
```

Si quieres ejecutar todos los test, sin usar docker

```bash
pytest --ds=ChallengeBackEndLQN.settings_test
```

Esto ejecutará todos los tests de las apps (`character`, `planet`, `film`) incluyendo:

- Tests de modelos (`tests/test_<modelo>_model.py`)
- Tests de GraphQL (`tests/test_<modelo>_graphql.py`)

---

### 8.2 Ejecutar tests específicos de una app

Por ejemplo, solo los tests de `character`:

```bash
docker-compose exec web python manage.py test apps.character
```

---

### 8.3 Ejecutar un test específico

```bash
docker-compose exec web python manage.py test apps.character.tests.test_character_graphql.TestCharacterQueries
```

---

### Notas

- Los tests se ejecutan en el entorno del contenedor, por lo que no necesitas instalar dependencias localmente.
- Se recomienda ejecutar los tests después de hacer migraciones o agregar nuevas funcionalidades para asegurar que todo funciona correctamente.

## 🛰️ **Endpoint Admin**

Una vez iniciado el servidor, puedes acceder al **Administrador de Django** en:

```
http://localhost:8000/admin/
```

---

## 🛰️ **Endpoint GraphQL**

Una vez iniciado el servidor, puedes acceder al **Playground GraphQL** en:

```
http://localhost:8000/graphql/
```

---

## 🛰️ **Endpoint Produccion**

Tambien puedes acceder al **Playground GraphQL** y **Admin** en:

```
https://lqn.fabiocordoba.me/graphql/
https://lqn.fabiocordoba.me/admin/

```

Credenciales admin Produccion

```bash
Username: fabiocordoba
Password: admin
```

---

## ⭐ **Ejemplos de consultas**

## [Ir a la documentación de Api](docs.md)

## 📌 **Buenas prácticas recomendadas**

- Usar **Conventional Commits**
- Mantener una arquitectura modular en `/apps`
- Separar la lógica en capas (models, schema)
- Incluir pruebas unitarias (pytest o unittest)
- Configurar entorno `.env` para credenciales

---

## ©️ **Autor**

**Fabio Córdoba**
Challenge Back-End – LQN
