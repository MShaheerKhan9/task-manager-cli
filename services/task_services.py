

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
        return[
            {
                "id" : i+1,
                "name" : name,
                "status" : status
            }
            for i,(name,status) in enumerate(zip(self.manager.tasks,self.manager.status))

        ]

    def reset_tasks(self):
        self.manager.reset_tasks_to_default()

    def mark_done(self,task_num):
        return self.manager.update_tasks(task_num)

    def add_task(self,task_name):
        return self.manager.add_task(task_name)

    def remove_task(self,task_num):
        return self.manager.remove_task(task_num)

    def get_task(self,task_num):
        return self.manager.get_task(task_num)

    def get_progress(self):
        completed, total = self.manager.cal_progress()
        percent = round(100 * completed / total) if total > 0 else 0
        return{
            "completed" : completed,
            "total" : total,
            "percent" : percent
        }