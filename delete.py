import re , csv
import phonenumbers
import pandas as pd


def delete(user):

    finish = False
    owners = pd.read_csv("db/projects.csv" , header=None, usecols=[0] , dtype=str)
    owners_names=owners.ix[:,:].values
    print("=====================delete========================")
    while True:

        print ("1- delete by title : ")
        print ("2- delete by date : ")
        print ("Enter your choice from 1 to 2: ")
        choice = raw_input("> ")

        if choice == "1" :


            titles = pd.read_csv("db/projects.csv" , header=None, usecols=[1] , dtype=str)

            while( not finish ):
                project_name = raw_input("Enter project title: ")
                projects= titles.ix[:,:].values
                for k,i in enumerate(projects):
                    if i == project_name and user==owners_names[k]:
                        print('exist')
                        finish = True

                        proj = pd.read_csv("db/projects.csv" , header = None )
                        proj.rename(columns={0:"owner" , 1:"title" , 2:"details" , 3:"total" , 4:"start" , 5:"end" }, inplace=True)
                        print(proj.iloc[[k]])

                        proj.drop(proj.index[k], inplace=True)
                        print(proj)
                        proj.to_csv("db/projects.csv", header = None , index=False,sep=',')

                        return

                if not finish:
            		print("project not exist or your are not allowed to delete it")

        elif choice == "2" :


            start_dates = pd.read_csv("db/projects.csv" , header=None, usecols=[4] , dtype=str)

            while( not finish ):
                project_start_date = raw_input("Enter project start date: ")

                projects= start_dates.ix[:,:].values
                print(projects)
                for k,i in enumerate(projects):
                    if i == project_start_date and user==owners_names[k]:
                        print('exist')
                        finish = True


                        proj = pd.read_csv("db/projects.csv" , header = None )
                        proj.rename(columns={0:"owner" , 1:"title" , 2:"details" , 3:"total" , 4:"start" , 5:"end" }, inplace=True)
                        print(proj.iloc[[k]])

                        proj.drop([k])
                        proj.to_csv("db/projects.csv", sep=',' , index=False)

                        return

                if not finish:
            		print("project not exist or your are not allowed to delete it")
        else:
            print("wrong choice")
