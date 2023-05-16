import sys

from PyQt5.QtWidgets import QApplication

from simple_priority_queue.cli import main_cli
from simple_priority_queue.gui import PriorityGUI


def main(args=None):
    """
    Main function to run the Simple Priority Queue application.

    Args:
        args (List[str], optional): Command-line arguments. Defaults to None.
    """

    if args is None:
        args = sys.argv[1:]

    # Check if the application should run the CLI or GUI
    if not args:
        app = QApplication([])  # Create an instance of QApplication
        gui = PriorityGUI(app)  # Initialize PriorityGUI with the QApplication instance
        gui.show()  # Make the GUI visible
        app.exec_()  # Start the QApplication's event loop
    else:
        main_cli(args)


if __name__ == "__main__":
    main()
