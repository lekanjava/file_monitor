# src/main.py
import psutil
import logging

# Configure logging
logging.basicConfig(filename='activity.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def monitor_processes():
    for proc in psutil.process_iter(['pid', 'name', 'cmdline']):
        try:
            if proc.info['name'] in ['cmd.exe', 'powershell.exe']:
                logging.info(f"Detected: {proc.info['name']} (PID: {proc.info['pid']})")
                logging.info(f"Command Line: {' '.join(proc.info['cmdline'])}")
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass

if __name__ == "__main__":
    print("Monitoring CMD and PowerShell activity...")
    while True:
        monitor_processes()
