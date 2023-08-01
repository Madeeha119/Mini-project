class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print(f"Task '{task}' added to the to-do list.")

    def mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index]["completed"] = True
            print(f"Task '{self.tasks[task_index]['task']}' marked as completed.")
        else:
            print("Invalid task index.")

    def display_tasks(self):
        if not self.tasks:
            print("Your to-do list is empty.")
        else:
            print("Your to-do list:")
            for index, task in enumerate(self.tasks):
                status = "✔" if task["completed"] else "❌"
                print(f"{index + 1}. {status} {task['task']}")

def main():
    todo_list = ToDoList()

    while True:
        print("\nWhat would you like to do?")
        print("1. Add task")
        print("2. Mark task as completed")
        print("3. Display tasks")
        print("4. Exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            task_index = int(input("Enter the task index to mark as completed: ")) - 1
            todo_list.mark_completed(task_index)
        elif choice == "3":
            todo_list.display_tasks()
        elif choice == "4":
            print("Exiting the to-do list app. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
