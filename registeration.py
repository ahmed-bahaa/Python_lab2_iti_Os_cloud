import re , csv
import phonenumbers

def registeration():

    confirmed = False
    valid_phone = False
    print("=====================registeration========================")
    Fname = raw_input("Enter your First name: ")
    Lname = raw_input("Enter your Last name: ")
    Email = raw_input("Enter your email: ")

    while( not confirmed ):
        Password = raw_input("Enter your Password: ")
        Conf_Password = raw_input("Confirm your password: ")
        if  Password == Conf_Password :
            confirmed = True
        else :
            print("your password is not the same")


    while( not valid_phone ):
        phone = raw_input("Enter your phone number: ")
        x = phonenumbers.is_valid_number(phonenumbers.parse(phone, "EG"))
        if not x:
    		print("wrong phone number")
    	else:
    		valid_phone = True

    user = [ Fname , Lname , Email , Password , phone ]
    with open('db/users.csv', 'ab') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(user)

    return 1
