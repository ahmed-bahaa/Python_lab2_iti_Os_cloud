import csv
import pandas as pd
from create import *
from registeration import *
from login import *
from create import *
from search import *
from display import *
from delete import *

while (True):

    print ("Enter your choice from 1 to 2: ")
    print ("1- create account : ")
    print ("2- login : ")
    choice = raw_input("> ")

    if choice == "1" :
        ans = registeration()
        if ans :
                print("registeration done successfully!")
    elif  choice == "2" :
        user_name = login()
        print("login done successfully!")

        while (True) :
            print ("======================Menu==================")
            print ("Enter your choice from 1 to 2: ")
            print ("1- display projects ")
            print ("2- search projects ")
            print ("3- create projects ")
            print ("4- delete projects ")
            ch =  raw_input("Enter your choice from 1 to 4: ")
            if ch == "1" :
                    display();

            elif ch == "2" :
                    print ("1- delete by title : ")
                    print ("2- delete by date : ")
                    print ("Enter your choice from 1 to 2: ")
                    choice = raw_input("> ")

                    if choice == "1" :
                        search("title")
                    elif choice == "1":
                        search("date")
                    else:
                        print("wrong choice")

            elif ch == "3" :
                    response = create(user_name)

            elif ch == "4" :
                    delete(user_name)
                
