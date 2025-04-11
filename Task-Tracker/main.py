import argparse
import sys
from TaskTracker import TaskTracker
from helper import FileWriteError

# Initialize TaskTracker with the file path to store tasks
task_tracker = TaskTracker("tasks.json")

def add_task(description):
    try:
        task_id = task_tracker.add(description, 'todo')  # default status is 'todo'
        print(f"Task added successfully (Id: {task_id})")
    except FileWriteError as e:
        print(f"Error adding task: {str(e)}")

def update_task(task_id, description):
    try:
        task_tracker.update(task_id, description=description)
    except Exception as e:
        print(f"Error updating task: {str(e)}")

def delete_task(task_id):
    try:
        task_tracker.delete(task_id)
    except Exception as e:
        print(f"Error deleting task: {str(e)}")

def list_tasks(filter_status=None):
    try:
        task_tracker.list_tasks(filter_status)
    except Exception as e:
        print(f"Error listing tasks: {str(e)}")

def mark_task_in_progress(task_id):
    try:
        task_tracker.update(task_id, status='in-progress')
    except Exception as e:
        print(f"Error marking task as in-progress: {str(e)}")

def mark_task_done(task_id):
    try:
        task_tracker.update(task_id, status='done')
    except Exception as e:
        print(f"Error marking task as done: {str(e)}")

def main():
    # Set up the argument parser
    parser = argparse.ArgumentParser(description="Task management CLI")

    # Add subparsers for different commands
    subparsers = parser.add_subparsers(dest="command")

    # Add task command
    add_parser = subparsers.add_parser('add', help="Add a new task")
    add_parser.add_argument('description', type=str, help="Task description")

    # Update task command
    update_parser = subparsers.add_parser('update', help="Update an existing task")
    update_parser.add_argument('task_id', type=int, help="Task ID")
    update_parser.add_argument('description', type=str, help="New task description")

    # Delete task command
    delete_parser = subparsers.add_parser('delete', help="Delete a task")
    delete_parser.add_argument('task_id', type=int, help="Task ID to delete")

    # List tasks command
    list_parser = subparsers.add_parser('list', help="List tasks")
    list_parser.add_argument('filter_status', type=str, nargs='?', choices=['todo', 'in-progress', 'done'], help="Filter tasks by status")

    # Mark task as in-progress command
    mark_in_progress_parser = subparsers.add_parser('mark-in-progress', help="Mark task as in-progress")
    mark_in_progress_parser.add_argument('task_id', type=int, help="Task ID")

    # Mark task as done command
    mark_done_parser = subparsers.add_parser('mark-done', help="Mark task as done")
    mark_done_parser.add_argument('task_id', type=int, help="Task ID")

    # Parse the arguments
    args = parser.parse_args()

    # Handle the commands
    if args.command == 'add':
        add_task(args.description)
    elif args.command == 'update':
        update_task(args.task_id, args.description)
    elif args.command == 'delete':
        delete_task(args.task_id)
    elif args.command == 'list':
        list_tasks(args.filter_status)
    elif args.command == 'mark-in-progress':
        mark_task_in_progress(args.task_id)
    elif args.command == 'mark-done':
        mark_task_done(args.task_id)
    else:
        print("Unknown command. Use 'task-cli --help' for usage details.")

if __name__ == "__main__":
    main()
