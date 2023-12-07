import psycopg2
conn =  psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")

cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS user_using_copy(
            id serial primary key,
            email text,
            name text,
            phone text,
            postal_code text
        )
        """)

with open("/Users/nurululum/Documents/DATA ENGINEER/PROJECT/PROJECT 3/source/users_w_postal_code.csv","r") as f :
    next(f)
    cur.copy_from(f, "user_using_copy", sep = ",", columns = ("email","name","phone","postal_code"))

conn.commit()