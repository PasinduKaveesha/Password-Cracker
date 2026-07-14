import hashlib
#https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/Leaked-Databases/Ashley-Madison.txt

pass_filename = "passwordSet.txt"

password = "5f4dcc3b5aa765d61d8327deb882cf99"

enc_password = password.encode("utf-8")
password_hash = hashlib.md5(enc_password.strip()).hexdigest()

pass_file = open(pass_filename, "r")

for word in pass_file:
    enc_word = word.encode("utf-8")
    enc_hash = hashlib.md5(enc_word.strip()).hexdigest()

    if password_hash == enc_hash:
        print("you found the password sir. it's " + word)
        quit()

print("this password is quite hard to crack sir")