# FLASK REST API PROJECT, deployed on Render.com

Deployed in Render.com, check it out 👉 https://flask-rest-api-project-rmrw.onrender.com/
<br>Database transformation: SQLite -> PostgreSQL

## Tools and Technologies 🛠️:

Flask, Flask-SQLAlchemy, Flask-JWT-Extended, Flask-RESTX, Python-Decouple, PyTest, SwaggerUI, Werkzeug, Unittest, Render.com, PostgreSQL, DB browser, SQLite

## Practicing Include 📚:

- Flask REST API with Python
- Environment variables with Python-Decouple
- JWT Authentication with Flask-JWT-Extended
- Databases with Flask-SQLAlchemy
- How to write Unit Tests with Unittest and PyTest
- Documenting REST APIs with SwaggerUI and Flask-RESTX
- Error Handling with Werkzeug

## Basic Setup 🚀

Enter the project folder and create a virtual environment

```bash
$ python -m venv env
$ source env/bin/actvate #On linux Or Unix
$ source env/Scripts/activate #On Windows
$ pip install -r requirements.txt #Install all requirements
python runserver.py #Run the server
```

## Changed the id type from integer to serial in the table

Note: While transferring the database schema from SQLite to PostgreSQL, I encountered errors when signing up new users and creating new orders in SwaggerUI. After thorough troubleshooting, I discovered that PostgreSQL does not auto-increment the ID, unlike SQLite. To resolve this, I deleted the transformed old table in HeidiSQL, changed the ID type to serial, created a new table, inserted data, and implemented SQL auto-increment code in the table, which resolved the issue.

## DEMO Time 🛒

## Run the project in development environment

Database: SQLite || Backend test tool: Thunder Client<br>
localhost http://127.0.0.1:5000/
![screenshot1](screencut/flaskapi.jpg)

## Run the project in production environment

![screenshot1](screencut/SwaggerUITest.jpg)

## 1. Signup a new user

![screenshot1](screencut/signup.jpg)
![screenshot1](screencut/signup2.jpg)

## 2. Login with the user

![screenshot1](screencut/login1.jpg)
![screenshot1](screencut/login2.jpg)

## 3. Authorization with JWT successfully

<img src="screen/../screencut/jwt1.jpg" alt="s" width="400" height="220">

<img src="screen/../screencut/jwt2.jpg" alt="s" width="400" height="200">

## Reference:

👍 **Very good Flask learning resource from Youtuber [Ssali Jonathan](https://www.youtube.com/watch?v=OEZxEY_wdN4&list=PLEt8Tae2spYnFMndU9EM082imnnzke07J)** update
