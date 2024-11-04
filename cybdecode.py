import os
import sys

Version = '0.0.3'

try:
    from colorama import Fore, Back, Style
    g = Fore.GREEN
    r = Fore.RED
    m = Fore.MAGENTA
    y = Fore.YELLOW
    res = Style.RESET_ALL
except ImportError:
    print('[-] Cannot find module colorama')
    print('[*] Install by pip install colorama')
    sys.exit()

class cybdecode:
    def __init__(self):
        self.clscr()
        self.option()
        choice = int(input(y + 'Choose from the options above > '))
        if choice == 1:
            self.enc_alph()
        elif choice == 2:
            self.dec_alph()
        elif choice == 3:
            exit()
        else:
            print(r + 'Wrong Choice')

    def option(self):
        print(m + """
                                        CYBDECODE
                            <<< Run by - python cybdecode.py >>>
                                    <<< By Cyb3r3x3r >>>
            |-----------------------------"""+y+"""---------------------------------------|
            | 1 = encrypt message by alphabet cipher                             |
            | 2 = decrypt message by alphabet """+g+"""cipher                             |
            | 3 = exit                                                           |
            |--------------------------------------------------------------------| """+res)

    def clscr(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux, windows][os.name == 'nt'])

    def enc_alph(self):
        enc_msg = ''
        msg = input(y + 'Enter the message to encrypt > ')
        enc_key = int(input(y + 'Enter the encryption key > '))
        print(y + 'How do you want to encrypt?')
        print(y + '1. Forward (addition) to alphabets')
        print(y + '2. Backward (subtraction) to alphabets')
        print(y + '3. One addition One subtraction')
        msg_len = len(msg)
        choose = int(input('> '))
        if choose == 1:
            for x in range(0, msg_len):
                if not msg[x] == ' ':
                    iden = ord(msg[x])
                    iden2 = iden + enc_key
                    enc_msg += chr(iden2)
                else:
                    enc_msg += msg[x]
            print(g + 'Message Encrypted > ' + enc_msg + res)
        elif choose == 2:
            for x in range(0, msg_len):
                if not msg[x] == ' ':
                    iden = ord(msg[x])
                    iden2 = iden - enc_key
                    enc_msg += chr(iden2)
                else:
                    enc_msg += msg[x]
            print(g + 'Message Encrypted > ' + enc_msg + res)
        elif choose == 3:
            for x in range(0, msg_len):
                if not msg[x] == ' ':
                    iden = ord(msg[x])
                    if x % 2 == 0:
                        iden2 = iden + enc_key
                    else:
                        iden2 = iden - enc_key
                    enc_msg += chr(iden2)
                else:
                    enc_msg += msg[x]
            print(g + 'Message Encrypted > ' + enc_msg + res)
        else:
            print(r + 'Wrong Choice')

    def dec_alph(self):
        msg1 = input(y + 'Enter the encrypted message > ')
        print(y + 'How do you want to decrypt?')
        print(y + '1. Backward (subtraction) to alphabets (if addition done during encryption)')
        print(y + '2. Forward (addition) to alphabets (if subtraction done during encryption)')
        print(y + '3. One addition One subtraction')
        print(y + '4. Try all possible keys (decryption key not known)')
        choose1 = int(input('> '))
        if choose1 == 1:
            dec_key = int(input(y + 'Enter the decryption key > '))
            self.back_dec(dec_key, msg1)
        elif choose1 == 2:
            dec_key = int(input(y + 'Enter the decryption key > '))
            self.for_dec(dec_key, msg1)
        elif choose1 == 3:
            dec_key = int(input(y + 'Enter the decryption key > '))
            self.one_add_one_sub_dec(dec_key, msg1)
        elif choose1 == 4:
            self.try_all_keys(msg1)
        else:
            print(r + 'Wrong Choice' + res)

    def back_dec(self, dkey, dmsg):
        dec_msg = ''
        for char in dmsg:
            if char != ' ':
                iden = ord(char)
                iden2 = iden - dkey
                dec_msg += chr(iden2)
            else:
                dec_msg += char
        print(g + 'Message Decrypted > ' + dec_msg + res)

    def for_dec(self, dkey, dmsg):
        dec_msg = ''
        for char in dmsg:
            if char != ' ':
                iden = ord(char)
                iden2 = iden + dkey
                dec_msg += chr(iden2)
            else:
                dec_msg += char
        print(g + 'Message Decrypted > ' + dec_msg + res)

    def one_add_one_sub_dec(self, dkey, dmsg):
        dec_msg = ''
        for x in range(len(dmsg)):
            if dmsg[x] != ' ':
                iden = ord(dmsg[x])
                if x % 2 == 0:
                    iden2 = iden - dkey  # Reverse addition
                else:
                    iden2 = iden + dkey  # Reverse subtraction
                dec_msg += chr(iden2)
            else:
                dec_msg += dmsg[x]
        print(g + 'Message Decrypted > ' + dec_msg + res)

    def try_all_keys(self, dmsg):
        with open('possible_decryptions.txt', 'w') as f:
            for key in range(1, 26):  # Trying keys from 1 to 25
                dec_msg = ''
                for char in dmsg:
                    if char != ' ':
                        iden = ord(char)
                        iden2 = iden - key  # Assuming backward decryption
                        dec_msg += chr(iden2)
                    else:
                        dec_msg += char
                f.write(f'Key {key}: {dec_msg}\n')
            print(g + f'All possible decryptions saved to possible_decryptions.txt' + res)

start = cybdecode()
