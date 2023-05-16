import unittest
from unittest.mock import patch, MagicMock

from simple_priority_queue import cli


class TestCli(unittest.TestCase):
    @patch('simple_priority_queue.cli.PriorityQueue')
    def test_add_task(self, mock_queue):
        """
        Test adding a task to the priority queue.

        Args:
            mock_queue (MagicMock): The mocked PriorityQueue object.

        Returns:
            None
        """
        # Create a mock for the command-line arguments
        mock_args = MagicMock()
        mock_args.task = 'test_task'
        mock_args.priority = 3

        # Call the add_task function with the mock arguments and mock queue
        cli.add_task(mock_args, mock_queue)

        # Assert that the add_task method of the mock queue is called once
        mock_queue.add_task.assert_called_once()

        # Get the call arguments of the add_task method
        call_args = mock_queue.add_task.call_args[0]

        # Assert that the command and priority of the task match the expected values
        self.assertEqual(call_args[0]['command'], 'test_task')
        self.assertEqual(call_args[0]['priority'], 3)

    @patch('simple_priority_queue.cli.PriorityQueue')
    def test_process_task_with_task(self, mock_queue):
        """
        Test processing a task from the priority queue when a task is present.

        Args:
            mock_queue (MagicMock): The mocked PriorityQueue object.

        Returns:
            None
        """
        # Set up the mock return value for the process_task method
        mock_queue.process_task.return_value = {'command': 'test_task', 'priority': 3}

        # Patch the built-in print function to capture the printed output
        with patch('builtins.print') as mock_print:
            # Call the process_task function with the mock queue
            cli.process_task(mock_queue)

        # Assert that the print function is called once with the expected output
        mock_print.assert_called_once_with('Processed task: test_task with priority 3')

    @patch('simple_priority_queue.cli.PriorityQueue')
    def test_process_task_without_task(self, mock_queue):
        """
        Test processing a task from the priority queue when no task is present.

        Args:
            mock_queue (MagicMock): The mocked PriorityQueue object.

        Returns:
            None
        """
        # Set up the mock return value for the process_task method
        mock_queue.process_task.return_value = None

        # Patch the built-in print function to capture the printed output
        with patch('builtins.print') as mock_print:
            # Call the process_task function with the mock queue
            cli.process_task(mock_queue)

        # Assert that the print function is called once with the expected output
        mock_print.assert_called_once_with('No tasks to process.')

    @patch('simple_priority_queue.cli.main_cli')
    def test_main_cli(self, mock_main):
        """
        Test the main_cli function.

        Args:
            mock_main (MagicMock): The mocked main_cli function.

        Returns:
            None
        """
        # Set up the test arguments
        test_args = ['add', 'test_task', '3']

        # Call the main_cli function with the test arguments
        cli.main_cli(test_args)

        # Assert that the main_cli function is called once
        mock_main.assert_called_once()


if __name__ == '__main__':
    unittest.main()
