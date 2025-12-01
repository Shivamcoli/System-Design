from task import Task
class TaskManager:
    def __init__(self):
        self.tasks = []
        self.task_id_counter = 1

    def add_task(self):
        newtask = Task(self.task_id_counter)
        self.task_id_counter += 1
        self.tasks.append(newtask)
        print(f"Task {newtask.task_id} added.")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for t in self.tasks:
            print(f"Task ID: {t.task_id}, Title: {t.title}, Description: {t.description}, "
                  f"Priority: {t.priority}, Due Date: {t.date}, Author: {t.author}, Status: {t.status}")

    def update_task_status(self, task_id, new_status):
        for t in self.tasks:
            if t.task_id == task_id:
                t.update_status(new_status)
                print(f"Task ID {task_id} status updated to {new_status}.")
                return
        print(f"Task ID {task_id} not found.")


if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Task Status\n4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            manager.add_task()
        elif choice == "2":
            manager.view_tasks()
        elif choice == "3":
            try:
                task_id = int(input("Enter Task ID to update: ").strip())
            except ValueError:
                print("Invalid Task ID. Must be an integer.")
                continue
            new_status = input("Enter new status (Not Started/In Progress/Completed): ").strip()
            manager.update_task_status(task_id, new_status)
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")
