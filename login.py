import re , csv
import phonenumbers
import pandas as pd

def login():

    confirmed = False
    valid_email = False
    user_index=-1

    #load email column
    df_email = pd.read_csv("db/users.csv" , header=None, usecols=[2])

    #load password column
    df_pass = pd.read_csv("db/users.csv" , header=None, usecols=[3] , dtype=str)

    #bring user name
    owners = pd.read_csv("db/users.csv" , header=None, usecols=[0] , dtype=str)


    # email validaion
    while( not valid_email ):
        Email = raw_input("Enter your email: ")

        emails= df_email.ix[:,:].values
        for k,i in enumerate(emails):
            if i == Email :
                print('exist')
                valid_email = True
                user_index = k
                user_name = owners.ix[k,:].values
                break

        if not valid_email:
    		print("wrong email")

    # password
    while( not confirmed ):
        Password = raw_input("Enter your password: ")

        passwords= df_pass.ix[k,:].values
        print(passwords)
        if passwords == Password :
                print('exist')
                confirmed = True
                break

        else:
    		print("wrong password")


    return user_name[0]
