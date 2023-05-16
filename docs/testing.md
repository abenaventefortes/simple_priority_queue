# Testing

The Simple Priority Queue library has a comprehensive suite of tests to ensure that it works correctly and reliably. Here's how you can run them and what they cover.

## Running the tests

To run the tests, use the following command:

    python -m unittest discover -s tests/

This will discover all the tests in the tests/ directory and run them.

## Test coverage

The tests cover all the functionality of the priority queue and the CLI and GUI interfaces.

### Unit tests

The test_priority_queue.py module contains unit tests for the PriorityQueue class, ensuring that it can correctly add and process tasks in order of priority.

The test_cli.py module contains unit tests for the CLI class, ensuring that it can correctly parse command-line arguments and execute the appropriate commands on the priority queue.

The test_gui.py module contains unit tests for the PriorityGUI class, ensuring that it can correctly add and process tasks in order of priority, and that it displays the correct status messages.

### Integration tests
The test_integration.py module contains integration tests for the priority queue library, ensuring that it can correctly handle a series of tasks with varying priorities.

### Performance tests
The test_performance.py module contains performance tests for the priority queue library, ensuring that it can handle a large number of tasks with varying priorities within a reasonable time frame.

### Continuous Integration
This library uses Continuous Integration (CI) to automatically run the test suite whenever changes are made to the codebase. This ensures that the tests are always passing and that the code is always in a working state.

The CI pipeline for this library is configured using GitHub Actions, and is set up to run the test suite on every push and pull request to the main branch.