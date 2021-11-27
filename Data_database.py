import sqlite3

def log_data(date, uuid, humidity, temperature):
    con = sqlite3.connect('data.db')
    cur = con.cursor()

    try:
        # Create table
        cur.execute('''CREATE TABLE logs
                       (date text, uuid text,  humidity text, temperature text)''')
    except:
        print("Table existed")
    # The qmark style used with executemany():
    lang_list = [
        (date, uuid, humidity, temperature),
    ]

    cur.executemany("INSERT INTO logs VALUES (?,?,?,?)", lang_list)

    # Save (commit) the changes
    con.commit()

    # We can also close the connection if we are done with it.
    # Just be sure any changes have been committed or they will be lost.
    con.close()

if __name__ == "__main__":
    log_data()