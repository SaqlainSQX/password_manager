from cryptography.fernet import Fernet

'''
def write_key ():
    key =Fernet.generate_key()
    with open ("key.key","wb") as key_file :
        key_file.write(key)
'''


def load_key ():
    file = open ("key.key", "rb")
    key=file.read()
    file.close()
    return key








def view ():
    with open ('password.txt' , 'r') as f:
        for line in f.readlines():
            data =  line.rstrip()
            user , passw = data.split("|")

            print(f"User : {user} Password : {fer.decrypt(passw.encode()).decode()}")
            

        

def add():
    name = input("Account Name : ")
    pwd = input ("Password : ")

    with open ('password.txt' , 'a') as f:
        f.write(name+"|"+ fer.encrypt(pwd.encode()).decode() + "\n")

master_pwd=input ("Enter master password : ")

if(master_pwd == "Yes"):
    key=load_key() 
    fer = Fernet(key)



    while True:

        mode =input("Would you want to add a new password or input new ones or quit (view , add , quit )").lower()

        if mode == 'quit':
            quit()

        if mode == 'view':
            view()

        elif mode == 'add':
            add ()

        else :
            continue

else : 
    print("Wrong Password !!! Try again later")