from psycopg2 import connect, OperationalError

CREATE_DB = "CREATE DATABASE workshop;"

CREATE_USERS_TABLE = """CREATE TABLE users(
    id serial PRIMARY KEY, 
    username varchar(255) UNIQUE,
    hashed_password varchar(80))"""

CREATE_MESSAGES_TABLE = """CREATE TABLE messages(
    id SERIAL, 
    from_id INTEGER REFERENCES users(id) ON DELETE CASCADE,
    to_id INTEGER REFERENCES users(id) ON DELETE CASCADE, 
    text varchar(255),
    creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP)"""

USER = "postgres"
PASSWORD = "coderslab"
HOST = "127.0.0.1"

try:
    cnx = connect(user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()
    try:
        cursor.execute(CREATE_DB)
        print("Database created")
    except Exception as e:
        print("Database exists ", e)
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)

try:
    cnx = connect(database="workshop", user=USER, password=PASSWORD, host=HOST)
    cnx.autocommit = True
    cursor = cnx.cursor()

    try:
        cursor.execute(CREATE_USERS_TABLE)
        print("Table users created")
    except Exception as e:
        if e.pgcode == "42P07":
            print("Table already exists!")
    try:
        cursor.execute(CREATE_MESSAGES_TABLE)
        print("Table messages created")
    except Exception as e:
        if e.pgcode == "42P07":
            print("Table already exists!")
    cnx.close()
except OperationalError as e:
    print("Connection Error: ", e)