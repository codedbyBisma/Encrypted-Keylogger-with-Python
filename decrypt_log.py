from cryptography.fernet import Fernet

# ✅ Load the saved encryption key
with open(".encryption_key.key", "rb") as key_file:
    key = key_file.read()

cipher = Fernet(key)

# ✅ Load the encrypted log file
with open(".keystrokes_encrypted.log", "rb") as encrypted_file:
    encrypted_data = encrypted_file.read()

# ✅ Decrypt the data
try:
    decrypted_data = cipher.decrypt(encrypted_data)
except Exception as e:
    print(f"[!] Decryption failed: {e}")
    exit()

# ✅ Save the decrypted data to a file
output_file = "decrypted_keystrokes.txt"
with open(output_file, "wb") as f:
    f.write(decrypted_data)

# ✅ Print output to terminal
print(f"[+] Decryption complete. Decrypted log saved in '{output_file}'\n")
print(decrypted_data.decode())
