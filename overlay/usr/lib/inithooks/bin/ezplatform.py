#!/usr/bin/python3
"""Set eZ Platform admin password, email and domain to serve

Option:
    --pass=     unless provided, will ask interactively
    --email=    unless provided, will ask interactively


"""

import os
import re
import sys
import getopt
import inithooks_cache

import bcrypt
import time

from dialog_wrapper import Dialog
from mysqlconf import MySQL


def usage(s=None):
    if s:
        print("Error:", s, file=sys.stderr)
    print("Syntax: %s [options]" % sys.argv[0], file=sys.stderr)
    print(__doc__, file=sys.stderr)
    sys.exit(1)


def main():
    try:
        opts, args = getopt.gnu_getopt(sys.argv[1:], "h",
                                       ['help', 'pass=', 'email='])
    except getopt.GetoptError as e:
        usage(e)

    password = ""
    email = ""
    for opt, val in opts:
        if opt in ('-h', '--help'):
            usage()
        elif opt == '--pass':
            password = val
        elif opt == '--email':
            email = val

    if not password:
        d = Dialog('TurnKey Linux - First boot configuration')
        password = d.get_password(
            "eZ Platform Password",
            "Enter new password for the eZ Platform 'admin' account.")
    if not email:
        if 'd' not in locals():
            d = Dialog('TurnKey Linux - First boot configuration')

        email = d.get_email(
            "eZ Platform Email",
            "Enter email address for the eZ Platform 'admin' account.",
            "admin@example.com")

    inithooks_cache.write('APP_EMAIL', email)
    hashpass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
    today_unixtime = int(time.time())  
    
    m = MySQL()
    
    m.execute('UPDATE ezplatform.ezuser SET password_hash="%s"  WHERE login="admin";' % hashpass)
    m.execute('UPDATE ezplatform.ezuser SET password_updated_at="%s"  WHERE login="admin";' % today_unixtime)
    m.execute('UPDATE ezplatform.ezuser SET email="%s" WHERE login="admin";' % email)
    m.execute('UPDATE ezplatform.ezcontentobject_name SET name="TurnKey Linux eZ Platform" WHERE contentobject_id="1"')

if __name__ == "__main__":
    main()


