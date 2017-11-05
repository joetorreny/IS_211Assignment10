import sqlite3


def main():
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()
    cursor.execute("insert into Person values (1, 'James', 'Smith', 41)")
    cursor.execute("insert into Person values (2, 'Diana', 'Greene', 23)")
    cursor.execute("insert into Person values (3, 'Sara', 'White', 27)")
    cursor.execute("insert into Person values (4, 'William', 'Gibson', 23)")
    cursor.execute("insert into Pet values (1, 'Rusty', 'Dalmation', 4, 1)")
    cursor.execute("insert into Pet values (2, 'Bella', 'Alaskan Malamute', 3, 0)")
    cursor.execute("insert into Pet values (3, 'Max', 'Cocker Spaniel', 1, 0)")
    cursor.execute("insert into Pet values (4, 'Rocky', 'Beagle', 7, 0)")
    cursor.execute("insert into Pet values (5, 'Rufus', 'Cocker Spaniel', 1, 0)")
    cursor.execute("insert into Pet values (6, 'Spot', 'Bloodhound', 2, 1)")
    cursor.execute("insert into Person_Pet values (1, 1)")
    cursor.execute("insert into Person_Pet values (1, 2)")
    cursor.execute("insert into Person_Pet values (2, 3)")
    cursor.execute("insert into Person_Pet values (2, 4)")
    cursor.execute("insert into Person_Pet values (3, 5)")
    cursor.execute("insert into Person_Pet values (4, 6)")
    conn.commit()


if __name__ == "__main__":
    main()
