class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task '{task}' added!")

    def delete_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            print(f"Task '{task}' deleted!")
        else:
            print(f"Task '{task}' not found!")

    def mark_done(self, task):
        if task in self.tasks:
            self.tasks[self.tasks.index(task)] = f"[X] {task}"
            print(f"Task '{task}' marked as done!")
        else:
            print(f"Task '{task}' not found!")

    def list_tasks(self):
        if not self.tasks:
            print("To-Do List is empty!")
        else:
            for i, task in enumerate(self.tasks, 1):
                print(f"{i}. {task}")

def main():
    todo_list = TodoList()

    while True:
        print("\nTo-Do List Menu:")
        print("1. Add Task")
        print("2. Delete Task")
        print("3. Mark Task as Done")
        print("4. List Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task = input("Enter task: ")
            todo_list.delete_task(task)
        elif choice == "3":
            task = input("Enter task: ")
            todo_list.mark_done(task)
        elif choice == "4":
            todo_list.list_tasks()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!")

if __name__ == "__main__":
    main()