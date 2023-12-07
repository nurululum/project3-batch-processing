import psycopg2

conn =  psycopg2.connect("host=localhost dbname=postgres user=postgres password=digitalskola")

cur = conn.cursor()

cur.execute("""
            CREATE TABLE IF NOT EXISTS latihan(
            id serial primary key,
            email text,
            name text,
            phone text,
            postal_code text
        )
        """)

conn.commit()