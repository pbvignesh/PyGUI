"""
    GUI Application for commonly used Dev Operations
"""
from tkinter import Tk, Label, Entry, Button
import urllib.parse
import pyperclip

root = Tk()
root.title("DevToys")
root.geometry("750x450")

url_label = Label(root, text="Enter URL that needs to be encoded")
url_label.pack()

url_entry = Entry(root, width=80)
url_entry.focus_set()
url_entry.pack()

def encode_url_and_display_and_copy_to_clipboard():
    """
        Function to get the URL and encode it and then display it in the UI and
        copy it to the clipboard
    """
    url_to_encode = url_entry.get()
    encoded_url = urllib.parse.quote(url_to_encode, safe='')
    encoded_url_label.config(text=encoded_url)
    pyperclip.copy(encoded_url)


button = Button(root, text="Encode URL and Copy 📝", command=encode_url_and_display_and_copy_to_clipboard)
button.pack(pady=20)

encoded_url_label = Label(root, text="Encoded URL will appear here")
encoded_url_label.pack()

root.mainloop()
