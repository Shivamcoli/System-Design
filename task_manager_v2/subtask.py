# subtask.py

class Subtask:
    def __init__(self, subtask_id):
        self.subtask_id = subtask_id
        self.description = input("Enter the description of the subtask: ")
        self.priority = input("Enter the priority of the subtask (Low, Medium, High): ")
        self.status = "Pending"

    def update_status(self, new_status):
        self.status = new_status
