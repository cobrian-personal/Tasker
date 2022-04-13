import pyfiglet
import datetime
from tqdm import tqdm
from time import sleep
import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu
from utils.tasks import tasks
from utils.data import archiveFiles


"""
This will be the main running file for my personal task management software
The intitial functionality for this software will be a daily welcome message,
add pertinent dates, daily tasks for completion, etc. 
"""


def run():
    date = datetime.date.today()
    d2 = date.strftime("%B %d, %Y")
    
    helloMsg = "Welcome to the software. Today is " + d2

    fig = pyfiglet.Figlet()
    print(colored(fig.renderText(helloMsg), "magenta"))

    taskList = pd.read_csv("utils/data/tasks.csv")
    
    stopCode = True
    while stopCode:
        menuOptions = ["View All Tasks", "Add a Task", "Upcoming Tasks #TODO", "Mark Task Complete", "Quit"]

        #### TODO Edit Tasks, Goal Tracker, To do list, 
        menu = TerminalMenu(menuOptions)
        entry = menu.show()

        if entry == 0:
            tasks.showTasks(taskList)
        if entry == 1:
            taskList = tasks.taskEntry(taskList)
        if entry == 2:
            tasks.showUpcoming()
        if entry == 3:
            taskList = tasks.markComplete(taskList)
        if entry == 4:
            print("Saving Data...")
            archiveFiles.uploadTasks(taskList)
            stopCode = False




run()