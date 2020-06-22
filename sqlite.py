import sqlite3 as lit

def main():
    try:
        db = lit.connect('simplon.db')

    except:
        print("Failed to create database")

    finally:
        db.close()

if __name__ == "__main__":
    main()

