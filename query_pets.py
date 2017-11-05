import sqlite3


def main():
    conn = sqlite3.connect("pets.db")
    cursor = conn.cursor()
    while 1:
        person_id = input("Enter person ID: ")
        if person_id == "-1":
            print("Exiting program")
            break
        cursor.execute("select * from Person where id={}".format(person_id))
        person = cursor.fetchall()
        cursor.execute("select pet_id from Person_Pet where person_id={}".format(person_id))
        pet_ids = cursor.fetchall()
        pet_ids = [pet_id[0] for pet_id in pet_ids]
        if len(person) == 0:
            print("No person found")
        else:
            person_first_name = person[0][1]
            person_last_name = person[0][2]
            person_age = person[0][3]
            print("{} {} is {} years old".format(person_first_name, person_last_name, person_age))
            for pet_id in pet_ids:
                cursor.execute("select * from Pet where id={}".format(pet_id))
                pet = cursor.fetchall()
                pet_name = pet[0][1]
                pet_breed = pet[0][2]
                pet_age = pet[0][3]
                print("{} {} owned {}, a {}, that was {} years old".format(person_first_name, person_last_name,
                                                                           pet_name, pet_breed, pet_age))


if __name__ == "__main__":
    main()
