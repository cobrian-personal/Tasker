from pandas import*

def uploadTasks(taskList):
    # print(taskList)
    taskList.to_csv('utils/data/tasks.csv', index=False)
    print("Tasks uploaded")