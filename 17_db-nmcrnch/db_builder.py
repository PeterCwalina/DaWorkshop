#Peter Cwalina, Jabir Chowdhury
#SoftDev1 pd0
#SQLITE3 BASICS
#2018-10-04

import sqlite3   #enable control of an sqlite database
import csv       #facilitates CSV I/O


DB_FILE="discobandit.db"

db = sqlite3.connect(DB_FILE) #open if file exists, otherwise create
c = db.cursor()               #facilitate db ops


command = "drop table if exists courses"
c.execute(command)
command = "CREATE TABLE courses(code TEXT,mark INTEGER, id INTEGER);"          
c.execute(command)    

with open('raw/courses.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        params = (str(row['code']), str(row['mark']),str(row['id']))
        command = "INSERT INTO courses VALUES(\'%s\',%s,%s);" % params
        c.execute(command)
command = "drop table if exists occupations"
c.execute(command)
command = "CREATE TABLE occupations(JobClass TEXT,Percentage FLOAT);"          
c.execute(command)

with open('raw/occupations.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        params = (str(row['Job Class']), str(row['Percentage']))
        command = "INSERT INTO occupations VALUES(\'%s\',%s);" % params
        c.execute(command)
command = "drop table if exists peeps"
c.execute(command)
command = "CREATE TABLE peeps(name TEXT,age INTEGER,id INTEGER);"          
c.execute(command)

with open('raw/peeps.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        params = (str(row['name']), str(row['age']),str(row['id']))
        command = "INSERT INTO peeps VALUES(\'%s\',%s,%s);" % params
        c.execute(command)

    


db.commit() #save changes
db.close()  #close database


