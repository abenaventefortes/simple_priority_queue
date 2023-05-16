# CLI Detailed Usage Guide

Here you can find detailed instructions and examples for each CLI command.

## Add Task

To add a task to the priority queue, use the add command followed by the task and priority level:

    simple_priority_queue add <task> <priority>

For example, to add the task "Clean the kitchen" with priority level 2, you would run the following command:

    simple_priority_queue add "Clean the kitchen" 2

### Process Task
To process the highest priority task in the priority queue, use the process command:

    simple_priority_queue process
This will remove the highest priority task from the queue and print a message indicating the task that was processed.

### List Tasks

To list all the tasks in the priority queue, use the list command:

    simple_priority_queue list

This will print a list of all the tasks in the queue, grouped by priority level.

### Clear Queue
To clear all tasks from the priority queue, use the clear command:

    simple_priority_queue clear

This will remove all tasks from the queue.

## Examples

Here are some examples of how you can use the CLI:

### Add tasks to the priority queue
    simple_priority_queue add "Buy groceries" 1
    simple_priority_queue add "Clean the house" 2
    simple_priority_queue add "Do laundry" 3

### List tasks in the priority queue
    simple_priority_queue list

### Process highest priority task
    simple_priority_queue process

### List tasks in the priority queue
    simple_priority_queue list

### Clear all tasks from the priority queue
    simple_priority_queue clear

### Help
To get help on how to use the CLI, use the --help option:

    simple_priority_queue --help

This will print a help message that explains how to use the CLI and the available commands and options.