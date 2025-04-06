# executor.py

import subprocess

def execute_command(command):
    print(f"\AI wants to run: {command}")
    approval = input("Approve? (y/n): ").strip().lower()
    if approval in ["yes", "y"]:
        try:
            result = subprocess.run(command, shell=True, check=True, text=True, capture_output=True)
            return result.stdout
        except subprocess.CalledProcessError as e:
            return f"Error: {e}"
    else:
        return "Command execution cancelled."
