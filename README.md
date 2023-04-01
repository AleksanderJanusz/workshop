# Workshop, app using SQL to hold users in database allowing to send messages
   
- Open terminal
- Go to app_user folder
1) To create account:
    - use: python main.py -u 'USERNAME' -p 'PASSWORD'
2) To list users:
    - use: python main.py -l
3) To edit your password
    - use: python main.py -u 'USERNAME' -p 'PASSWORD' -n 'NEW PASSWORD' -e
4) To delete user:
    - use: python main.py -u 'USERNAME' -p 'PASSWORD' -n -d
### APP MESSAGE
- Open terminal
- Go to app_message folder
1) To list messages:
    - use: python main.py -u 'USERNAME' -p 'PASSWORD' -l
2) To sand message:
    - use: python mian.py -u 'USERNAME' -p 'PASSWORD' -t 'RECIPIENT-USERNAME' -s 'MESSAGE'

### -h or --help to get help