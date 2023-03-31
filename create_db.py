from psycopg2 import connect, OperationalError, sql, DatabaseError
from psycopg2.errors import DuplicateDatabase, DuplicateTable

create_db_query = sql.SQL("""
    CREATE DATABASE {db_name}

""").format(db_name=sql.Identifier('workshop'))

create_table_user = sql.SQL("""
    CREATE TABLE {table_name}(
        id SERIAL PRIMARY KEY,
        username VARCHAR(255),
        hashed_password VARCHAR(80));

""").format(table_name=sql.Identifier('users'))

create_table_messages = sql.SQL("""
    CREATE TABLE {table_name}(
        id SERIAL PRIMARY KEY,
        from_id INTEGER REFERENCES {foreign_table_name}(id),
        to_id INTEGER REFERENCES {foreign_table_name}(id),
        creation_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        text VARCHAR(255));

""").format(table_name=sql.Identifier('messages'), foreign_table_name=sql.Identifier('users'))

""" 
CREATE DATABASE
"""
try:
    cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432)
    cnx.autocommit = True
    cursor = cnx.cursor()
    print('Connected')
except OperationalError as error:
    print('Connection Error')
    raise ValueError(f'Connection Error: {error}')

try:
    cursor.execute(create_db_query)
except DuplicateDatabase as error:
    print('This database already exists')
finally:
    cnx.close()

"""
OPEN DATABASE
"""

try:
    cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
    cnx.autocommit = True
    cursor = cnx.cursor()
    print('Connected')
except OperationalError as error:
    print('Connection Error')
    raise ValueError(f'Connection Error: {error}')

with cnx:
    try:
        cursor.execute(create_table_user)
    except DatabaseError as error:
        print(error)
    except DuplicateTable as error:
        print("This table already exists")

    try:
        cursor.execute(create_table_messages)
    except DatabaseError as error:
        print(error)
    except DuplicateTable as error:
        print("This table already exists")

cnx.close()
