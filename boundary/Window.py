#This class implements the main section of the TK interface UI.

# @author Group 6
from tkinter import *
#from control.DialogBox import DialogBox
from entity.TaskList import TaskList
from entity.Task import Task


class Window:
    def __init__(self):
        self.list = TaskList()
        self.root = Tk()
        self.root.title("Dragon Taska'")
        self.label = Label(self.root, text="Taska'")
        self.root.minsize(600, 900)
        self.root.config(bg="#D2B48C")

        self.color_options = ["lightblue", "#D2B48C", "pink", "grey"]
        self.current_color_index = 0

        # Button widgets
        self.change_color = Button(self.root, text="Change Color", command=self.changeColor)
        self.add = Button(self.root, text="Add", command=self.openDialog)

        # pack the widgets into the window
        self.label.pack(pady=10)
        # Centered change_color button to the left of add button
        self.change_color.pack(side="right", anchor="se", pady=10, padx=5)
        
        # Centered add button in the bottom right corner
        self.add.pack(side="right", anchor="se", pady=10, padx=10)
        

    def addToList(self, task):
        self.list.makeTask(task)

    def openDialog(self):
        # Hide the add button to stop potential double clicks
        self.add.pack_forget()

        # Button Widgets
        self.cancel = Button(self.root, text="Cancel", command=self.destroyElements)
        self.submit = Button(self.root, text="Submit", command=self.submitTask)

        self.cancel.pack(side="right", anchor="ne", pady=10, padx=10)
        self.submit.pack(side="right", anchor="ne", pady=10, padx=10)

        # Entry Widgets
        self.title = Entry(self.root, font=("Arial", 12))
        self.title.pack(side="left")
        self.category = Entry(self.root, font=("Arial", 12))
        self.category.pack(side="left")
        self.description = Entry(self.root, font=("Arial", 12))
        self.description.pack(side="left")
        self.date = Entry(self.root, font=("Arial", 12))
        self.date.pack(side="left")
        
          # Enter descriptive text into the entry boxes
        self.title.insert(0, "title")
        self.category.insert(0, "category")
        self.description.insert(0, "description")
        self.date.insert(0, "date")

        # Define entry_clear_title
        def entry_clear_title(e):
            if self.title.get() == 'title':
                self.title.delete(0, END)

        # Define entry_clear_category
        def entry_clear_category(e):
            if self.category.get() == 'category':
                self.category.delete(0, END)
        
        # Define entry_clear_description
        def entry_clear_description(e):
            if self.description.get() == 'description':
                self.description.delete(0, END)
        
        # Define entry_clear_date
        def entry_clear_date(e):
            if self.date.get() == 'date':
                self.date.delete(0, END)
                
        # Bind the entry boxes
        self.title.bind("<Button-1>",entry_clear_title)
        self.category.bind("<Button-1>", entry_clear_category)
        self.description.bind("<Button-1>", entry_clear_description)
        self.date.bind("<Button-1>", entry_clear_date)

        # Define entry_add_title
        def entry_add_date(e):
            if self.title.get() == '':
                self.title.insert(0, "title", END)
            
        # Define entry_add_category
        def entry_add_category(e):
            if self.cateory.get() == '':
                self.category.insert(0, "category", END)

        # Define entry_add_description
        def entry_add_description(e):
            if self.description.get() == '':
                self.description.insert(0, "description", END)

        # Define entry_add_date
        def entry_add_date(e):
            if self.date.get() == '':
                self.date.insert(0, "date", END)

        # pack the widgets into the window
        self.label.pack(pady=10)

    def submitTask(self):
        myTask = Task(self.title.get(),         # create task object and get all the input
                       self.category.get(),
                       self.description.get(),
                       self.date.get())
        self.list.makeTask(myTask)              # add to the task list
        self.destroyElements()

        # re pack the button
        self.add.pack(side="right", anchor="se", pady=10, padx=10)
        
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
                if widget.cget("text") != "Taska'" and widget.cget("text") != "Add" and widget.cget("text") != "Change Color":
                    widget.destroy()

        # re print elements on screen
        for idx, task in enumerate(myList.getTasks()):
            label = Label(self.root, text=f"Task {idx + 1}: {task.getTask()}")
            label.pack()

            # create a delete button for each label
            formatedtxt = ("Delete task: " + str(idx+1))
            delete_button = Button(self.root, text=formatedtxt, command=lambda index=idx: self.delete_task(myList, idx))
            delete_button.pack()
    
    def delete_task(self, myList, index):
        myList.delTask(index)
        self.show_taskList(myList)

    def changeColor(self):

        # Get the next color from the list
        next_color = self.color_options[self.current_color_index]

        # Increment the color index for the next cycle
        self.current_color_index = (self.current_color_index + 1) % len(self.color_options)

        # Change the background color of the window
        self.root.config(bg=next_color)

