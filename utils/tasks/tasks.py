from pandas import *
from simple_term_menu import TerminalMenu
import datetime
from termcolor import colored



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
        print()
        print("==================================================================================================================================")
        print()
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
    print("==================================================================================================================================")
    print()

    return taskList


def showTasks(taskList):
    taskList.columns = taskList.columns.str.strip()
    taskList['Due Date'] = to_datetime(taskList['Due Date'])
    taskList = taskList.sort_values(by=['Complete','Due Date'])
    print('\nShowing tasks in order of due date (Green = Complete, Cyan = IP)\n')
    t = taskList[taskList.Complete == False].filter(items=["Task Name", "Due Date", "Label", "Notes"])
    print(colored(t,"cyan"))
    print()
    t1 = taskList[taskList.Complete == True].filter(items=["Task Name", "Due Date", "Label", "Notes"])
    print(colored(t1,"green"))
    print()
    print("==================================================================================================================================")
    print()
    
def showUpcoming(taskList):
    today = datetime.date.today().strftime("%Y-%m-%d")
    t2 = taskList[taskList["Due Date"] == today][taskList.Complete==False].filter(items=["Task Name", "Due Date", "Label", "Notes"])
    print(colored(t2,"yellow"))
    print()
    t3 = taskList[taskList["Due Date"] == today][taskList.Complete==True].filter(items=["Task Name", "Due Date", "Label", "Notes"])
    print(colored(t3,"green"))
    print()
    print("==================================================================================================================================")
    print()

def markComplete(taskList):
    print()
    print("Tasks that are incomplete: \n")
    options =["Back"]
    t = taskList.to_dict('list')
    count = 0
    for i in t["Task Name"]:
        if t["Complete"][count] == False:
            options = [str(t["ID"][count]) + " : " + i + " : " + t["Label"][count]] + options
        count+=1    
    menu = TerminalMenu(options)
    entry = menu.show()

    if entry == len(options) -1:
        return taskList

    id = int(options[entry].split(" : ")[0].strip())
    for i in range(len(t["ID"])):
        if t["ID"][i] == id:
            t["Complete"][i] = True

    # print(t)
    print()
    print("==================================================================================================================================")
    print()

    return DataFrame(t)
    

