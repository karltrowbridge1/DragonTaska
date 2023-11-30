#This class implements the main section of the TK interface UI.

# @author Group 6
from tkinter import *
#from control.DialogBox import DialogBox
from entity.TaskList import TaskList
from entity.Task import Task


class Window:
    def __init__(self):
        # Task List Creation
        self.list = TaskList()

        # Regular GUI creation stuff that reflects our PD1
        self.root = Tk()
        self.root.title("Dragon Taska'")
        self.label = Label(self.root, text="Taska'")

        # Button widgets
        self.add = Button(self.root, text="Add", command=self.openDialog)

        # pack the widgets into the window
        self.label.pack(pady=10)
        self.add.pack(pady=10)

    def addToList(self, task):
        self.list.makeTask(task)

    def openDialog(self):
        # Button Widgets
        self.cancel = Button(self.root, text="Cancel", command=self.destroyElements)
        self.submit = Button(self.root, text="Submit", command=self.submitTask)
  
        # Entry Widgets
        self.title = Entry(self.root, font=("Arial", 12))
        self.title.pack(side=LEFT)
        self.category = Entry(self.root, font=("Arial", 12))
        self.category.pack(side=LEFT)
        self.description = Entry(self.root, font=("Arial", 12))
        self.description.pack(side=LEFT)
        self.date = Entry(self.root, font=("Arial", 12))
        self.date.pack(side=LEFT)
        

        # pack the widgets into the window
        self.label.pack(pady=10)
        self.cancel.pack(pady=10)
        self.submit.pack(pady=10)

    def submitTask(self):
        myTask = Task(self.title.get(),         # create task object and get all the input
                       self.category.get(),
                       self.description.get(),
                       self.date.get())
        self.list.makeTask(myTask)              # add to the task list
        self.destroyElements()
        
    def destroyElements(self):
        self.title.destroy()
        self.category.destroy()
        self.description.destroy()
        self.date.destroy()
        self.cancel.destroy()
        self.submit.destroy()
        self.show_taskList(self.list)
        
        
        
    def show_window(self):
        self.root.mainloop()



    def show_taskList(self, myList):
        # delete any elements on screen
        for widget in self.root.winfo_children():
            if isinstance(widget, (Button, Label)):
                if widget.cget("text") != "Taska'" and widget.cget("text") != "Add":
                    widget.destroy()

        # re print elements on screen
        for idx, task in enumerate(myList.getTasks()):
            label = Label(self.root, text=f"Task {idx + 1}: {task.getTask()}")
            label.pack()

            # create a delete button for each label
            formatedtxt = ("Delete task:" + str(idx+1))
            delete_button = Button(self.root, text=formatedtxt, command=lambda index=idx: self.delete_task(myList, idx))
            delete_button.pack()
    
    def delete_task(self, myList, index):
        myList.delTask(index)
        self.show_taskList(myList)



#      Enter info into window
#      Display all of the tasks in TASK LIST
#      Add to the TASK LIST 
#      Enter info into window