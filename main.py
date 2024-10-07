import os
from database.mongo_handler import Operations
from database.entities import User


if __name__ == '__main__':
    operator = Operations()
    user = None

    os.system('cls')
    while True:
        print("PyMongoChat - Sign In\n")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        aux = operator.authenticate(email, password)

        if(not aux):
            print("\nUser doesn't exist. Try again...")

        user = User(aux["nickname"], aux["email"], aux["password"])
        break    

    os.system('cls')
    while True:
        print("Hello, " + user.nickname + ", what would you like to do?\n")
        print("1. Send Message")
        print("2. Read Messages")
        print("3. Sign Out")
        
        option = input("\nEnter the option you want: ")
        
        if option == "3":
            os.system('cls')
            print("\nLoging Out...")
            break

        if option == "2":
            while True:
                os.system('cls') 
                print("Lendo mensagens")
                print("\nLista de mensagens:")
                print("\n1. dksadhsaj@gmail.com: olá, tudo bem?") #consulta e define prints para todos os resultados da consulta
                print("2. asdsd@gmail.com: olá, como vai?")
                print("3. lçiolçi@gmail.com: olá, bom dia.")

                sair = input("\nDeseja sair? (S/N): ")
                if sair == "S": 
                    break


        if option == "1":
            while True: 
                os.system('cls') 
                print("Enviando uma mensagem")
                emailTo = input("\nInsira o email de quem você deseja enviar uma mensagem: ")
                if emailTo == "teste": #consulta se existe esse email na coleção users
                    break
                
            while True:
                os.system('cls') 
                print("Enviando uma mensagem")
                mensagem = input("\nInsira a mensagem que deseja enviar: ")
                if len(mensagem) > 0: #valida se a mensagem não é nula
                    break
                    
            while True:
                os.system('cls') 
                print("Enviando uma mensagem")
                chaveCrip = input("\nInsira a chave de criptografia: ")
                if chaveCrip == "teste": #aqui pode ser feita uma validação se a chave é valida
                    i = 1
                    break