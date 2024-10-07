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
                print("Sending a message")
                email_to = input("\nInsert the email to whom you desire to send a message: ")

                if (not operator.verify_email(email_to)):
                    print("No user using this email. Try again...")
                break
                
            os.system('cls')
            while True:
                print("Sending a message")

                msg_content = input("\nEnter the message: ")

                if len(msg_content) > 0:
                    message = Message(user.email, email_to, cipher.encrypt(msg_content))
                    break
                
                print("\033[31mThe message must have at least 1 character.\033[0m")
                    
            os.system('cls')
            while True:
                print("Sending a message")
                chaveCrip = input("\nEnter the encryption key: ")
                if chaveCrip == key:
                    operator.send_new_message(message)
                    break

        if option == "2":
            while True:
                os.system('cls') 
                print("Reading Messages")
                print("\nInbox: ")
                
                messages = operator.get_messages(user.email)

                i = 0

                if(not messages or len(messages) <= 0):
                    print("Your inbox is empty.")
                else:
                    while i < len(messages):
                        print('{}. From:{}\Message: {}\n'.format(i+1, messages[i]["email_from"], cipher.decrypt(messages[i]["content"])))
                        i = i+1

                sair = input("\nDo you want to back to the menu? (Y/N): ")
                if sair == "Y" or sair == "y": 
                    break

        if option == "3":
            os.system('cls')
            print("\nLoging Out...")
            break