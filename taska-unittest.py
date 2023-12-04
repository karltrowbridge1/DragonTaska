import unittest
from entity.Task import Task
from entity.TaskList import TaskList

class TestTaskApplication(unittest.TestCase):
    
    def test_taskAdd(self):
        testTask = Task("Test title", "Test category", "Test description", "Test date")
        testList = TaskList()
        testList.makeTask(testTask)
        returnedList = testList.getTasks()
        exceptedOutput = "('Test title', 'Test category', 'Test description', 'Test date')"     
        self.assertEqual(str(returnedList[0].getTask()), exceptedOutput)

    def test_taskDelete(self):
        # Create Task and Task List objects
        testTask = Task("Test title", "Test category", "Test description", "Test date")
        testTaskTwo = Task("Test title2", "Test category2", "Test description2", "Test date2")
        testList = TaskList()

        # Add tasks to the list
        testList.makeTask(testTask)
        testList.makeTask(testTaskTwo)

        # Delete the first Task from the Task List
        testList.delTask(0)

        # Return the task, and test if the second Task is still in the List
        returnedList = testList.getTasks()
        exceptedOutput = "('Test title2', 'Test category2', 'Test description2', 'Test date2')"     
        self.assertEqual(str(returnedList[0].getTask()), exceptedOutput)

if __name__ == "__main__":
    unittest.main()
