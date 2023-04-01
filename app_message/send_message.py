from app_user.hash import hash_password
from models import User, Messages
from psycopg2 import connect, OperationalError, sql, DatabaseError


def send_message(name, password, to, text):
    check = User()
    check.load_user_by_username(name)
    recipient = User()
    recipient.load_user_by_username(to)
    if check.username != name:
        print('Incorrect username')
        return
    if hash_password(password) not in check.hashed_password:
        print('Incorrect password')
        return
    if recipient.username != to:
        print('There is no such user')
        return
    if len(text) > 255:
        print('Your message is to long. Max 255 characters')
        return

    message = Messages(check.id(), recipient.id(), text)
    message.save_to_db()
    print('Message send')



