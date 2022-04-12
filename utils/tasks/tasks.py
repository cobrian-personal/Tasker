from pandas import *
from simple_term_menu import TerminalMenu
import datetime


def taskEntry(taskList):    
    print()
    print("When is the task due to be completed?\n")
    menuOptions = ["Today", "Other", "Cancel"]
    menu = TerminalMenu(menuOptions)
    entry = menu.show()

    if entry==0:
        date = datetime.date.today().strftime("%m/%d/%y")
    elif entry==1:
        date = input("Input a date in the format MM/DD/YY: ")
        x = date.split('/')
        date = datetime.datetime(int(x[2]),int(x[0]),int(x[1]))
        date = date.strftime("%m/%d/%y")
    elif entry==2:
        return taskList
    
    title = input("Give the task a name: ")
    menuOptions1 = ["Schoolwork", "Work", "Leisure", "Personal", "Other"]
    menu1 = TerminalMenu(menuOptions1)
    entry1 = menu1.show()
    label = menuOptions1[entry1]
    notes = input("Task Notes: ")
    id = len(taskList.index) + 1
    created = datetime.date.today().strftime("%m/%d/%y")
    complete = False

    newFrame = {
                "ID":id,
                "Task Name" : title,
                "Due Date": date,
                "Notes" : notes,
                "Label" : label,
                "Created" : created,
                "Complete" : complete
                }
    
    taskList.columns = taskList.columns.str.strip()

    taskList = taskList.append(newFrame, ignore_index = True)

    print()

    return taskList


def showTasks(taskList):
    taskList.columns = taskList.columns.str.strip()
    taskList['Due Date'] = to_datetime(taskList['Due Date'])
    taskList = taskList.sort_values(by='Due Date')
    print('\nShowing tasks in order of due date....\n')
    print(taskList)
    print('\n')
    

def showUpcoming():
    print("Upcoming")
