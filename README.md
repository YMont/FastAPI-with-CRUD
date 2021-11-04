# FastAPI-with-CRUD
This is Python's framework FastAPI to connect SQLite database with SQLAlchemy framework

# Prepare
## virtual enviroment
```
pip install virtualenv
```
## requirements
```txt
anyio==3.3.4
asgiref==3.4.1
click==8.0.3
colorama==0.4.4
fastapi==0.70.0
greenlet==1.1.2
h11==0.12.0
idna==3.3
Jinja2==3.0.2
MarkupSafe==2.0.1
pydantic==1.8.2
sniffio==1.2.0
SQLAlchemy==1.4.26
starlette==0.16.0
typing-extensions==3.10.0.2
uvicorn==0.15.0
```

# File Architecture
```
|---project
|       |---app
|            |---__init__.py
|            |---database.py
|            |---model.py
|            |---schemas.py
|            |---crud.py
|            |---main.py
```
# Get Start
## create virtualenv
virtual project name is "app"
```
virtualenv appName
```
## activate virtualenv
```
# open and enter cmd
# (windows)
D:\fastapi\app>Scripts\activate
(app)D:\fastapi\app\Scripts\activate
```
## run fastapi server
```
# cmd
(app) D:\fastapi\app> uvicorn main:app --reload
[32mINFO[0m:     Waiting for application startup.
[32mINFO[0m:     Application startup complete.
...
...
```

