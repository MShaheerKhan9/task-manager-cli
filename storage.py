"""
storage.py

Handles persistence for the task manager.
Currently uses a file-based storage system.
Future versions may support databases.
"""

class Storage:
    def load_tasks(self):
        raise NotImplementedError("Storage backend not implemented yet")

    def save_tasks(self, tasks, status):
        raise NotImplementedError("Storage backend not implemented yet")