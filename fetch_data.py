import psycopg2

# Connect to PostgreSQL
try:
    conn = psycopg2.connect(
        dbname="hmdbms",
        user="postgres",
        password="postgres",
        host="localhost",
        port="5432"
    )

    cursor = conn.cursor()

    # Example: Fetch data from the `patients` table
    cursor.execute("SELECT * FROM patients")
    rows = cursor.fetchall()

    # Print fetched data
    for row in rows:
        print(row)

    cursor.execute("SELECT * FROM doctors")
    demo = cursor.fetchall()

    for dem in demo:
        print(dem)

except Exception as e:
    print(f"Error: {e}")

finally:
    if 'cursor' in locals():
        cursor.close()
    if 'conn' in locals():
        conn.close()
