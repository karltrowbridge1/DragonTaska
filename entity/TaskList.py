#This class implements the Task list object and all of its methods such as 
#getTask() and getNextClass(). It is similar to an arraylist but as an object and for the Task objects. 
#It will also include a getter and setter method pair.


# @author Group 6


class TaskList:
    def __init__(self):
        self.list = []

    def getTasks(self):
        return self.list

    def makeTask(self,task): # self, task
        self.list.append(task)

    def delTask(self, index):
        self.list.pop(0)

    