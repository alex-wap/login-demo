# Login Demo

## Youtube Link

Coming soon!

## Setup
1. `django-admin startproject login_demo`
2. `cd login_demo && mkdir apps && cd apps`
3. `touch __init__.py`
4. `python ../manage.py startapp login`
5. `cd login && mkdir templates`
6. `mkdir templates/login`
7. `touch templates/login/index.html`
8. `touch templates/login/success.html`
9. `touch urls.py`
10. Complete urls.py files and settings.py
11. python manage.py makemigrations
12. python manage.py migrate
13. Complete HTML.


## Complete During Demo
1. Model register method
2. Model login method
3. Views.py register route
4. Views.py login route
5. Views.py index route
6. Views.py logout route


## Helpful Snippets


* bcrypt for login
```python
hashed = user.password
password = postData['password']
if bcrypt.checkpw(password.encode(), hashed.encode()):
  # do something
```

* bcrypt for register
```python
password = postData['password']
pw_hash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
```

* email regex pattern
```python
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
```