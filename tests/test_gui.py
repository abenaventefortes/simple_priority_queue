import sys
import unittest

from PyQt5.QtWidgets import QApplication

from simple_priority_queue.gui import PriorityGUI
from simple_priority_queue.priority_queue import PriorityQueue


class TestGui(unittest.TestCase):
    def setUp(self):
        """
        Set up the test environment.

        Returns:
            None
        """
        self.app = QApplication(sys.argv)
        self.pq = PriorityQueue()
        self.gui = PriorityGUI(self.app)

    def test_add_task(self):
        """
        Test adding a task to the queue.

        Returns:
            None
        """
        # Set the task and priority in the GUI
        self.gui.task_edit.setText("Task 1")
        self.gui.priority_edit.setText("1")
        # Call the add_task method to add the task
        self.gui.add_task()
        # Wait for the GUI event loop to process the task addition
        QApplication.processEvents()
        # Assert that the number of rows in the queue table is as expected
        self.assertEqual(self.gui.queue_table.rowCount(), 1)
        # Assert that the added task details are correct
        task = self.gui.queue.get_tasks()[0]
        self.assertEqual(task['command'], "Task 1")
        self.assertEqual(task['priority'], 1)

    def test_initial_state(self):
        """
        Test the initial state of the GUI.

        Returns:
            None
        """
        # Wait for the GUI event loop to process any pending events
        QApplication.processEvents()
        # Assert that the initial state of the GUI is as expected
        self.assertEqual(self.gui.task_edit.text(), "")
        self.assertEqual(self.gui.priority_edit.text(), "")
        self.assertEqual(self.gui.queue_table.rowCount(), 0)
        self.assertEqual(self.gui.log_display.toPlainText(), "")
        self.assertEqual(self.gui.progress_bar.value(), 0)
        self.assertEqual(self.gui.queue.get_tasks(), [])

    def test_process_task(self):
        """
        Test processing a task from the queue.

        Returns:
            None
        """
        # Add tasks to the priority queue
        self.pq.add_task({'task_id': '1', 'command': 'Task 1', 'priority': 1})
        self.pq.add_task({'task_id': '2', 'command': 'Task 2', 'priority': 2})

        # Set the priority and add a task in the GUI
        self.gui.priority_edit.setText("1")
        self.gui.add_task()
        # Call the process_tasks method to process the tasks
        self.gui.process_tasks()
        # Assert that the number of rows in the queue table is as expected
        self.assertEqual(self.gui.queue_table.rowCount(), 0)

    def test_update_queue_display(self):
        """
        Test updating the queue display.

        Returns:
            None
        """
        # Set the task and priority in the GUI and add a task
        self.gui.task_edit.setText("Task 1")
        self.gui.priority_edit.setText("1")
        self.gui.add_task()
        # Assert that the task name and priority in the queue table are as expected
        self.assertEqual(self.gui.queue_table.item(0, 0).text(), "Task 1")
        self.assertEqual(int(self.gui.queue_table.item(0, 2).text()), 1)


if __name__ == "__main__":
    unittest.main()
