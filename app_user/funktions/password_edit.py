from psycopg2 import connect, OperationalError, sql, DatabaseError

from app_user.hash import hash_password
from models import User


def password_edit(name, password, new_password):
    check = User()
    check.load_user_by_username(name)

    if check.username == name and hash_password(password) in check.hashed_password:
        new_password = hash_password(new_password)
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        query_update_password = sql.SQL("""
             UPDATE {table_name}
             SET hashed_password = %s
             WHERE username = %s


         """).format(table_name=sql.Identifier('users'))

        with cnx:
            try:
                cursor.execute(query_update_password, (new_password, name))
            except DatabaseError as error:
                print(error)
        cnx.close()
        return

    print('User name or password is incorrect')
    return
