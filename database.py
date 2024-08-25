import mysql.connector as mc 
conn = mc.connect(host ='localhost' , user = 'root' , password = 'root')

cur = conn.cursor()

create_database_query = "CREATE DATABASE IF NOT EXISTS userdata"
cur.execute(create_database_query)

conn.commit()

cur.close()
conn.close()

conn = mc.connect(host='localhost', user='root', password='root', database='userdata')

# Create a new cursor object
cur = conn.cursor()

# Create the table if it doesn't exist
create_table_query = """
CREATE TABLE IF NOT EXISTS userecord (
    name VARCHAR(25),
    email VARCHAR(25),
    query VARCHAR(60)
)
"""
cur.execute(create_table_query)

print("You have successfully created the table in the database!") 

# Close the cursor and connection
cur.close()
conn.close()