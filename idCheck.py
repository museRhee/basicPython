#input id, password
idName = input("id? ")
password = input("password? ")

#id and pw are both whitin 10 letters
if len(idName) > 10 :
    print("register failure: id length is over 10char")
elif len(password) > 10 :
    print("register failure: pw length is over 10char")
else :
    print("successfully register")

        
