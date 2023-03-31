from models import User


def users_list():
    user = User()
    user.load_all_users()
