import uuid

from PyQt5.QtWidgets import QApplication, QMainWindow, QGridLayout, QLabel, QLineEdit, QPushButton, QCheckBox
from PyQt5.QtWidgets import QTextEdit, QProgressBar, QTableWidgetItem, QHeaderView, QTableWidget, QWidget
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QIntValidator

from simple_priority_queue.priority_queue import PriorityQueue


class PriorityGUI(QMainWindow):
    """A GUI for managing a priority queue."""

    def __init__(self, app):
        """Initialize the GUI and priority queue."""
        super().__init__()

        # Initialize the priority queue and the checkbox states
        self.queue = PriorityQueue()  # Initialize the queue object
        self.checkbox_states = {}  # A dictionary to keep track of checkbox states

        self.app = app
        self.setWindowTitle("Priority Queue")

        # Initialize the main widget and layout
        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)
        self.grid_layout = QGridLayout(self.central_widget)

        # Initialize Task Table
        self.queue_table = QTableWidget(self)
        self.queue_table.setColumnCount(4)
        self.queue_table.setHorizontalHeaderLabels(["Task", "Task ID", "Priority", "Queue"])

        header = self.queue_table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.Stretch)
        header.setSectionResizeMode(1, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QHeaderView.ResizeToContents)

        self.queue_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.grid_layout.addWidget(self.queue_table, 5, 0, 1, 2)

        # Initialize Task and Priority Fields
        self.init_task_priority_fields()

        # Initialize Add Task Button
        self.add_button = QPushButton("Add Task")
        self.add_button.clicked.connect(self.add_task)
        self.grid_layout.addWidget(self.add_button, 2, 0, 1, 2)

        # Initialize Process Tasks Button
        self.process_button = QPushButton("Process Tasks")
        self.process_button.clicked.connect(self.process_tasks)
        self.grid_layout.addWidget(self.process_button, 3, 0, 1, 2)

        # Initialize Progress Bar
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        self.grid_layout.addWidget(self.progress_bar, 4, 0, 1, 2)

        # Initialize Log Display
        self.log_display = QTextEdit()
        self.log_display.setReadOnly(True)
        self.grid_layout.addWidget(self.log_display, 6, 0, 1, 2)

    def init_task_priority_fields(self):
        """Initialize the task and priority fields."""
        self.task_label = QLabel("Task:")
        self.task_edit = QLineEdit()
        self.grid_layout.addWidget(self.task_label, 0, 0)
        self.grid_layout.addWidget(self.task_edit, 0, 1)

        self.priority_label = QLabel("Priority:")
        self.priority_edit = QLineEdit()
        self.priority_edit.setValidator(QIntValidator(1, 10))
        self.grid_layout.addWidget(self.priority_label, 1, 0)
        self.grid_layout.addWidget(self.priority_edit, 1, 1)

    @pyqtSlot()
    def add_task(self):
        """Add a task with the given priority to the queue."""
        task = self.task_edit.text().strip()  # Remove leading and trailing spaces
        priority_text = self.priority_edit.text()

        if not task:
            self.log_display.append("Failed to add task: Task name cannot be empty or only spaces.")
            self.task_edit.clear()  # Clear the input field
            return

        if not priority_text.isdigit():
            self.log_display.append("Failed to add task: Priority must be a number.")
            self.priority_edit.clear()  # Clear the input field
            return

        priority = int(priority_text)

        if priority < 1 or priority > 10:
            self.log_display.append("Failed to add task: Priority must be a number between 1 and 10.")
            self.priority_edit.clear()  # Clear the input field
            return

        task_id = str(uuid.uuid4())  # Create a unique identifier for the task
        task_dict = {'task_id': task_id, 'command': task, 'priority': priority}  # Task dictionary
        self.queue.add_task(task_dict)  # Add the task to the queue
        self.checkbox_states[task_id] = True  # Store the task ID as a string key in checkbox_states
        self.log_display.append(f"Added Task: {task} with Priority: {priority}")

        self.update_queue_display()  # Update the queue display and checkbox states after adding a task

        self.task_edit.clear()
        self.priority_edit.clear()

    @pyqtSlot()
    def process_tasks(self):
        """Process the highest priority task in the queue."""
        rows_to_process = []
        for row in range(self.queue_table.rowCount()):
            checkbox = self.queue_table.cellWidget(row, 3)
            task_id = self.queue_table.item(row, 1).text()  # Get the task ID from the QTableWidgetItem text
            task = self.queue_table.item(row, 0).text()  # Get the task from the QTableWidgetItem text
            priority = int(self.queue_table.item(row, 2).text())  # Get the priority from the QTableWidgetItem text
            task_dict = {'task_id': task_id, 'command': task, 'priority': priority}
            if checkbox.isChecked() and self.queue.has_task(task_dict):
                rows_to_process.append(row)

        if not rows_to_process:  # No tasks to process
            self.log_display.append("No tasks to process. Please add and select tasks.")
            return

        total_tasks = len(rows_to_process)
        self.progress_bar.setMaximum(100)  # Set the maximum value for the progress bar

        for index, row in enumerate(reversed(rows_to_process)):  # Reverse to avoid index changes during removal
            task = self.queue_table.item(row, 0).text()
            task_id = self.queue_table.item(row, 1).text()  # Get the task ID from the QTableWidgetItem text
            priority = int(self.queue_table.item(row, 2).text())
            task_dict = {'task_id': task_id, 'command': task, 'priority': priority}
            self.queue.remove_task(task_dict)  # Remove the task from the priority queue
            self.log_display.append(f"Processed Task: {task} with Priority: {priority}")
            self.progress_bar.setValue((index + 1) * 100 // total_tasks)  # Update progress bar using integer division
        self.update_queue_display()

        if not self.queue_table.rowCount():  # If all tasks are processed, reset the progress bar
            self.progress_bar.reset()

    def update_queue_display(self):
        """Update the task table with the current queue contents."""
        tasks = sorted(self.queue.get_tasks(), key=lambda x: x['priority'])  # Sort tasks by priority
        self.queue_table.setRowCount(len(tasks))

        for row, task in enumerate(tasks):
            task_id = task['task_id']  # Get the task ID from the task dictionary
            checked = self.checkbox_states.get(task_id, True)  # Retrieve the checkbox state or default to True

            checkbox = QCheckBox()
            checkbox.setChecked(checked)  # Set the checkbox state
            checkbox.stateChanged.connect(self.update_checkbox_state)  # Connect the stateChanged signal to our method
            checkbox.setProperty('task_id', task_id)  # Set the task_id as a property of the checkbox

            task_item = QTableWidgetItem(task['command'])  # Get the command string from the task dictionary
            task_id_item = QTableWidgetItem(task_id)
            priority_item = QTableWidgetItem(str(task['priority']))

            self.queue_table.setItem(row, 0, task_item)
            self.queue_table.setItem(row, 1, task_id_item)
            self.queue_table.setItem(row, 2, priority_item)
            self.queue_table.setCellWidget(row, 3, checkbox)

    @pyqtSlot(int)
    def update_checkbox_state(self, state):
        """Update the checkbox state when it is changed."""
        checkbox = self.sender()
        task_id = checkbox.property('task_id')
        self.checkbox_states[task_id] = bool(state)

    def closeEvent(self, event):
        """Save checkbox states before closing the application."""
        for row in range(self.queue_table.rowCount()):
            task_id = self.queue_table.item(row, 1).text()  # Get the task ID from the QTableWidgetItem text
            checkbox = self.queue_table.cellWidget(row, 3)
            self.checkbox_states[task_id] = checkbox.isChecked()

        super().closeEvent(event)


if __name__ == "__main__":
    app = QApplication([])
    gui = PriorityGUI(app)
    gui.show()
    app.exec_()
