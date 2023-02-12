import psycopg2
import hashlib

def connect_to_db():
    try:
        conn = psycopg2.connect(
            host="127.0.0.1",
            database="Casino",
            user="Archy",
            password="LALonely1"
        )
        print("Connected to the database.")
        return conn

    except psycopg2.OperationalError as e:
        print("Unable to connect to the database: ", e)
        return None

def export_to_db(conn, data):
    try:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM users WHERE username=%s", (data[0],))
        if cursor.fetchone():
            print("Username already exists in the database.")
        else:
            # Hash the password using SHA-256
            hashed_password = hashlib.sha256(data[1].encode()).hexdigest()
            cursor.execute("""
                INSERT INTO users (username, password)
                VALUES (%s, crypt(%s, gen_salt('bf')))
            """, (data[0], hashed_password))
            conn.commit()
            print("Data exported successfully to the database.")

    except psycopg2.DatabaseError as e:
        print("Error while exporting data to the database: ", e)
        conn.rollback()

conn = connect_to_db()
if conn:
    data = ("username", "xpass")
    export_to_db(conn, data)
    username = input("Login")
    xpass = input("Your password")
    data = (username, xpass)
    export_to_db(conn, data)
    conn.close()
