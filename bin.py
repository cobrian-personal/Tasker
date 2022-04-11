import pyfiglet
import datetime
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

    stopCode = True
    while stopCode:
        menuOptions = ["View Today's Tasks", "Add a Task", "Upcoming Tasks", "Quit"]
        menu = TerminalMenu(menuOptions)
        entry = menu.show()

        if entry == 0:
            tasks.showTasks()
        if entry == 1:
            tasks.taskEntry()
        if entry == 2:
            tasks.showUpcoming()
        if entry == 3:
            print("Saving Data...")
            archiveFiles.uploadTasks()
            stopCode = False




run()