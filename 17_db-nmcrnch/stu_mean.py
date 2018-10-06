#The Cool Cids Club 
#SofDev1 pd 7
#K17 Average
#2018-10-06

import sqlite3

DB_FILE='discobandit.db'

db = sqlite3.connect(DB_FILE)
c = db.cursor()
#function time
#takes a students id spits out their grades
def lookUpGrades(id):
    command = 'SELECT mark FROM courses WHERE id = {0};'.format(str(id))
    c.execute(command)
    grades  = c.fetchall()
    return grades
#using id does the avg of the student
def computeAvg(id):
    grades = lookUpGrades(id)
    avg = 0
    for item in grades:
        avg+= item[0]

    avg = avg/len(grades)
    return avg


#prints all of the students data
def printStuNIA():
    command = 'SELECT name,id FROM peeps'
    c.execute(command)
    data = c.fetchall()
    for item in data:
        print(item[0],item[1],computeAvg(item[1]))
#returns a list of tuples of each stud entsid,and avg
def listStuIA():
    command = 'SELECT id FROM peeps'
    c.execute(command)
    data = c.fetchall()
    stuNIA =[]
    for item in data:
        stuNIA.append((item[0],computeAvg(item[0])))
    return stuNIA
#if table of id and avgs does not exist creates if it does it updates it
def updateIatbl():
    command = 'DROP TABLE if exists peeps_avg'
    c.execute(command)
    command = 'CREATE TABLE peeps_avg(id INTEGER,avg FLOAT);'
    c.execute(command)
    data = listStuIA()
    for item in data:
        command = 'INSERT INTO peeps_avg VALUES({0},{1});'.format(str(item[0]),str(item[1]))
        c.execute(command)
#adds to courses make note if you put in id of someone not in peeps they will be unaccounted for in the avgs table
def add2Courses(code,mark,id):
    #add the values
    command = 'INSERT INTO courses VALUES(\"{0}\",{1},{2});'.format(str(code),str(mark),str(id))
    c.execute(command)
    #update the id avg table accordingly
    updateIatbl()
    
        


#prints all of the students names ids and averages
printStuNIA()
#prints a students grades
print(lookUpGrades(1))
#creates student id avg table
updateIatbl()
#print it out
c.execute('SELECT id,avg FROM peeps_avg')
print(c.fetchall())
#lets add to the courses table
add2Courses('art',10,1)
#check the avgs table to see what changed
c.execute('SELECT id,avg FROM peeps_avg')
print(c.fetchall())


db.commit()
db.close()
