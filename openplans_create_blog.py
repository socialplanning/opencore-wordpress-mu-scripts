#!/usr/bin/env python

import hmac
import sha
import urllib
import os

def get_secret(topp_secret_filename):
    f = open(topp_secret_filename, 'rb')
    try:
        return f.read().strip()
    finally:
        f.close()

def create_blog(blog_base, domain, path, title, user_id, topp_secret_filename):
    url = blog_base + '/openplans-create-blog.php'
    data = {
        'domain': domain,
        'path': path,
        'title': title,
        'user_id': str(user_id),
        }
    sig = hmac.new(get_secret(topp_secret_filename), domain, sha).digest()
    sig = sig.encode('base64').strip()
    data['signature'] = sig
    data = urllib.urlencode(data)
    print 'Opening url: %s' % url
    f = urllib.urlopen(url, data)
    res = f.read()
    if f.geturl() != url:
        print 'Got a redirect: %s' % f.geturl()
    f.close()
    return res

if __name__ == '__main__':
    import sys
    script, args = os.path.basename(sys.argv[0]), sys.argv[1:]
    if len(args) != 5:
        print 'Usage: %s blog_url domain title user_id /path/to/secret.txt\n' \
              '  e.g. %s http://localhost:8090 someproj.openplans.org my_title my_id /usr/local/topp/var/lib/secret.txt' % (
            script, script)
        sys.exit(2)
    blog_base, domain, title, user_id, topp_secret_filename = args
    res = create_blog(blog_base, domain, '/blog', title, user_id, topp_secret_filename)
    print res or 'no response'
    
