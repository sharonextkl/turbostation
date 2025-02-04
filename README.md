# TurboStation

TurboStation is a Python utility designed to manage and optimize startup programs on Windows, aiming to improve boot times and enhance overall system responsiveness.

## Features

- **List Startup Programs:** Display all programs set to run at startup, both from the registry and the startup folder.
- **Disable Startup Programs:** Remove specified programs from the startup list in the Windows registry.
- **Enable Startup Programs:** Add specified programs to the startup list to run when Windows boots.
- **Optimize Startup:** Placeholder for future functionality to automatically optimize startup processes.

## Requirements

- Windows Operating System
- Python 3.x

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/TurboStation.git
   ```
2. Navigate to the project directory:
   ```bash
   cd TurboStation
   ```

## Usage

Run the script using Python:

```bash
python TurboStation.py
```

### Example

To disable or enable a specific program at startup, modify the `main()` function in `TurboStation.py` with the desired program name and path.

```python
# Disable a startup program
turbo_station.disable_startup_program("MyProgram")

# Enable a startup program
turbo_station.enable_startup_program("MyProgram", r"C:\Path\To\MyProgram.exe")
```

## Future Improvements

- Implement automatic startup optimization algorithms.
- GUI for user-friendly interaction.
- Schedule periodic optimization checks.

## Disclaimer

This tool modifies system settings. Use with caution and ensure you have backups of important data.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.