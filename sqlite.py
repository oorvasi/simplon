import sqlite3 as lit

def main():
    try:
        db = lit.connect('apprenant.db')

    except:
        print("Failed to create database")

    finally:
        db.close()

if __name__ == "__main__":
    main()