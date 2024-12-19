import os
import platform
from datetime import datetime

# Define log file path
log_file = "/tmp/dummy_script.log"

# Write system information to the log file
def log_system_info():
    with open(log_file, "a") as file:
        file.write(f"{'-'*40}\n")
        file.write(f"Script Run at: {datetime.now()}\n")
        file.write("System Information:\n")
        file.write(f"OS: {platform.system()} {platform.release()}\n")
        file.write(f"Node Name: {platform.node()}\n")
        file.write(f"Processor: {platform.processor()}\n")
        file.write(f"Python Version: {platform.python_version()}\n")
        file.write(f"User: {os.getlogin()}\n")
        file.write(f"{'-'*40}\n")
    print(f"System information logged to: {log_file}")

# Main function
if __name__ == "__main__":
    print("Dummy Python Script is running...")
    log_system_info()
    print("Dummy Python Script completed successfully.")
