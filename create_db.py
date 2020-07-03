from psycopg2 import connect

USER = "postgres"
HOST = "127.0.0.1"
PASSWORD = "coderslab"


def create_db(db, debug=True):
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST);
    except Exception as e:
        if debug: print("Error", e.pgcode, ":", e)
        return False
    cnx.autocommit = True
    cur = cnx.cursor()
    try:
        cur.execute(f"CREATE DATABASE {db}")
    except Exception as e:
        if debug and e.pgcode == "42P04":
            print("DataBase already exist!")
        elif debug:
            print("Error", e.pgcode, ":", e)
        cur.close()
        cnx.close()
        return False
    cur.close()
    cnx.close()
    return print("DataBase created")


def create_tables(debug=False):
    try:
        cnx = connect(user=USER, password=PASSWORD, host=HOST, database="workshop2");
    except Exception as e:
        if debug: print("Error ", e.pgcode, ":", e)
        return False
    cnx.autocommit = True
    cur = cnx.cursor()
    sql = """
        CREATE TABLE Users(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        hashed_password VARCHAR(80) NOT NULL
        );
    """
    try:
        cur.execute(sql)
    except Exception as e:
        if debug and e.pgcode == "42P07":
            print("Table already exists!")
        elif debug:
            print("Error ", e.pgcode, ":", e)
        return False
    sql = """
        CREATE TABLE Messages(
            id SERIAL PRIMARY KEY,
            from_id INT REFERENCES Users(id) NOT NULL,
            to_id INT REFERENCES Users(id) NOT NULL,
            creation_date TIMESTAMP
        );
    """
    try:
        cur.execute(sql)
    except Exception as e:
        if debug and e.pgcode == "42P07":
            print("Table already exists!")
        elif debug:
            print("Error ", e.pgcode, ":", e)
        return False
    return print("Tables created")


if __name__ == "__main__":
    create_db("Workshop2", debug=True)
    create_tables(debug=True)
