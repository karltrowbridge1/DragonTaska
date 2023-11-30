#This class implements the Task object with the attributes of title, 
#category, description, and date. It will also include a getter and setter method pair.

# @author Group 6


class Task:
    def __init__(self, title, category, description, date):
        self.title = title
        self.category = category
        self.description = description
        self.date = date

    def getTask(self):
        return self.title, self.category,  self.description, self.date
    