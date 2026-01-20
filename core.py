from datetime import datetime



class TaskManager:
    """
    Manages tasks, persistence, and daily state.
    """

    def __init__(self,filename = "tasks.txt"):
        self.tasks = []
        self.status = []
        self.taskfile = filename
        self.read_tasks()
        if self.tasks == []:
            self.reset_tasks_to_default()
        self.last_log_date = self.read_last_log_date()

    def reset_tasks_to_default(self):
        """Renews the tasks list."""
        self.tasks = ["gym", "work", "study"]
        self.status = [False, False, False]
        with open(self.taskfile, "w") as file:
            for task in self.tasks:
                file.write(f"{task},False\n")

    def read_last_log_date(self):
        """ Reads the last log date from the last_log file"""
        try:
            with open("last_log.txt", "r") as file:
                file_content = file.read()
                return file_content.split("\n")[0]
        except FileNotFoundError:
            today = datetime.today().strftime("%Y-%m-%d")
            with open("last_log.txt", "w") as file:
                file.write(today)
                return today


    def read_tasks(self):
        """Reads the tasks from the tasks file"""
        self.tasks = []
        self.status = []
        try:
            with open(self.taskfile, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            return

        for line in lines:
            line = line.strip()  # remove \n and spaces
            if not line:
                continue  # skip empty lines

            parts = line.split(",")
            if len(parts) != 2:
                continue  # invalid format

            task_name, task_status = parts
            task_status = task_status.strip().lower()
            self.tasks.append(task_name)

            if task_status == "true":

                self.status.append(True)
            elif task_status == "false":

                self.status.append(False)
            else:
                continue  # invalid status


    def log_history(self):
        """ logs the history to the log file"""

        date = datetime.now().strftime("%Y-%m-%d")

        with open("log.txt", "a") as file:
            file.write(f"===== {self.last_log_date} =====\n")
            for t,st in zip(self.tasks,self.status):
                file.write(f"Task:{t}, Status:{st}\n")
            file.write("\n")

        with open("last_log.txt", "w") as file:
            file.write(f"{date}\n")
        self.last_log_date = date

    def write_tasks_to_file(self):
        """Writes the tasks to the tasks file"""
        with open("tasks.txt", "w") as file:
            for t,st in zip(self.tasks,self.status):
                file.write(f"{t},{st}\n")

    def run(self):
        """run every day to log the tasks and to renew the tasks"""
        if self.last_log_date  != datetime.now().strftime("%Y-%m-%d"):
            self.log_history()
            self.reset_tasks_to_default()


    def cal_progress(self):
        """calculates the progress of the day."""
        return f"{sum(self.status)} / {len(self.status)}"


    def update_tasks(self,task_num):
        """updates the tasks list"""



        if task_num > len(self.tasks) or task_num <= 0:
            print("invalid task number")
            return
        if self.status[task_num - 1]:
            print("Task Marked Already!")
            return
        self.status[task_num - 1] = True
        self.update_file(task_num)

    def update_file(self,task_num):
        """updates the tasks list"""
        try:
            with open(self.taskfile, "r") as file:
                lines = file.readlines()
        except FileNotFoundError:
            return
        if 0 < task_num <= len(lines):
            task, _ = lines[task_num - 1].strip().split(",")
            lines[task_num - 1] = f"{task.strip()},True\n"
        with open(self.taskfile, "w") as file:
            file.writelines(lines)
    def sort_tasks(self):
        """sorts the tasks list on adding a task."""
        combined = sorted(
            zip(self.tasks, self.status),
            key=lambda pair: pair[0].lower()
        )
        self.tasks,self.status = map(list,zip(*combined))

    def add_task(self,task_name):
        """adds a task to the tasks list nad to the file"""
        for task in self.tasks:
            if task_name == task:
                print("Task Already Exists!")
                return
        self.tasks.append(task_name)
        self.status.append(False)
        self.sort_tasks()
        self.write_tasks_to_file()
        print("Task Added!")


    def remove_task(self,task_num):
        """removes a task from the tasks list and updates the file"""
        if  0 < task_num <= len(self.tasks):
            index = task_num -1
            self.tasks.pop(index)
            self.status.pop(index)
        else:
            print("invalid task number")
            return

        self.write_tasks_to_file()
        print("Task Removed!")

    def print_task_manager(self):
        """not is use for now. Prints the tasks with their status."""
        print("\nTask Manager")
        task_with_status = [f"{t}:{st}" for t, st in zip(self.tasks, self.status)]
        print("Today's tasks:", ", ".join(task_with_status))


    def print_tasks(self):
        """prints the tasks"""
        print("Today's tasks")
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}: {task}")



    def print_progress(self):
        """prints the progress of the day."""
        print("\nTask Progress")

        print("Today's progress:", self.cal_progress())
