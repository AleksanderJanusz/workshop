import argparse
from app_user.funktions.add import add_user
from app_user.funktions.dele import delete_user
from app_user.funktions.lists import users_list
from app_user.funktions.password_edit import password_edit


parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-n", "--new_pass", help="new password (min 8 characters)")
parser.add_argument("-l", "--list", help="list all users", action="store_true")
parser.add_argument("-d", "--delete", help="delete user", action="store_true")
parser.add_argument("-e", "--edit", help="edit user", action="store_true")

args = parser.parse_args()


if __name__ == '__main__':
    if args.username and args.password and args.edit and args.new_pass:
        password_edit(args.username, args.password, args.new_pass)
    elif args.username and args.password and args.delete:
        delete_user(args.username, args.password)
    elif args.username and args.password:
        add_user(args.username, args.password)
    elif args.list:
        users_list()
    else:parser.print_help()

