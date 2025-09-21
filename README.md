# Task Tracker CLI

A simple command-line tool for tracking tasks and saving progress. This project is written in Python and provides a CLI interface for managing tasks, with data persistence in JSON files.

## Features
- Add, list, and manage tasks via the command line
- Save and load task data from JSON files
- Modular codebase for easy extension

## Project Structure
```
src/
  cli.py      # Command-line interface app
  main.py     # Main logic for the CLI
  __pycache__/  # Compiled Python files
saves/
  .gitkeep
  *.json      # Saved task data
README.md     # Project documentation
```

## Getting Started
1. **Clone the repository**
2. **Install Python 3.12+**
3. **Run the CLI:**
   ```cmd
   python src/cli.py
   ```

## Usage
- Add tasks, list tasks, and manage your progress using the CLI prompts.
- Task data is saved automatically in the `saves/` directory as JSON files.

## Requirements
- Python 3.12 or newer

## Contributing
Pull requests and suggestions are welcome! Please open an issue to discuss changes before submitting PRs.

## License
MIT License

## Future Improvements

### GUI Version (CTk)

A graphical user interface (GUI) version of Task Tracker is planned using CustomTkinter (CTk). This will provide a more user-friendly experience for managing tasks and categories, with features such as:

- Visual task and category management
- Enhanced data visualization
- Improved accessibility and usability

Stay tuned for updates on the CTk GUI version!
