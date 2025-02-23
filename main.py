# main.py
import tkinter as tk
from tkinter import messagebox, ttk
from utils.gmail_utils import authenticate_gmail, fetch_emails
from spam_model import is_spam
import threading

LOG_FILE = "log.txt"

def log_spam_email(email_data):
    with open(LOG_FILE, "a") as log:
        log.write(f"From: {email_data['from']}\n")
        log.write(f"Subject: {email_data['subject']}\n")
        log.write(f"Snippet: {email_data['snippet']}\n")
        log.write("-" * 50 + "\n")

def check_for_spam():
    try:
        # Start the Gmail API authentication
        service = authenticate_gmail()
        progress_label.config(text="Fetching emails...")
        emails = fetch_emails(service)
        
        # Begin checking each email for spam
        progress_label.config(text="Checking for spam...")
        for email in emails:
            if is_spam(email["snippet"]):
                log_spam_email(email)
        
        progress_label.config(text="Completed! Check log for details.")
        messagebox.showinfo("Process Completed", "Spam check completed. Check the log file for details.")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")
    finally:
        progress_bar.stop()

def start_spam_check():
    email_address = email_entry.get()
    if not email_address:
        messagebox.showwarning("Input Required", "Please enter your Gmail address.")
        return
    
    progress_label.config(text="Starting spam check...")
    progress_bar.start()
    
    # Use a separate thread to prevent freezing the UI during the email fetching process
    threading.Thread(target=check_for_spam).start()

# GUI Setup
root = tk.Tk()
root.title("Spam Checker")
root.geometry("400x300")
root.configure(bg="#f0f0f0")

# Title label
title_label = tk.Label(root, text="Spam Checker for Gmail", font=("Helvetica", 16, "bold"), bg="#f0f0f0")
title_label.pack(pady=10)

# Instruction label
instruction_label = tk.Label(root, text="Enter your Gmail address below to check for spam emails.", bg="#f0f0f0")
instruction_label.pack(pady=5)

# Email entry field
email_frame = tk.Frame(root, bg="#f0f0f0")
email_frame.pack(pady=10)
email_entry_label = tk.Label(email_frame, text="Gmail Address:", bg="#f0f0f0")
email_entry_label.grid(row=0, column=0, padx=5)
email_entry = tk.Entry(email_frame, width=30)
email_entry.grid(row=0, column=1)

# Start button
start_button = tk.Button(root, text="Start Spam Check", command=start_spam_check, bg="#4CAF50", fg="white", font=("Helvetica", 12, "bold"))
start_button.pack(pady=20)

# Progress bar and label
progress_label = tk.Label(root, text="", bg="#f0f0f0")
progress_label.pack(pady=5)
progress_bar = ttk.Progressbar(root, mode="indeterminate", length=250)
progress_bar.pack(pady=5)

root.mainloop()
