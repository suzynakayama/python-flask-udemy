import sqlite3

connection = sqlite3.connect('data.db')  # initialize sqlite and pass the name of the file you want 'data.db'

cursor = connection.cursor()  # responsible to execute the queries and store the result

create_table = 'CREATE TABLE users (id int, username text, password text)'  # pass the schema inside the ()

cursor.execute(create_table)  # execute the query

user = (1, 'John', '1234')

insert_query = 'INSERT INTO users VALUES(?,?,?)'
cursor.execute(insert_query, user)

users = [
    (2, 'Jane', '5678'),
    (3, 'Mary', '9012'),
    (4, 'Laird', '3456'),
]

cursor.executemany(insert_query, users)

select_query = "SELECT * FROM users"  # get all the data
for row in cursor.execute(select_query):
    print(row)

connection.commit() # save the db

connection.close() # close the connection