import os
from database.mongo_handler import Operations
from database.entities import User, Message
from aes_pkcs5.algorithms.aes_ecb_pkcs5_padding import AESECBPKCS5Padding


if __name__ == '__main__':

    operator = Operations() 
    user = None
    
    while True:
        os.system('cls')
        print("PyMongoChat - Sign In\n")
        email = input("Enter your email: ")
        password = input("Enter your password: ")

        aux = operator.authenticate(email, password)

        if(aux):
            user = User(aux["nickname"], aux["email"], aux["password"])
            break    

        warning = input("\nThis user doesn't exist. Try again...  (Press 'enter')")

    while True:
        os.system('cls')
        print("Hello, " + user.nickname + ", what would you like to do?\n")
        print("1. Send Message")
        print("2. Read Messages")
        print("3. Sign Out")
        
        option = input("\nEnter the option you want: ")

        if option != "1" and option != "2" and option != "3":
            warning = input("\nThis option doesn't exist. Try again...  (Press 'enter')")
        
        message = None
        email_to = ""
        msg_content = ""
        key = ""

        if option == "1":
            while True: 
                os.system('cls')
                print("Sending a message")
                email_to = input("\nInsert the email to whom you desire to send a message: ")
                aux = operator.verify_email(email_to)
                if email_to != user.email: 
                    if (aux):
                        break
                
                warning = input("\nNo user found with this email, or it may be your own. Please try again... (Press 'enter')")
                
            while True:
                os.system('cls')
                print("Sending a message")
                msg_content = input("\nEnter the message: ")
                
                if len(msg_content) > 0:
                    break
                
                warning = input("\nThe message must have at least 1 character. Please try again... (Press 'enter')")
                    
            while True:
                os.system('cls')
                print("Sending a message")
                chaveCrip = input("\nEnter the encryption key: ")

                if len(chaveCrip) == 16:

                    output_format = "b64"
                    cipher = AESECBPKCS5Padding(chaveCrip, output_format)

                    message = Message(user.email, email_to, cipher.encrypt(msg_content))

                    operator.send_new_message(message)
                    break

                warning = input("\nThe encryption key must have 16 characters. Please try again... (Press 'enter')")

        if option == "2":
            sair_loop = False
            while not sair_loop:
                os.system('cls') 
                print("Reading Messages")
                print("\nInbox: ")
                
                messages = operator.get_messages(user.email)

                i = 0

                if(not messages or len(messages) <= 0):
                    print("\nYour inbox is empty.")
                    sair = input("\nPress 'enter' to go back to the menu: ")
                    sair_loop = True
                    break
                else:
                    while i < len(messages):
                        print("\n"+ str(i + 1) +". From: "+ messages[i]["email_from"] +" - Message: "+ messages[i]["content"])
                        i = i + 1
            
                option = int(input("\nDo you want to decrypt a message? Enter the message number ('0' to exit): "))

                if option == 0:
                    sair_loop = True
                    break

                if ((option <= len(messages)) and (option > 0)):
                    break

                warning = input("\nThe option you chose doesn't exist. Please try again... (Press 'enter')")

            while not sair_loop:
                os.system('cls') 
                print("Reading Messages")
                chaveCrip = input("\nEnter the decryption key: ")

                if len(chaveCrip) == 16:
                    output_format = "b64"
                    cipher = AESECBPKCS5Padding(chaveCrip, output_format)
                    message = cipher.decrypt(messages[int(option)-1]["content"])
                    break

                warning = input("\nThe decryption key must have 16 characters. Please try again... (Press 'enter')")

            while not sair_loop:
                os.system('cls') 
                print("Reading Messages")
                print("\nDecypted message: "+message)
                sair = input("\nPress 'enter' to go back to the menu: ")
                break

        if option == "3":
            os.system('cls')
            print("\nLoging Out...")
            break
        
