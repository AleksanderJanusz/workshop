from psycopg2 import connect, OperationalError, sql, DatabaseError
from app_user.hash import hash_password


class User:
    def __init__(self, name='', password=''):
        self._id = -1
        self.username = name
        self.hashed_password = password

    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return {self._hashed_password}

    @hashed_password.setter
    def hashed_password(self, value):
        try:
            value = hash_password(value)
        except TypeError:
            raise TypeError('Try again later')
        self._hashed_password = value

    def save_to_db(self):
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        query_insert_user = sql.SQL("""
            INSERT INTO {table_name}(username, hashed_password)
            VALUES (%s, %s)
        """).format(table_name=sql.Identifier('users'))

        with cnx:
            try:
                cursor.execute(query_insert_user, (self.username, self._hashed_password))
            except DatabaseError as error:
                print(error)
        cnx.close()

    def _load_user(self, value=None):
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
            # print('Connected')
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        request_sql = sql.SQL("""
            SELECT id, username, hashed_password
            FROM users;

        """)

        with cnx:
            try:
                cursor.execute(request_sql)
                if type(value) == str:
                    for (id, username, hashed_password) in cursor:
                        if username == value:
                            self._id = id
                            self.username = username
                            self._hashed_password = hashed_password
                elif type(value) == int:
                    for (id, username, hashed_password) in cursor:
                        if id == value:
                            self._id = id
                            self.username = username
                            self._hashed_password = hashed_password
                else:
                    cnx.close()
                    print("Something goes wrong. Try again later")
                    return

            except DatabaseError as error:
                print(error)
        cnx.close()

    def load_user_by_username(self, name):
        self._load_user(name)

    def load_user_by_id(self, id_):
        self._load_user(id_)

    @staticmethod
    def load_all_users():
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
            # print('Connected')
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        request_sql = sql.SQL("""
            SELECT id, username, hashed_password
            FROM users;

        """)
        print('ID | username')
        print('_____________')
        with cnx:
            try:
                cursor.execute(request_sql)
                for row in cursor.fetchall():
                    id_, username, hashed_password = row
                    print(id_, '|', username)

            except DatabaseError as error:
                print(error)
        cnx.close()

    def delete(self):
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
            # print('Connected')
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        query_delete = sql.SQL("""
            DELETE
            FROM {table_name}
            WHERE id = %s
        """).format(table_name=sql.Identifier('users'))

        with cnx:
            try:
                cursor.execute(query_delete, (self._id,))
            except DatabaseError as error:
                print(error)
        cnx.close()


class Messages:
    def __init__(self, from_id, to_id, text):
        self._id = -1
        self.from_id = from_id
        self.to_id = to_id
        self.text = text
        self.creation_data = None

    def id(self):
        return self._id

    def save_to_db(self):
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
            # print('Connected')
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        query_insert_message = sql.SQL("""
            INSERT INTO {table_name}(from_id, to_id, text)
            VALUES (%s, %s, %s)
        """).format(table_name=sql.Identifier('messages'))

        with cnx:
            try:
                cursor.execute(query_insert_message, (self.from_id, self.to_id, self.text))
            except DatabaseError as error:
                print(error)
        cnx.close()

    @staticmethod
    def load_all_messages():
        try:
            cnx = connect(user='postgres', password='coderslab', host='localhost', port=5432, database='workshop')
            cursor = cnx.cursor()
            # print('Connected')
        except OperationalError as error:
            print("Connection Error")
            raise ValueError(f"Connection Error: {error}")

        request_sql = sql.SQL("""
            SELECT id, from_id, to_id, creation_date, text
            FROM messages;

        """)
        print("|ID|", "ID from|", "ID to|", "Date of creation|", "Message|")
        with cnx:
            try:
                cursor.execute(request_sql)
                for [*args] in cursor:
                    print(*args)
            except DatabaseError as error:
                print(error)
        cnx.close()


