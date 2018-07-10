import sqlite3

def insert_into_db():
    # Connect to database - i.e. create database file if not present
    conn = sqlite3.connect("datenbank.db")
    c = conn.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS personen(nr int, name text)")

    # Insert some sample data
    for i, name in enumerate(["Peter", "Petra", "Hans", "Claudia"]):
        # use ? to avoid sql injection
        c.execute("INSERT INTO personen VALUES(?,?)", (100+i, name))

    conn.commit()
    conn.close()

def select_from_db():
    conn = sqlite3.connect("datenbank.db")
    c = conn.cursor()
    rows = c.execute("SELECT nr, name FROM personen")

    print("Nr.\tName")
    for i, name in rows:
        print(i, "    ", name)

    conn.close()


if __name__ == "__main__":
    insert_into_db()
    select_from_db()
