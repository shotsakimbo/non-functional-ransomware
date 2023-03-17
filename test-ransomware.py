import random
import string
from twilio.rest import Client
import tkinter as tk
from tkinter import messagebox

# generate a random encryption key
key = ''.join(random.choices(string.ascii_letters + string.digits, k=16))

# generate a random id number
id_number = str(random.randint(0, 999)).zfill(3)

# send key and id number through Twilio SMS
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)
message = client.messages.create(
    body=f'Encryption key: {key}\nID number: {id_number}',
    from_='your_twilio_phone_number',
    to='recipient_phone_number'
)

# declare key_entry as a global variable
global key_entry

# function to verify decryption key
def verify_key():
    input_key = key_entry.get()
    if input_key == key:
        messagebox.showinfo("Success", "Decryption key verified. No files to decrypt.")
    else:
        messagebox.showerror("Error", "Invalid decryption key. Please try again.")

# function to display GUI
def display_gui():
    global key_entry
    root = tk.Tk()
    root.geometry('300x150')
    root.title('Encryption Tool')

    # sms label
    sms_label = tk.Label(root, text="example: message laksjdhfajsd@gmail.com for decryption key")
    sms_label.pack(pady=5)

    # key label and entry
    key_label = tk.Label(root, text="Enter decryption key:")
    key_label.pack()
    key_entry = tk.Entry(root, show="*")
    key_entry.pack(pady=5)

    # verify button
    verify_button = tk.Button(root, text="Verify", command=verify_key)
    verify_button.pack()

    # id number label
    id_number_label = tk.Label(root, text=f'ID Number: {id_number}')
    id_number_label.pack(side=tk.BOTTOM)

    root.mainloop()

# start GUI
display_gui()
