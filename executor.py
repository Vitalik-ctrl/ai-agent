# executor.py

import subprocess
import platform

def execute_command(command):
    print(f"AI wants to run: {command}")
    approval = input("Approve? (y/n): ").strip().lower()
    
    if approval not in ["yes", "y"]:
        return "Command execution cancelled."

    system = platform.system()

    try:
        if system == "Windows":
            result = subprocess.run(["powershell", "-Command", command], capture_output=True, text=True, check=True)
        else:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)

        return result.stdout or "Command executed successfully (no output)."

    except subprocess.CalledProcessError as e:
        return f"Error: {e.stderr or str(e)}"
