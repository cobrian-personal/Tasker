import pyfiglet
import datetime
from tqdm import tqdm
from time import sleep
import pandas as pd
from termcolor import colored
from simple_term_menu import TerminalMenu
from utils.tasks import tasks
from utils.data import archiveFiles

import warnings
warnings.filterwarnings("ignore")

import os
os.system('cls' if os.name == 'nt' else 'clear')


"""
This will be the main running file for my personal task management software
The intitial functionality for this software will be a daily welcome message,
add pertinent dates, daily tasks for completion, etc. 
"""


def run():
    date = datetime.date.today()
    d2 = date.strftime("%B %d, %Y")
    
    helloMsg = "Welcome to Tasker. Today is " + d2
    fig = pyfiglet.Figlet()
    print(colored(fig.renderText(helloMsg), "magenta"))

    print("                          ", end="")
    print(colored("Prepare for optimal productivity.", "grey", "on_white"))
    print()
    print("==================================================================================================================================")
    print()

    taskList = pd.read_csv("utils/data/tasks.csv")
    
    stopCode = True
    while stopCode:
        menuOptions = ["View All Tasks", "Show Incomplete Tasks", "Add a Task", "Tasks Due Today", "Mark Task Complete", "Move Task to Today", "Show Scrum Menu", "Quit"]

        #### TODO Edit Tasks, Goal Tracker, To do list, 
        menu = TerminalMenu(menuOptions)
        entry = menu.show()

        if entry == 0:
            tasks.showTasks(taskList)
        if entry == 1:
            tasks.showIncomplete(taskList)
        if entry == 2:
            taskList = tasks.taskEntry(taskList)
            archiveFiles.uploadTasks(taskList)
        if entry == 3:
            tasks.showUpcoming(taskList)
        if entry == 4:
            taskList = tasks.markComplete(taskList)
            archiveFiles.uploadTasks(taskList)
        if entry == 5:
            taskList = tasks.moveToToday(taskList)
            archiveFiles.uploadTasks(taskList)

        if entry == 6:
            tasks.showScrumMenu(taskList)

        if entry == 7:
            print("Saving Data...")
            archiveFiles.uploadTasks(taskList)
            stopCode = False




run()