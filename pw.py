#! usr/bin/python3
# this is a basic password manager program. warning: not a secure solution student use only

PASSWORDS = {'email': 'f69420ABC123abcXyZ',
             'blog': '5ixtYn9n3!',
             'luggage': '123456789'}


import sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python pw.py [account] - copy account password')
    sys.exit()

account = sys.argv[1]       # first command line arg is the account name again

if account in PASSWORDS:
    pyperclip.copy(PASSWORDS[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named: ' + account)

