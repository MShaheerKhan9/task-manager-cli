import argparse
from core import TaskManager
from services.task_services import TaskServices

def cmd_done(args):
    args.service.mark_done(args.number)

def cmd_reset(args):
    args.service.reset_tasks()

def cmd_progress(args):
    args.service.show_progress()

def cmd_tasks(args):
    args.service.list_tasks()

def cmd_add(args):
    args.service.add_task(args.name)

def cmd_remove(args):
    args.service.remove_task(args.number)

def run_cli():
    #parser
    task_manager = TaskManager()
    task_manager.run()

    service = TaskServices(task_manager)

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest="command")

    #subparsers
    done_parser = subparser.add_parser("done")
    done_parser.add_argument("number", type=int)

    progress_parser = subparser.add_parser("progress")
    reset_parser = subparser.add_parser("reset")
    print_parser = subparser.add_parser("tasks")
    list_parser = subparser.add_parser("list") #alias of print_parser tasks,list

    add_parser = subparser.add_parser("add")
    add_parser.add_argument("name")

    remove_parser = subparser.add_parser("remove")
    remove_parser.add_argument("number", type=int)



    # subparsers functions
    done_parser.set_defaults(func=cmd_done, service = service)
    progress_parser.set_defaults(func=cmd_progress,service = service)
    reset_parser.set_defaults(func=cmd_reset,service = service)
    print_parser.set_defaults(func=cmd_tasks,service = service)
    list_parser.set_defaults(func=cmd_tasks,service = service)
    add_parser.set_defaults(func=cmd_add,service = service)
    remove_parser.set_defaults(func=cmd_remove,service =service)

    args = parser.parse_args()
    if not hasattr(args, "func"):
        parser.print_help()
        return

    args.func(args)

