import re , csv
import phonenumbers
import pandas as pd

def display():

    print("=====================projects========================")

    try:
            df_email = pd.read_csv("db/projects.csv" , header = None )

            df_email.rename(columns={0:"owner" , 1:"title" , 2:"details" , 3:"total" , 4:"start" , 5:"end" }, inplace=True)

            print(df_email)
    except Exception as e:
            print ("empty file")
