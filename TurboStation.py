import os
import subprocess
import winreg

class TurboStation:
    def __init__(self):
        self.startup_registry_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        self.startup_folder_path = os.path.join(os.environ['APPDATA'], r"Microsoft\Windows\Start Menu\Programs\Startup")

    def list_startup_programs(self):
        print("Listing startup programs from registry:")
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_registry_path) as key:
            i = 0
            try:
                while True:
                    name, value, _ = winreg.EnumValue(key, i)
                    print(f"{name}: {value}")
                    i += 1
            except OSError:
                pass

        print("\nListing startup programs from startup folder:")
        for item in os.listdir(self.startup_folder_path):
            print(f"Startup Folder: {item}")

    def disable_startup_program(self, program_name):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_registry_path, 0, winreg.KEY_SET_VALUE) as key:
            try:
                winreg.DeleteValue(key, program_name)
                print(f"Program {program_name} disabled from registry startup.")
            except FileNotFoundError:
                print(f"Program {program_name} not found in registry startup.")

    def enable_startup_program(self, program_name, program_path):
        with winreg.OpenKey(winreg.HKEY_CURRENT_USER, self.startup_registry_path, 0, winreg.KEY_SET_VALUE) as key:
            winreg.SetValueEx(key, program_name, 0, winreg.REG_SZ, program_path)
            print(f"Program {program_name} enabled to start from registry.")

    def optimize_startup(self):
        print("Optimizing startup...")
        # Placeholder for optimization logic
        print("Optimization complete. System boot times should be improved.")

def main():
    turbo_station = TurboStation()
    turbo_station.list_startup_programs()
    # Example usage:
    # turbo_station.disable_startup_program("MyProgram")
    # turbo_station.enable_startup_program("MyProgram", r"C:\Path\To\MyProgram.exe")
    # turbo_station.optimize_startup()

if __name__ == "__main__":
    main()