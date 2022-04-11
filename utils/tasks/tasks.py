from pandas import *

def taskEntry():    
    print("You found me")
    #TODO

def showTasks(taskList):
    taskList.columns = taskList.columns.str.strip()
    taskList = taskList.sort_values(by='Due Date', axis='index', ascending=True)
    print('\nShowing tasks in order of date....\n')
    print(taskList)
    print('\n')
    

def showUpcoming():
    print("Upcoming")
