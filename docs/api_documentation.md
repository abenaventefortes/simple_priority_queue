# API Documentation

The PriorityQueue class represents a priority queue of tasks, where tasks are processed in order of priority. Higher priority tasks are processed before lower priority tasks. This document provides detailed information about the methods provided by the PriorityQueue class.

## PriorityQueue Class

### Methods

#### `add_task(command: str, priority: int) -> None`

This method is used to add a task to the priority queue.

- **Parameters:**
    - `command` (str): The task to be added.
    - `priority` (int): The priority level of the task.
- **Returns:** None

#### `process_task() -> Tuple[str, int]`

This method processes the highest priority task in the priority queue.

- **Returns:** 
    - `tuple`: A tuple representing the processed task. The tuple contains two elements - the command (str) and the priority level (int).
