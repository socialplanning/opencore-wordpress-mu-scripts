import MySQLdb
import sys

try:
    dbname = sys.argv[1]
except IndexError:
    dbname = 'woonerf_livablestreets_wordpress'

db = MySQLdb.connect(db=dbname, user='wordpress', passwd='wordpress')
c = db.cursor()
query = 'select blog_id from wp_blogs'
c.execute(query)
results = list(c.fetchall())
for row in results:
    id = row[0]
    update_query = "update wp_%s_options set option_value='livablestreets' where option_name='template'" % id
    c.execute(update_query)
