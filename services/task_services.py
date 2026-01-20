from core import TaskManager


class TaskServices:

    """Task services class. it has functions:
    list_tasks: prints out the list of tasks
    add_task: adds a task
    remove_task: removes a task
    reset_tasks: resets all the tasks
    show_progress: shows the progress of the day.
    mark_done: marks the task as done


    """
    def __init__(self, manager: TaskManager):
        self.manager = manager


    def list_tasks(self):
        self.manager.print_tasks()

    def reset_tasks(self):
        self.manager.reset_tasks_to_default()

    def show_progress(self):
        self.manager.print_progress()

    def mark_done(self,task_num):
        self.manager.update_tasks(task_num)

    def add_task(self,task_name):
        self.manager.add_task(task_name)
    def remove_task(self,task_num):
        self.manager.remove_task(task_num)