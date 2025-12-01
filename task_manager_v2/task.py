# task.py

from subtask import Subtask

class Task:
    def __init__(self, task_id):
        self.task_id = task_id
        self.subtask_list = []
        self.subtask_counter = 1
        self.title = input("Enter the title of the task: ")

    def add_subtask(self):
        new_subtask = Subtask(self.subtask_counter)
        self.subtask_list.append(new_subtask)
        self.subtask_counter += 1
        print(f"Subtask {new_subtask.subtask_id} added to Task '{self.title}'.")
        return new_subtask

    def view_subtasks(self):
        if not self.subtask_list:
            print("  No subtasks.")
            return
        for subtask in self.subtask_list:
            print(f"  Subtask ID: {subtask.subtask_id}, Description: {subtask.description}, "
                  f"Priority: {subtask.priority}, Status: {subtask.status}")

    def update_subtask_status(self, subtask_id, new_status):
        for subtask in self.subtask_list:
            if subtask.subtask_id == subtask_id:
                subtask.update_status(new_status)
                print(f"Subtask ID: {subtask_id} status updated to {new_status}")
                return
        print(f"Subtask ID: {subtask_id} not found")
