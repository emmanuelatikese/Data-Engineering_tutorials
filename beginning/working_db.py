import psycopg2 as db
from faker import Faker
# Database connection parameters
fake = Faker()
conn_string = "dbname='users' host='localhost' user='postgres' password='password'"
def DBWorkings():
    try:
        conn = db.connect(conn_string)
        cur = conn.cursor()

        data = []
        for x in range(100):
            data.append((fake.name(), x, fake.street_address()))
        
        tuple_data = tuple(data)
        query = "insert into userstable (name, id, street) values (%s, %s, %s)"
        
        cur.executemany(query, tuple_data)
        conn.commit()
        
        cur.execute("Select * from userstable")
        rows = cur.fetchall()
        for y in rows:
            print(y) 
    except:
        conn.rollback()
        print("error here!!!")
    finally:
        if cur:
            cur.close()
        if conn:
            conn.close()
DBWorkings() 