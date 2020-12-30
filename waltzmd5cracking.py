print("THIS PROGRAM IS INTENDED FOR PASSWORD CRACKING")
print("THIS PROGRAM IS FOR EDUCATIONAL PURPOSE ONLY")
print("CREATED BY: WALTZ")

import hashlib
flag = 0
pass_hash = input("ILAGAY ANG MD5 HASH NA GUSTONG ICRACK: ")
wordlist = input("PANGALANG NG WORDLIST FILE: ")

try:
    pass_file = open(wordlist, 'r')
except:
    print("No File Found")
    quit()

for word in pass_file:

    enc_wrd = word.encode('utf-8')
    digest = hashlib.md5(enc_wrd.strip()).hexdigest()

    if digest == pass_hash:
        print("ANG PASSWORD AY NATAGPUAN")
        print("ANG PASSWORD AY " + word)
        flag = 1
        break
if flag == 0:
    print("ANG PASSWORD AY WALA SA WORDLIST")
