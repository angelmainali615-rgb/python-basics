import json  #used to read or write data in json format 
import os    #used to check if file exists 


class Task:
    def __init__(self,title,status=False):
        self.title=title     #store task title(string)
        self.status=status   # Store task status (True/False)
    
    def convert_to_dict(self):
        # used to convert task object into dictionary 
        return 
        {"title":self.title,
         "status":self.status}
        
    # class to manage all task
class TaskManager:
        def __init__(self,filename="tasks.json"):
            self.filename=filename
            self.tasks=self.load_tasks() # Load tasks when program starts
        def load_tasks(self):
             # If file does not exist, return empty list
            if not  os.path.exists(self.filename):
                return []
            try:
                 # Open JSON file in read mode
                with open(self.filename,"r") as f:
                    data=json.load(f,indent=4)  # Load JSON data into Python list
                    tasks=[] # Empty list to store Task objects
                   #convert dictionary into task objects 
                    for item in data:
                        tasks.append(Task(item["title"] ,item["status"]))
            
                        return tasks
            
            except:
                return [] #return empty lists        
        def save_tasks(self):
            save_task=[] #list to store task dictionaries
             # Convert each Task object to dictionary
            for task in self.tasks:
                save_task.append(task.convert_to_dict()) 
                # Open file in write mode and save data
                with open(self.filename,"w") as f:
                    json.dump(save_task,f)
        def add_task(self,title):
            # Create new Task and add to list
            self.tasks.append(Task(title))
            self.save_tasks()  #save any changes to file 
            print("Task added ")
        def view_tasks(self):
             # If there are no tasks
            if not self.tasks:
                print("File not available")
                return 
             # Display each task with number and status
            for i, task in enumerate(self.tasks,start=1):
                status = "Done" if task.status else "Pending"

                print(f"{i} .{task.title} [{status}]")
                
        def delete_task(self,index):
            #check if index is valid
            if 0<=index <len(self.tasks):
                self.tasks.pop(index) #remove task from list 
                self.save_tasks()
                print("Task deleted")
            else:
                print("Invalid task number")
                
        def mark_complete(self,index):
            #check if index is valid
            if 0<= index<len(self.tasks):
                self.tasks[index].status=True #status is completed
                self.save_tasks()
                print("Task marked as complete")
            else:
                print("invalid task number")
# Main menu function
def main():
    manager = TaskManager()   # Create TaskManager object

    # Run menu until user exits
    while True:
        print("\n--- Smart Task Manager ---")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Delete Task")
        print("4. Mark Task Complete")
        print("5. Exit")

        choice = input("Enter your choice: ")
        if choice == "1":
            manager.view_tasks()

        elif choice == "2":
            title = input("Enter task title: ")
            manager.add_task(title)

        elif choice == "3":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to delete: ")) - 1
                manager.delete_task(index)
            except ValueError:
                print("Please enter a number.")

        elif choice == "4":
            manager.view_tasks()
            try:
                index = int(input("Enter task number to mark complete: ")) - 1
                manager.mark_complete(index)
            except ValueError:
                print("Please enter a number.")

        elif choice == "5":
            print("Exiting program.")
            break

        else:
            print("Invalid choice.")
            
# Program starts here
if __name__ == "__main__":
    main()   # Call main function