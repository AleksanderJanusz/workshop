from app_user.hash import hash_password
from models import User


def delete_user(name, password):
    check = User()
    check.load_user_by_username(name)

    if check.username == name and hash_password(password) in check.hashed_password:
        check.delete()
        print('User deleted')
        return
    print("Login failed")
