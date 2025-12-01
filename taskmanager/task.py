class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        self.title = input("Enter task title: ")
        self.description = input("Enter task description: ")
        self.priority = input("Enter task priority (Low/Medium/High): ")
        self.date = input("Enter due date (YYYY-MM-DD): ")
        self.author = input("Enter author name: ")
        self.status = "Not Started"

    def update_status(self, new_status):
        self.status = new_status
