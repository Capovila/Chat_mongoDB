import os
from database.mongo_handler import Operations
from database.entities import User, Message
from aes_pkcs5.algorithms.aes_ecb_pkcs5_padding import AESECBPKCS5Padding


if __name__ == '__main__':
    key = "chatmongopython1"
    output_format = "b64"
    cipher = AESECBPKCS5Padding(key, output_format)
    operator = Operations()
    user = None

    os.system('cls')
    while True:
        print("PyMongoChat - Sign In\n")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        aux = operator.authenticate(email, password)

        if(aux):
            user = User(aux["nickname"], aux["email"], aux["password"])
            break    

        print("\033[31mUser doesn't exist. Try again...\033[0m\n")

    while True:
        os.system('cls')
        print("Hello, " + user.nickname + ", what would you like to do?\n")
        print("1. Send Message")
        print("2. Read Messages")
        print("3. Sign Out")
        
        option = input("\nEnter the option you want: ")
        
        message = None
        email_to = ""
        msg_content = ""
        if option == "1":
            os.system('cls')
            while True: 
                print("Enviando uma mensagem")

                email_to = input("\nInsira o email de quem você deseja enviar uma mensagem: ")

                if (not operator.verify_email(email_to)):
                    print("No user using this email. Try again...")
                break
                
            os.system('cls')
            while True:
                print("Enviando uma mensagem")

                msg_content = input("\nInsira a mensagem que deseja enviar: ")

                if len(msg_content) > 0: #valida se a mensagem não é nula
                    message = Message(user.email, email_to, cipher.encrypt(msg_content))
                    break
                
                print("\033[31mThe message must have at least 1 character.\033[0m")
                    
            os.system('cls')
            while True:
                print("Enviando uma mensagem")
                chaveCrip = input("\nInsira a chave de criptografia: ")
                if chaveCrip == key: #aqui pode ser feita uma validação se a chave é valida
                    operator.send_new_message(message)
                    break

        if option == "2":
            while True:
                os.system('cls') 
                print("Reading Messages")
                print("\nInbox: ")
                print("\n1. dksadhsaj@gmail.com: olá, tudo bem?") #consulta e define prints para todos os resultados da consulta
                print("2. asdsd@gmail.com: olá, como vai?")
                print("3. lçiolçi@gmail.com: olá, bom dia.")

                sair = input("\nDeseja sair? (S/N): ")
                if sair == "S": 
                    break

        if option == "3":
            os.system('cls')
            print("\nLoging Out...")
            break