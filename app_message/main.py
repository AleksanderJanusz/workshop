import argparse
from app_message.list_messages import messages_list
from app_message.send_message import send_message

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--username", help="username")
parser.add_argument("-p", "--password", help="password (min 8 characters)")
parser.add_argument("-l", "--list", help="list all users", action="store_true")
parser.add_argument("-t", "--to", help="recipient")
parser.add_argument("-s", "--send", help="text of the message")

args = parser.parse_args()

if __name__ == '__main__':
    if args.username and args.password and args.to and args.send:
        send_message(args.username, args.password, args.to, args.send)
    elif args.username and args.password and args.list:
        messages_list(args.username, args.password)
    else:
        parser.print_help()
