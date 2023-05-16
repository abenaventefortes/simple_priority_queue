import threading
import uuid

from typing import Dict, Any, Union, List


class PriorityQueue:
    """A thread-safe priority queue that processes tasks in order of priority."""

    def __init__(self):
        """Initialize the priority queue."""
        self.queue = {}
        self.lock = threading.RLock()

    def add_task(self, task: Dict[str, Any]) -> None:
        """
        Add a task to the priority queue.

        Args:
            task (Dict[str, Any]): The task to be added.
        """
        with self.lock:
            task_id = str(uuid.uuid4())  # Generate a new task ID
            task['task_id'] = task_id  # Add the task ID to the task
            priority = task.get('priority')
            if priority is not None:
                if priority in self.queue:
                    self.queue[priority].append(task)
                else:
                    self.queue[priority] = [task]

    def remove_task(self, task: Dict[str, Any]) -> None:
        """
        Remove a task from the priority queue.

        Args:
            task (Dict[str, Any]): The task to be removed.
        """
        with self.lock:
            priority = task.get('priority')
            if priority is not None:
                if priority in self.queue and task in self.queue[priority]:
                    self.queue[priority].remove(task)
                    if not self.queue[priority]:
                        del self.queue[priority]

    def process_task(self) -> Union[Dict[str, Any], None]:
        """
        Process the highest priority task in the priority queue.

        Returns:
            Union[Dict[str, Any], None]: The processed task or None if the queue is empty.
        """
        with self.lock:
            if not self.queue:
                return None

            highest_priority = max(self.queue)
            command = self.queue[highest_priority].pop(0)

            if not self.queue[highest_priority]:
                del self.queue[highest_priority]

            return {'command': command, 'priority': highest_priority}

    def get_tasks(self) -> List[Dict[str, Union[str, int]]]:
        """
        Return all tasks sorted by priority.

        Returns:
            List[Dict[str, Union[str, int]]]: The list of tasks.
        """
        with self.lock:
            tasks = []
            for priority in sorted(self.queue, reverse=True):
                for task in self.queue[priority]:
                    tasks.append({'task_id': task['task_id'], 'command': task['command'], 'priority': priority})
            return tasks

    def __len__(self) -> int:
        """
        Return the total number of tasks in the queue.

        Returns:
            int: The total number of tasks in the queue.
        """
        with self.lock:
            return sum(len(tasks) for tasks in self.queue.values())

    def has_task(self, task_dict):
        """
        Check if a task is in the queue.

        Args:
            task_dict (Dict[str, Any]): The task to check.

        Returns:
            bool: True if the task is in the queue, False otherwise.
        """
        with self.lock:
            for priority in self.queue:
                for task in self.queue[priority]:
                    if isinstance(task, dict) and 'task_id' in task:  # Check if 'task' is a dictionary and has
                        # 'task_id' field
                        if task['task_id'] == task_dict['task_id']:
                            return True
        return False
