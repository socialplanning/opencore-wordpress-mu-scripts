#!/usr/bin/env python

import sys, re
try:
    db      = sys.argv[1]
    oldrole = len(sys.argv) > 2 and sys.argv[2] or 'contributor'
    newrole = len(sys.argv) > 3 and sys.argv[3] or 'author'
    user    = len(sys.argv) > 4 and sys.argv[4] or 'wordpress'
    passwd  = len(sys.argv) > 5 and sys.argv[5] or 'wordpress'
except IndexError:
    print "Usage:", sys.argv[0], "database [oldrole] [newrole] [user] [passwd]"
    print "FOR WOONERF: oldrole=contributor, newrole=author"
    sys.exit(1)

import MySQLdb
db = MySQLdb.connect(db=db,user=user,passwd=passwd)
c = db.cursor()

query_wp_usermeta = 'select meta_value, meta_key from wp_usermeta'
c.execute(query_wp_usermeta)
results_wp_usermeta = c.fetchall()

pattern = 'wp_\d+_capabilities'
reg = re.compile(pattern)

for meta_value, meta_key in results_wp_usermeta:

    meta_match = reg.search(meta_key)
    if not meta_match:
        pass
    else:
        oldSerial = meta_value
        newSerial = meta_value.replace(oldrole,newrole)
        newSerial = newSerial.replace(str(len(oldrole)), str(len(newrole)))
        query_update_role = "UPDATE wp_usermeta SET meta_value = '%s' WHERE meta_value = '%s' " % (newSerial, oldSerial)
        c.execute(query_update_role)
        print query_update_role

