# To-Do List Application finished

class ToDoList:
    def __init__(self):
        self.tasks = []

    def show_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("\nYour To-Do List:")
            for index, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Incomplete"
                print(f"{index}. {task['title']} - {status}")
            print()

    def add_task(self, title):
        task = {"title": title, "completed": False}
        self.tasks.append(task)
        print(f"Task '{title}' added to the list.\n")

    def update_task(self, task_number, new_title):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["title"] = new_title
            print(f"Task {task_number} updated to '{new_title}'.\n")
        else:
            print("Invalid task number.\n")

    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            removed_task = self.tasks.pop(task_number - 1)
            print(f"Task '{removed_task['title']}' removed from the list.\n")
        else:
            print("Invalid task number.\n")

    def mark_completed(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            print(f"Task {task_number} marked as completed.\n")
        else:
            print("Invalid task number.\n")


def display_menu():
    print("To-Do List Menu:")
    print("1. View tasks")
    print("2. Add a task")
    print("3. Update a task")
    print("4. Delete a task")
    print("5. Mark a task as completed")
    print("6. Exit")


def main():
    to_do_list = ToDoList()

    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            to_do_list.show_tasks()
        elif choice == "2":
            title = input("Enter task title: ")
            to_do_list.add_task(title)
        elif choice == "3":
            to_do_list.show_tasks()
            task_number = int(input("Enter task number to update: "))
            new_title = input("Enter new title: ")
            to_do_list.update_task(task_number, new_title)
        elif choice == "4":
            to_do_list.show_tasks()
            task_number = int(input("Enter task number to delete: "))
            to_do_list.delete_task(task_number)
        elif choice == "5":
            to_do_list.show_tasks()
            task_number = int(input("Enter task number to mark as completed: "))
            to_do_list.mark_completed(task_number)
        elif choice == "6":
            print("Exiting To-Do List application. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()
