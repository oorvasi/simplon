import sqlite3 as lit

def main():
    try:
        db = lit.connect('simplon.db')
        cur=db.cursor()

        tablequery = "CREATE TABLE apprenant(Name TEXT, Age INT, Hobbies TEXT)"

        cur.execute(tablequery)
        print("Table Created Successfully")

    except:
        print("Unable to create table")

    finally:
        db.close()

if __name__ == "__main__":
    main()