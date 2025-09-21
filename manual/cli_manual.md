# Task Tracker CLI Manual

This manual explains how to use the command-line interface (CLI) for the Task Tracker project. The CLI allows you to manage categories and tasks, save/load data files, and view your progress.

## Running the CLI

Navigate to the directory and run:

```cmd
python src/cli.py <command> [arguments]
```

## Commands

### 1. Create a New Save File
```
python src/cli.py new-file <file>
```
- **<file>**: Name of the new save file (without path).
- *Creates a new save file in the `saves/` directory and resets categories.*

### 2. Load an Existing Save File
```
python src/cli.py load-file <file>
```
- **<file>**: Name of the save file to load.
- *Loads categories and tasks from the specified file in `saves/`.*

### 3. Add a Category
```
python src/cli.py add-category <c_name>
```
- **<c_name>**: Name of the category to add.
- *Adds a new category to your tracker.*

### 4. Remove a Category
```
python src/cli.py rem-category <c_name>
```
- **<c_name>**: Name of the category to remove.
- *Removes the specified category and its tasks.*

### 5. Add a Task
```
python src/cli.py add-task <t_cname> <t_name> <t_time>
```
- **<t_cname>**: Category name to add the task to.
- **<t_name>**: Name of the task.
- **<t_time>**: Time estimate or value for the task.
- *Adds a new task to the specified category.*

### 6. Remove a Task
```
python src/cli.py rem-task <t_cname> <t_name>
```
- **<t_cname>**: Category name.
- **<t_name>**: Name of the task to remove.
- *Removes the specified task from the category.*

### 7. Show Categories and Tasks
```
python src/cli.py show
```
- *Displays all categories and their tasks.*

## Notes
- All save files are stored in the `saves/` directory as JSON.
- After each operation, changes are saved automatically.
- If an operation fails, an error message is shown and the program exits.

## Example Usage
```
python src/cli.py new-file "mytasks.json"
python src/cli.py add-category "Work"
python src/cli.py add-task Work "Write report" "2h"
python src/cli.py show
```

## Troubleshooting
- Ensure you are running Python 3.12 or newer.
- If you see a failure message, check your arguments and file names.

---
For more help, see the README or open an issue in the repository.
