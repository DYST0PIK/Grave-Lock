import hash_menu

def main_menu():
    print('''
        Choose an option [1-2]:                 Type "exit" to stop.
    
        [1] - Encrypt Password
        [2] - Decrypt Hash
        ''')

    while True:
        option = input(">> ")

        if option == "1":
            hash_menu.encrypt_option()
            main_menu()
        elif option == "2":
            hash_menu.decrypt_option()
            main_menu()
        elif option == "exit":
            exit()
        else:
            print("-- Wrong option --")
            main_menu()

