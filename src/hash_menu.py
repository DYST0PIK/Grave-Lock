import hash_tools
import main_menu
def encrypt_option():

    print("        Write the password: ")
    password = input(">> ")
    print("""   
        [1]     md5
        [2]     sha1
        [3]     sha224
        [4]     sha256
        [5]     sha384
        [6]     sha512
        [7]     sha3_224
        [8]     sha3_256
        [9]     sha3_384
        [10]    sha3_512
        [11]    shake_128
        [12]    shake_256
        [13]    blake2b
        [14]    blake2s

    Enter the hash type [1-14]:""")
    hash = input(">> ")
    try:
        while int(hash) < 1 or int(hash) > 14:
            print(hash, any(hash))
            print("Enter the hash type [1-14]:")
            hash = input(">> ")
    except(ValueError):
        print("        -Invalid value-        ")
        main_menu.main_menu()
    else:
        hash_tools.encrypt_hash(hash, password)

def decrypt_option():
    print("""   
        Enter the hash type [1-2]:                 Type "back" to return.
    
        [1]     Enter the hash
        [2]     Select a hash list [.txt]
        """)
    option = input(">> ")
    if option == "1":
        print("Enter the hash:")
        hash = input(">> ")
        hash_tools.decrypt_hash(hash)
    elif option == "2":
        hash_tools.decrypt_hashlist()
    elif option == "back":
        main_menu.main_menu()
    else:
        decrypt_option()
