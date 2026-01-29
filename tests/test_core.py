import os
from Task_Manager.core import TaskManager, TaskDoneAlreadyError
import pytest



def test_task_manager_initialize_default_tasks():

    test_file = "test_tasks.txt"

    if os.path.exists(test_file):
        os.remove(test_file)

    manager = TaskManager(filename=test_file)

    assert manager.tasks == ["gym","work","study"]
    assert manager.status == [False,False,False]

    os.remove(test_file)

def test_task_manager_add_task():
    test_file = "test_tasks.txt"
    if os.path.exists(test_file):
        os.remove(test_file)

    manager = TaskManager(filename=test_file)

    result  = manager.add_task("read")
    assert "read" in manager.tasks
    assert manager.status[manager.tasks.index("read")] == False
    assert result["name"] == "read"
    assert result["status"] == False

    os.remove(test_file)

def test_task_manager_mark_single_task_as_done():
    test_file = "test_tasks.txt"
    if os.path.exists(test_file):
        os.remove(test_file)

    manager = TaskManager(filename=test_file)
    result1 = manager.update_tasks(1)


    assert result1["id"] == 1
    assert result1["name"] == "gym"
    assert result1["status"] == True
    assert manager.status[0] == True


    os.remove(test_file)

def test_marking_completed_task_raises_error():
    test_file = "test_tasks.txt"
    if os.path.exists(test_file):
        os.remove(test_file)
    manager = TaskManager(filename=test_file)
    manager.update_tasks(1)

    with pytest.raises(TaskDoneAlreadyError):
        manager.update_tasks(1)

    os.remove(test_file)

