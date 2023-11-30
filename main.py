#This file will house the main function of our code. It will create instances of all the other classes. It will eventually depend on TK inter.

# @author Group 6

from boundary.Window import Window
from entity.TaskList import TaskList

def main():

    # Create window
    window = Window()
    window.show_window()

if __name__ == "__main__":
    main()