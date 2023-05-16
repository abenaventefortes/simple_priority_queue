import unittest

from simple_priority_queue.priority_queue import PriorityQueue


class TestPriorityQueue(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.

        Returns:
            None
        """
        self.pq = PriorityQueue()

    def test_add_task(self):
        """
        Test adding a task to the priority queue.

        Returns:
            None
        """
        task = {'command': 'Task 1', 'priority': 1}
        self.pq.add_task(task)
        self.assertEqual(self.pq.get_tasks(), [task])

    def test_remove_task(self):
        """
        Test removing a task from the priority queue.

        Returns:
            None
        """
        task = {'command': 'Task 1', 'priority': 1}
        self.pq.add_task(task)
        self.pq.remove_task(task)
        self.assertEqual(self.pq.get_tasks(), [])

    def test_process_task(self):
        """
        Test processing a task from the priority queue.

        Returns:
            None
        """
        # Create a new priority queue and tasks
        queue = PriorityQueue()
        tasks = [
            {'command': 'Task 1', 'priority': 1},
            {'command': 'Task 2', 'priority': 2},
            {'command': 'Task 3', 'priority': 3},
        ]

        # Add tasks to the priority queue
        for task in tasks:
            queue.add_task(task)

        # Process a task from the priority queue
        processed_task = queue.process_task()

        # Assert that a task is processed
        self.assertIsNotNone(processed_task)

        # Extract the processed command, task commands, and task IDs
        processed_command = processed_task['command']['command']
        task_commands = [task['command'] for task in tasks]
        processed_task_id = processed_task['command']['task_id']
        task_ids = [task['task_id'] for task in tasks]

        # Assert that the processed command and task ID are in the list of task commands and task IDs
        self.assertIn(processed_command, task_commands, f"Processed task command '{processed_command}' not found in tasks")
        self.assertIn(processed_task_id, task_ids, f"Processed task ID '{processed_task_id}' not found in task IDs")

    def test_get_tasks(self):
        """
        Test getting all tasks from the priority queue.

        Returns:
            None
        """
        # Create tasks
        task1 = {'command': 'Task 1', 'priority': 1}
        task2 = {'command': 'Task 2', 'priority': 2}

        # Add tasks to the priority queue
        self.pq.add_task(task1)
        self.pq.add_task(task2)

        # Assert that the retrieved tasks match the expected order
        self.assertEqual(self.pq.get_tasks(), [task2, task1])


if __name__ == "__main__":
    unittest.main()
