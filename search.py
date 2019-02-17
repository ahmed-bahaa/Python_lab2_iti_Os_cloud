import re , csv
import phonenumbers
import pandas as pd


def search(type):

    finish = False
    print("=====================Search========================")
    if type == "title":


        titles = pd.read_csv("db/projects.csv" , header=None, usecols=[1] , dtype=str)

        while( not finish ):
            project_name = raw_input("Enter project title: ")
            projects= titles.ix[:,:].values
            for k,i in enumerate(projects):
                if i == project_name :
                    print('exist')
                    finish = True
                    proj = pd.read_csv("db/projects.csv" , header = None )
                    proj.rename(columns={0:"owner" , 1:"title" , 2:"details" , 3:"total" , 4:"start" , 5:"end" }, inplace=True)
                    print(proj.iloc[[k]])

                    return

            if not finish:
        		print("project not exist")

    else:


        start_dates = pd.read_csv("db/projects.csv" , header=None, usecols=[4] , dtype=str)

        while( not finish ):
            project_start_date = raw_input("Enter project start date: ")

            projects= start_dates.ix[:,:].values
            print(projects)
            for k,i in enumerate(projects):
                if i == project_start_date :
                    print('exist')
                    finish = True
                    proj = pd.read_csv("db/projects.csv" , header = None )
                    proj.rename(columns={0:"owner" , 1:"title" , 2:"details" , 3:"total" , 4:"start" , 5:"end" }, inplace=True)
                    print(proj.iloc[[k]])

                    return

            if not finish:
        		print("project not exist")
