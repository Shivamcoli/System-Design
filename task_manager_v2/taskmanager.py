from task import Task

class TaskManager:
    def __init__(self):
        self.tasks = []               # list of Task instances
        self.task_id_counter = 1

    def add_task(self):
        # create Task instance (give it the id)
        t = Task(self.task_id_counter)

        # optionally let user add multiple subtasks now
        while True:
            ans = input("Add a subtask now? (y/n): ").strip().lower()
            if ans == 'y':
                t.add_subtask()
            else:
                break

        # store the Task instance (or (id, t) if you prefer tuples)
        self.tasks.append((t.task_id, t))   # storing tuple is fine; keep consistent
        print(f"Task {t.task_id} added.")
        self.task_id_counter += 1

    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
            return
        for task_id, task in self.tasks:
            print(f"Task ID: {task_id}, Title: {task.title}")
            task.view_subtasks()

    def add_subtask(self, task_id):
        for t_id, task in self.tasks:
            if t_id == task_id:
                # allow adding multiple subtasks if desired
                while True:
                    task.add_subtask()
                    more = input("Add another subtask to this task? (y/n): ").strip().lower()
                    if more != 'y':
                        break
                return
        print(f"Task ID: {task_id} not found")

    def update_task_subtask_status(self, task_id, subtask_id, new_status):
        for t_id, task in self.tasks:
            if t_id == task_id:
                task.update_subtask_status(subtask_id, new_status)
                return
        print(f"Task ID: {task_id} not found")
if __name__ == "__main__":
    manager = TaskManager()
    while True:
        print("\n1. Add Task\n2. View Tasks\n3. Update Subtask Status\n4. Create Subtask for Task\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            manager.add_task()
        elif choice == '2':
            manager.view_tasks()
        elif choice == '3':
            t_id = int(input("Enter Task ID: "))
            s_id = int(input("Enter Subtask ID: "))
            new_status = input("Enter new status (Pending, In Progress, Completed): ")
            manager.update_task_subtask_status(t_id, s_id, new_status)
        elif choice == '4':
            t_id = int(input("Enter Task ID: "))
            manager.add_subtask(t_id)
        elif choice == '5':
            break
        else:
            print("Invalid choice. Please try again.")
