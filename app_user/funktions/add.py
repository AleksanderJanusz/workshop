from models import User


def add_user(name, password):
    user = User(name, password)
    check = User('Check', 'Check')
    check.load_user_by_username(name)
    if check.username == name:
        print("This user name is taken")
        return
    if len(password) > 7:
        user.save_to_db()
        return
    print("The password is too short")
