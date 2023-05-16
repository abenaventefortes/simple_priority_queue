import argparse
import sys
import uuid

from simple_priority_queue.priority_queue import PriorityQueue


def main_cli(args=None):
    """
    Main function for running the CLI interface.

    Args:
        args (List[str], optional): Command-line arguments.
    """
    if args is None:
        args = sys.argv[1:]
    parser = parse_arguments()
    parsed_args = parser.parse_args(args)
    priority_queue = PriorityQueue()

    # Call the appropriate function based on the subcommand.
    if parsed_args.subcommand == "add":
        add_task(parsed_args, priority_queue)
    elif parsed_args.subcommand == "process":
        process_task(priority_queue)
    else:
        parser.print_help()


def parse_arguments():
    """
    Create and return the parser for the command-line arguments.

    Returns:
        argparse.ArgumentParser: The configured ArgumentParser object.
    """
    parser = argparse.ArgumentParser(description="Manage a priority queue.")
    subparsers = parser.add_subparsers(title="subcommands", dest="subcommand")

    # Create the parser for the add command.
    add_parser = subparsers.add_parser("add", help="add a task to the priority queue")
    add_parser.add_argument("task", help="the task to be added")
    add_parser.add_argument("priority", type=int, help="the priority of the task")

    # Create the parser for the process command.
    subparsers.add_parser("process", help="process the highest priority task in the priority queue")

    return parser


def add_task(namespace, priority_queue):
    """
    Add a task to the priority queue.

    Args:
        namespace (argparse.Namespace): An argparse.Namespace object that contains the task and priority arguments.
        priority_queue (PriorityQueue): The priority queue to add the task to.
    """
    try:
        task_id = str(uuid.uuid4())  # Create a unique identifier for the task
        task = {'task_id': task_id, 'command': namespace.task, 'priority': namespace.priority}
        priority_queue.add_task(task)  # Add the task to the priority queue
        print(f"Task added: {namespace.task} with priority {namespace.priority}")
    except ValueError as e:
        print(f"Error: {e}")


def process_task(priority_queue):
    """
    Process the highest priority task in the priority queue and print the command to be executed.

    Args:
        priority_queue (PriorityQueue): The priority queue to process the task from.
    """
    # Get the highest priority task from the queue
    task = priority_queue.process_task()

    # If there is a task to be executed
    if task:
        # Get the command and priority level of the task
        command, priority = task['command'], task['priority']
        # Print a message indicating the task has been processed
        print(f"Processed task: {command} with priority {priority}")
    else:
        # If there are no tasks to be executed, print a message indicating that
        print("No tasks to process.")
