#!/usr/bin/env python

import hmac
import sha
import urllib
import os

def sync_users(blog_base):
    url = blog_base + '/openplans-do-sync.php'
    print 'Opening url: %s' % url
    f = urllib.urlopen(url)
    res = f.read()
    if f.geturl() != url:
        print 'Got a redirect: %s' % f.geturl()
    f.close()
    return res

if __name__ == '__main__':
    import sys
    script, args = os.path.basename(sys.argv[0]), sys.argv[1:]
    if len(args) != 1:
        print 'Usage: %s domain\n' \
              '  e.g. %s http://localhost:8090' % (script, script)
        sys.exit(2)
    blog_base = args[0]
    res = sync_users(blog_base)
    print res or 'no response'
    
