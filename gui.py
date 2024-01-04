from tkinter import *

root = Tk()
root.geometry("750x450")

label = Label(root, text="Enter JSON Input")
label.pack()

entry = Entry(root, width=20)
entry.focus_set()
entry.pack()

def display_text():
    print("Hello World")

button = Button(root, text="Validate JSON", command=display_text)
button.pack(pady=20)

root.mainloop()