#Developed By Cyb3r3x3r
import os
import sys

Version = '0.0.2'

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
        else:
            print(r + 'Wrong Choice')

    def option(self):
        print(m + """
                                        CYBDECODE
                            <<< Run by - python cybdecode.py >>>
                                    <<< By Cyb3r3x3r >>>
            |-----------------------------"""+y+"""---------------------------------------|
            | 1 = encrypt message by alphabet cipher                             |
            | 2 = decrypt message by alphabet """+g+"""cipher (decryption key known)      |
            | 3 = decrypt message by alphabet cipher (decryption key  not known) |
            |--------------------------------------------------------------------| """+res)
    def clscr(self):
        linux = 'clear'
        windows = 'cls'
        os.system([linux,windows][os.name == 'nt'])

    def enc_alph(self):
        enc_msg = ''
        msg = input(y + 'Enter the messagge to encrypt > ')
        enc_key = int(input(y + 'Enter the encryption key> '))
        print(y + 'How do you want to encrypt ?')
        print(y + '1. Forward (addition) to alphabets')
        print(y + '2. Backward (subtraction) to alphabets')
        print(y + '3. One addition One subtraction')
        msg_len = len(msg)
        choose = int(input('> '))
        if choose == 1:
            for x in range(0,msg_len):
                if not msg[x] == ' ':
                    iden = ord(msg[x])
                    iden2 = iden + enc_key
                    iden = iden2
                    enc_msg = enc_msg + chr(iden)
                else:
                    enc_msg = enc_msg + msg[x]
            print(g + 'Message Encrypted >  ' + enc_msg + res)
        elif choose == 2:
            for x in range(0,msg_len):
                if not msg[x] == ' ':
                    iden = ord(msg[x])
                    iden2 = iden - enc_key
                    iden = iden2
                    enc_msg = enc_msg + chr(iden)
                else:
                    enc_msg = enc_msg + msg[x]
            print(g + 'Message Encrypted >  ' + enc_msg + res)
        elif choose == 3:
            for x in range(0,msg_len):
                if not msg[x]==' ':
                    iden = ord(msg[x])
                    if x%2==0:
                        iden2 = iden + enc_key
                        iden = iden2
                        enc_msg = enc_msg + chr(iden)
                    else:
                        iden2 = iden - enc_key
                        iden = iden2
                        enc_msg = enc_msg + chr(iden)
                else:
                    enc_msg = enc_msg + msg[x]
            print(g + 'Message Encrypted > ' + enc_msg + res)
        else:
            print(r + 'Wrong Choice')
            
    def dec_alph(self):
        msg1 = input(y + 'Enter the encrypted message > ')
        dec_key = int(input(y + 'Enter the decryption key> '))
        print(y + 'How do you want to decrypt ?')
        print(y + '1. Backward (subtraction) to alphabets(if addition done during encryption)')
        print(y + '2. Forward (addition) to alphabets(if subtraction done during encryption)')
        print(y + '3. One addition One subtraction')
        msg_len1 = len(msg1)
        choose1 = int(input('> '))
        if choose1 == 1:
            self.back_dec(dec_key,msg1,msg_len1)
        elif choose1 == 2:
            self.for_dec(dec_key,msg1,msg_len1)
        else:
            print(r + 'Wrong Choice'+ res)

    def back_dec(self,dkey,dmsg,mlen):
        dec_msg = ''
        for x in range(0,mlen):
            if not dmsg[x] == ' ':
                iden = ord(dmsg[x])
                iden2 = iden - dkey
                iden = iden2
                dec_msg = dec_msg + chr(iden)
            else:
                dec_msg = dec_msg + dmsg[x]
        print(g + 'Message Decrypted >  ' + dec_msg + res)

    def for_dec(self,dkey,dmsg,mlen):
        dec_msg = ''
        for x in range(0,mlen):
            if not dmsg[x] == ' ':
                iden = ord(dmsg[x])
                iden2 = iden + dkey
                iden = iden2
                dec_msg = dec_msg + chr(iden)
            else:
                dec_msg = dec_msg + dmsg[x]
        print(g + 'Message Decrypted >  ' + dec_msg + res)

start = cybdecode()
start
