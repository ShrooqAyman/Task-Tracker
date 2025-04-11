import datetime
from prettytable import PrettyTable
from Task import Task
from helper import create_new_json_file, read_json_file, update_json_file, FileNotFoundError, FileWriteError, InvalidJsonError

class TaskNotFoundError(Exception):
    """Custom exception raised when a task is not found by ID."""
    pass

class InvalidTaskInputError(Exception):
    """Custom exception raised when invalid input is provided for a task."""
    pass

class TaskTracker:
    """
    A class to manage tasks, including adding, updating, deleting, and listing tasks.
    It stores tasks in a JSON file.

    Attributes:
        file_path (str): The path to the JSON file where tasks are stored.
    """

    def __init__(self, file_path):
        """
        Initializes the TaskTracker with a given file path and creates a new JSON file if it doesn't exist.

        Args:
            file_path (str): The path to the JSON file where tasks are stored.

        Raises:
            FileWriteError: If the file cannot be created or accessed.
        """
        self.file_path = file_path
        try:
            create_new_json_file(file_path)
        except FileWriteError as e:
            print(FileWriteError(f"Error creating or accessing the file: {str(e)}"))


    def _read_data(self):
        """
        Reads and returns the data from the JSON file.

        Returns:
            list: A list of tasks stored in the JSON file.

        Raises:
            FileNotFoundError: If the file is not found.
            InvalidJsonError: If the file content is not valid JSON.
        """
        try:
            return read_json_file(self.file_path)
        except (FileNotFoundError, InvalidJsonError) as e:
            print(e)

    def _write_data(self, data):
        """
        Writes the given data back to the JSON file.

        Args:
            data (list): The data to write to the JSON file.

        Raises:
            FileWriteError: If the file cannot be written to.
        """
        try:
            update_json_file(self.file_path, data)
        except FileWriteError as e:
            print(FileWriteError(f"Error writing to the file: {str(e)}"))

    def _get_next_task_id(self, data):
        """
        Calculates the next task ID based on the existing tasks.

        Args:
            data (list): A list of tasks.

        Returns:
            int: The next available task ID.
        """
        if data:
            return max(task['id'] for task in data) + 1
        return 1  # start with 1 if there are no tasks

    def add(self, description, status):
        """
        Adds a new task with the given description and status.

        Args:
            description (str): The description of the task.
            status (str): The status of the task (e.g., 'pending', 'completed').

        Raises:
            InvalidTaskInputError: If description or status is invalid.
        """
        if not description or not status:
            print(InvalidTaskInputError("Both description and status must be provided."))
            return
        
        # Read existing data
        data = self._read_data()

        # Determine the next task ID
        new_task_id = self._get_next_task_id(data)

        # Create and add new task
        new_task = Task(new_task_id, description, status)
        data.append(new_task.to_dict())

        # Write updated data
        self._write_data(data)
        return new_task_id

    def update(self, task_id, description=None, status=None):
        """
        Updates the task with the given ID. You can update the description, status, or both.

        Args:
            task_id (int): The ID of the task to update.
            description (str, optional): The new description of the task.
            status (str, optional): The new status of the task.

        Raises:
            TaskNotFoundError: If the task with the specified ID is not found.
            InvalidTaskInputError: If description or status is invalid.
        """
        if description is None and status is None:
            print( InvalidTaskInputError("At least one of description or status must be provided."))
            return
        
        # Read existing data
        data = self._read_data()

        # Find task by ID
        task = next((task for task in data if task['id'] == task_id), None)

        if not task:
            print( TaskNotFoundError(f"No task found with ID {task_id}"))
            return

        task['updatedAt'] = datetime.datetime.now().isoformat()
        if description is not None:
            task['description'] = description
        if status is not None:
            task['status'] = status

        # Write updated data
        self._write_data(data)
        print(f"Task with ID {task_id} has been updated.")

    def delete(self, task_id):
        """
        Deletes the task with the given ID.

        Args:
            task_id (int): The ID of the task to delete.

        Raises:
            TaskNotFoundError: If the task with the specified ID is not found.
        """
        # Read existing data
        data = self._read_data()

        # Find and remove task by ID
        task = next((task for task in data if task['id'] == task_id), None)

        if not task:
            print( TaskNotFoundError(f"No task found with ID {task_id} to delete."))
            return

        data.remove(task)
        self._write_data(data)
        print(f"Task with ID {task_id} has been deleted.")

    def list_tasks(self, filter_status=None):
        """
        Lists all tasks in a table format, optionally filtered by status.

        Args:
            filter_status (str, optional): The status to filter tasks by (e.g., 'pending', 'completed').

        Raises:
            FileNotFoundError: If there is an issue reading the tasks from the file.
        """
        try:
            # Read existing data
            data = self._read_data()

            if data:
                # Create a PrettyTable instance
                table = PrettyTable()
                table.field_names = ["ID", "Description", "Status"]

                # Filter tasks based on the given filter
                filtered_data = [task for task in data if filter_status is None or task["status"] == filter_status]

                # Add rows to the table
                for task in filtered_data:
                    table.add_row([task["id"], task["description"], task["status"]])

                # Print the table
                print(table)
            else:
                print("No tasks available.")
        except FileNotFoundError as e:
            print(f"Error: {str(e)}")