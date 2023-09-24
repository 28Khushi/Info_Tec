#TO DO LIST PROJECT 
import pickle

class Task:
    def __init__(self, title, description, status="To Do"):
        self.title = title
        self.description = description
        self.status = status

class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, title, description):
        task = Task(title, description)
        self.tasks.append(task)

    def delete_task(self, title):
        for task in self.tasks:
            if task.title == title:
                self.tasks.remove(task)
                print(f"Task '{title}' deleted.")
                return
        print(f"Task '{title}' not found in the to-do list.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the to-do list.")
        else:
            print("To-Do List:")
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. Title: {task.title}, Description: {task.description}, Status: {task.status}")

    def save_tasks(self, filename):
        try:
            with open(filename, 'wb') as file:
                pickle.dump(self.tasks, file)
            print(f'Tasks saved to {filename}.')
        except Exception as e:
            print(f'Error saving tasks: {e}')

    def load_tasks(self, filename):
        try:
            with open(filename, 'rb') as file:
                self.tasks = pickle.load(file)
            print(f'Tasks loaded from {filename}.')
        except FileNotFoundError:
            print(f'File {filename} not found. No tasks loaded.')
        except Exception as e:
            print(f'Error loading tasks: {e}')

if __name__ == "__main__":
    todo_list = ToDoList()

    while True:
        print("\nTodo List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. View Tasks")
        print("4. Save Tasks")
        print("5. Load Tasks")
        print("6. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            todo_list.add_task(title, description)
        elif choice == "2":
            title = input("Enter the title of the task to delete: ")
            todo_list.delete_task(title)
        elif choice == "3":
            todo_list.view_tasks()
        elif choice == "4":
            filename = input("Enter filename to save tasks: ")
            todo_list.save_tasks(filename)
        elif choice == "5":
            filename = input("Enter filename to load tasks: ")
            todo_list.load_tasks(filename)
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")
