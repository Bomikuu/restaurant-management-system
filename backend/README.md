# Gentry Restaurant Management System

**Created by Team Vision**

 - Ang, Mico
 - Gomez, Divya
 - Maligad, Jam
 - Maxey, Adrheinelle
 - Mendoza, Rhainne
 - Pil, Gabriel
 - Pulido, Marco

# Project Structure

This repository will separate the development for the frontend and the backend.

The `backend` folder consists of the main backend files coming from django.

The `frontend` folder consists of the main frontend files coming from vuejs.

## Backend

### Development Setup

 1. Create a `virtualenv` or `virtualenvwrapper`
 2. Navigate to the `/requirements/` folder and run `pip install -r requirements.txt`
 3. Create a `local_settings.py` file in the `backend/conf/` directory with the contents below: 

    DATABASES  =  {
    'default':  {
    'ENGINE':  'django.db.backends.postgresql_psycopg2',
    'NAME':  'gentry-system-test-1',
    'USER':  'postgres',
    'PASSWORD':  'root',
    'HOST':  'localhost',
    'PORT':  '',
    }
    }

 4. Apply initial migrations using: `python manage.py migrate`
 5. Finally, you may run the server using: `python manage.py runserver <optional: port>`

## Frontend

### Development Setup

    To be added

# Modules

    Details for modules below will be added soon

## User Management

    To be added

## Order Management

    To be added

## Product Management

    To be added

## Inventory Management

    To be added

## UML diagrams (Sample)

You can render UML diagrams using [Mermaid](https://mermaidjs.github.io/). For example, this will produce a sequence diagram:

```mermaid
sequenceDiagram
Alice ->> Bob: Hello Bob, how are you?
Bob-->>John: How about you John?
Bob--x Alice: I am good thanks!
Bob-x John: I am good thanks!
Note right of John: Bob thinks a long<br/>long time, so long<br/>that the text does<br/>not fit on a row.

Bob-->Alice: Checking with John...
Alice->John: Yes... John, how are you?
```

And this will produce a flow chart:

```mermaid
graph LR
A[Square Rect] -- Link text --> B((Circle))
A --> C(Round Rect)
B --> D{Rhombus}
C --> D
```