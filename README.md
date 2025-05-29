# 🔐 Encrypted-Keylogger-with-Python
A basic keylogger built with Python using pynput and Fernet encryption. Captures keystrokes and encrypts logs for secure storage. Includes a decryption utility to access recorded logs securely.

---

## ⚙️ Features

- Captures user keystrokes with precise timestamps
  
- Logs system information (user, hostname, OS, processor)
  
- Encrypts the keystroke log file using Fernet (symmetric encryption)
  
- Decryption script to view the log securely
  
- Hides sensitive log files using dot-prefixed filenames
  
- Ignores and protects sensitive files from being uploaded

---

## 🗂️ Project Structure

```bash
├── keylogger.py             # Main script to log and encrypt keystrokes

├── decrypt_log.py           # Script to decrypt the encrypted log

├── .gitignore               # Prevents uploading of sensitive files

├── README.md                # Project documentation

🚀 How It Works

Run keylogger.py

It begins logging your keystrokes into a hidden .keystrokes.log file. Once the script ends (e.g. via Ctrl+C), it encrypts the log and saves it as .keystrokes_encrypted.log. The original log is deleted.

Run decrypt_log.py

This script reads the encrypted log and decrypts it using the stored Fernet key (.encryption_key.key). The output is saved to decrypted_keystrokes.txt.

🔐 Security Notes

This project is for educational purposes only.

Do not use it to log user activity without consent.

The encryption key is stored locally in .encryption_key.key and should not be uploaded or shared.

Log files and decrypted outputs are ignored using .gitignore.

📦 Requirements

Install dependencies using:

pip install pynput cryptography

📝 Usage

Run the keylogger:

python3 keylogger.py

❌ Files Not Uploaded

For security reasons, the following files are not included in the GitHub repo:

.keystrokes.log

.keystrokes_encrypted.log

.encryption_key.key

decrypted_keystrokes.txt

These are listed in .gitignore.

✅ Disclaimer

This project is created solely for learning and demonstration purposes. Misuse of this code is not the responsibility of the developer. Always ensure ethical use of monitoring tools.

📄 License

This project is licensed under the MIT License - feel free to use, modify, and share with attribution.

✍️ Author

Bisma Khushi
