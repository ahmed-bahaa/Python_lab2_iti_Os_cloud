import re , csv
import phonenumbers

def create(user):

    owner = user
    print("=====================create project========================")
    title = raw_input("Enter project title: ")
    details = raw_input("Enter project details: ")
    total = raw_input("Enter project total target: ")
    start = raw_input("Enter start date: ")
    end = raw_input("Enter end date: ")


    project = [ owner , title , details , total , start , end ]
    print(project)
    with open('db/projects.csv', 'ab') as writeFile:
        writer = csv.writer(writeFile)
        writer.writerow(project)
    print("Created successfully")
