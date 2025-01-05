# Multi-Interface Task Management Program

This program provides a versatile task management solution with both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)**. It enables users to manage tasks efficiently through user-friendly interfaces.

## Features

1. **Command-Line Interface (CLI):**
   - Quickly add, remove, and display tasks.
   - Designed for users who prefer text-based task management.

2. **Graphical User Interface (GUI):**
   - Intuitive graphical interface for task visualization and management.
   - Drag-and-drop support for task reordering.

3. **Core Functionalities:**
   - Maintain a dynamic task list stored in a file.
   - Support for multiple task-related operations (add, remove, list).

## File Overview

- **`gui.py`:** Contains the GUI implementation, offering a user-friendly way to interact with the task list.
- **`cli.py`:** Provides the CLI-based interface for task management.
- **`functions.py`:** Includes core functions shared between the CLI and GUI, such as task addition, deletion, and retrieval.
- **`todos.txt`:** Stores the list of tasks. Each task is represented as a line in this file.

## Setup and Usage

### Prerequisites
- Python 3.7 or higher
- Required libraries (install via `pip` if necessary):
  - `tkinter` (for GUI)

### Installation
1. Clone the repository or download the files.
2. Ensure Python and dependencies are installed.

### Running the Program

#### CLI
1. Navigate to the directory containing `cli.py`.
2. Run the program using:
   ```bash
   python cli.py
   ```
3. Use the available commands (displayed in the CLI) to manage tasks.

#### GUI
1. Navigate to the directory containing `gui.py`.
2. Launch the GUI with:
   ```bash
   python gui.py
   ```
3. Manage tasks through the graphical interface.

### Task File
- The program reads tasks from `todos.txt`.
- Tasks are stored line by line in plain text.
- Users can directly edit the file if needed, but it is recommended to use the program interfaces.
