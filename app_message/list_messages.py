from app_user.hash import hash_password
from models import User
from psycopg2 import connect, OperationalError, sql, DatabaseError


def messages_list(name, password):
    check = User()
    check.load_user_by_username(name)
    if check.username != name:
        print('Incorrect username')
        return
    if hash_password(password) not in check.hashed_password:
        print('Incorrect password')
        return

    try:
        cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
        cursor = cnx.cursor()
    except OperationalError as error:
        print("Connection Error")
        raise ValueError(f"Connection Error: {error}")

    query_list_messages = sql.SQL("""
                SELECT text, creation_date
                FROM messages
                WHERE to_id = %s;

            """)
    print(f'User: {check.username}\n\nMessages:\n')
    with cnx:
        try:
            cursor.execute(query_list_messages, (check.id(),))
            for [*args] in cursor:
                print(*args + ['\n'], sep=' | ')
        except DatabaseError as error:
            print(error)
    cnx.close()


