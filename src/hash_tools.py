import hashlib
import os
import hash_menu

def encrypt_hash(hash, password):
    password = password.encode()

    if hash == "1":
        md5 = hashlib.md5(password).hexdigest()
        print("\nMD5 -->  ", md5)
    elif hash == "2":
        sha1 = hashlib.sha1(password).hexdigest()
        print("\nSHA1 -->  ", sha1)
    elif hash == "3":
        sha224 = hashlib.sha224(password).hexdigest()
        print("\nSHA224 -->  ", sha224)
    elif hash == "4":
        sha256 = hashlib.sha256(password).hexdigest()
        print("\nSHA256 -->  ", sha256)
    elif hash == "5":
        sha384 = hashlib.sha384(password).hexdigest()
        print("\nSHA384 -->  ", sha384)
    elif hash == "6":
        sha512 = hashlib.sha512(password).hexdigest()
        print("\nSHA512 -->  ", sha512)
    elif hash == "7":
        sha3_224 = hashlib.sha3_224(password).hexdigest()
        print("\nSHA3_224 -->  ", sha3_224)
    elif hash == "8":
        sha3_256 = hashlib.sha3_256(password).hexdigest()
        print("\nSHA3_256 -->  ", sha3_256)
    elif hash == "9":
        sha3_384 = hashlib.sha3_384(password).hexdigest()
        print("\nSHA3_384 -->  ", sha3_384)
    elif hash == "10":
        sha3_512 = hashlib.sha3_512(password).hexdigest()
        print("\nSHA3_512 -->  ", sha3_512)
    elif hash == "11":
        print("\nDont work")
        hashlib.shake_128(password).hexdigest(20)
    elif hash == "12":
        print("\nDont work")
        hashlib.shake_256(password).hexdigest(20)
    elif hash == "13":
        blake2b = hashlib.blake2b(password).hexdigest()
        print("\nBLAKE2B -->  ", blake2b)
    elif hash == "14":
        blake2s = hashlib.blake2s(password).hexdigest()
        print("\nBLAKE2S -->  ", blake2s)


def decrypt_hash(hash):
    passwordlist = passwords_list()
    hashfounded = False
    print("Searching...\n")
    if os.stat("../dictionaries/passwords/" + passwordlist).st_size != 0:
        with open("../dictionaries/passwords/" + passwordlist, errors="ignore") as diccionary:
            for password in diccionary:
                if hashfounded is False:
                    passwordencode = password.encode().rstrip()
                    if hash == hashlib.md5(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha1(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha224(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha256(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha384(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha512(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha3_224(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha3_256(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha3_384(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.sha3_512(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.blake2b(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
                    elif hash == hashlib.blake2s(passwordencode).hexdigest():
                        credentials(hash, password)
                        hashfounded = True
        print("- Search finished -")
    else:
        print("- ", passwordlist, " empty -")


def decrypt_hashlist():
    hashlist = hashes_list()
    passwordlist = passwords_list()
    print("Searching...\n")
    if os.stat("../dictionaries/hashes/" + hashlist).st_size != 0:
        if os.stat("../dictionaries/passwords/" + passwordlist).st_size != 0:
            with open("../dictionaries/hashes/" + hashlist, errors="ignore") as diccionaryhashes:
                for hash in diccionaryhashes:
                    with open("../dictionaries/passwords/" + passwordlist, errors="ignore") as diccionarypasswords:
                        hash = hash.rstrip()
                        for password in diccionarypasswords:
                            passwordencode = password.encode().rstrip()
                            if hash == hashlib.md5(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha1(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha224(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha256(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha384(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha512(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha3_224(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha3_256(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha3_384(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.sha3_512(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.blake2b(passwordencode).hexdigest():
                                credentials(hash, password)
                            elif hash == hashlib.blake2s(passwordencode).hexdigest():
                                credentials(hash, password)
            print("- Search finished -")
        else:
            print("- ",passwordlist," empty -")
    else:
        print("- ",hashlist," empty -")

def hashes_list():
    listfiles = os.listdir("../dictionaries/hashes")
    x = 0
    print("\nChoose an dictionary: [0-" + str(int(len(listfiles)) - 1) + "]")
    for file in listfiles:
        print("        [" + str(x) + "] ", file)
        x = x + 1
    option = input(">> ")
    try:
        if int(option) > x or int(option) < 0:
            print("Dictionary (DEFAULT) HASHES.txt")
            return listfiles[0]
        else:
            return listfiles[int(option)]
    except ValueError:
        print("        -Invalid value-        ")
        hash_menu.decrypt_option()


def passwords_list():
    listfiles = os.listdir("../dictionaries/passwords")
    x = 0
    print("\nChoose an dictionary: [0-" + str(int(len(listfiles)) - 1) + "]")
    for file in listfiles:
        print("        [" + str(x) + "] ", file)
        x = x + 1
    option = input(">> ")
    try:
        if int(option) > x or int(option) < 0:
            print("Dictionary (DEFAULT) PASSWORDS.txt")
            return listfiles[0]
        else:
            return listfiles[int(option)]
    except ValueError:
        print("        -Invalid value-        ")
        hash_menu.decrypt_option()


def credentials(hash, password):
    print("HASH         -->     ", hash)
    print("PASSWORD     -->     ", password.rstrip(),"\n")

