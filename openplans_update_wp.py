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

def create_blog(blog_base, domain, path, title, topp_secret_filename):
    url = blog_base + '/openplans-create-blog.php'
    data = {
        'domain': domain,
        'path': path,
        'title': title,
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

def add_user(blog_base, username, email, topp_secret_filename):
    url = blog_base + '/openplans-create-user.php'
    data = {
        'username': username,
        'email': email
        }
    sig = hmac.new(get_secret(topp_secret_filename), username, sha).digest()
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

def remove_user(blog_base, username, topp_secret_filename):
    url = blog_base + '/openplans-remove-user.php'
    data = {
        'username': username,
        }
    sig = hmac.new(get_secret(topp_secret_filename), username, sha).digest()
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

def add_user_to_blog(blog_base, username, domain,role , topp_secret_filename):
    url = blog_base + '/openplans-add-usertoblog.php'
    data = {
        'username': username,
        'domain': domain,
        'role': role
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

def change_role(blog_base, username, domain, newrole , topp_secret_filename):
    url = blog_base + '/openplans-change-role.php'
    data = {
        'username': username,
        'domain': domain,
        'newrole': newrole
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

def remove_user_from_blog(blog_base, username, domain, topp_secret_filename):
    url = blog_base + '/openplans-remove-userfromblog.php'
    data = {
        'username': username,
        'domain': domain
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

def change_email(blog_base, username, email, topp_secret_filename):
    url = blog_base + '/openplans-change-email.php'
    data = {
        'username': username,
        'email': email
        }
    sig = hmac.new(get_secret(topp_secret_filename), username, sha).digest()
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
    if len(args) == 0:
        print 'Usage: %s blog_url action [parms for actions]  /path/to/secret.txt\n' \
              '  e.g. %s http://localhost:8090 adduser username email /usr/local/topp/var/lib/secret.txt \n' \
              '  e.g. %s http://localhost:8090 changerole project username newrole /usr/local/topp/var/lib/secret.txt \n' \
              '  e.g. %s http://localhost:8090 changeemail username newemail /usr/local/topp/var/lib/secret.txt \n' \
              '  e.g. %s http://localhost:8090 createblog someproj.openplans.org my_title /usr/local/topp/var/lib/secret.txt \n' \
              '  e.g. %s http://localhost:8090 addusertoblog username someproj.openplans.org role /usr/local/topp/var/lib/secret.txt \n' \
              '  e.g. %s http://localhost:8090 removeuserfromblog username someproj.openplans.org /usr/local/topp/var/lib/secret.txt \n' \
              '  e.g. %s http://localhost:8090 removeuser username /usr/local/topp/var/lib/secret.txt \n' \
              % (script, script,script, script, script, script, script, script  )
        sys.exit(2)
    blog_base = args[0]
    action = args[1]
    print "the action you selected is "+action
    if (action == 'adduser'):
        username = args[2]
        email = args[3]
        topp_secret_filename = args[4]
        res = add_user(blog_base, username, email, topp_secret_filename)
        print res or 'no response'
    elif (action == 'changerole'):
        domain = args[2]
        username = args[3]
        newrole = args[4]
        topp_secret_filename = args[5]
        res = change_role(blog_base, username, domain, newrole, topp_secret_filename)
        print res or 'no response'
    elif (action == 'changeemail'):
        username = args[2]
        newemail = args[3]
        topp_secret_filename = args[4]
        res = change_email(blog_base, username, newemail, topp_secret_filename)
        print res or 'no response'
    elif (action == 'createblog'):
        domain = args[2]
        title = args[3]
        topp_secret_filename = args[4]
        res = create_blog(blog_base, domain, '/blog', title, topp_secret_filename)
        print res or 'no response'
    elif (action == 'addusertoblog'):
        domain = args[3]
        username = args[2]
        role = args[4]
        topp_secret_filename = args[5]
        res = add_user_to_blog(blog_base, username, domain, role ,topp_secret_filename)
        print res or 'no response'
    elif (action == 'removeuserfromblog'):
        domain = args[3]
        username = args[2]
        topp_secret_filename = args[4]
        res = remove_user_from_blog(blog_base, username, domain, topp_secret_filename)
        print res or 'no response'
    elif (action == 'removeuser'):
        username = args[2]
        topp_secret_filename = args[3]
        print "do not use this yet.  It hasn't been decided how this will be implemented"
        sys.exit(2)
        res = remove_user(blog_base, username, topp_secret_filename)
        print res or 'no response'
    else:
        print "illegal action"
    
