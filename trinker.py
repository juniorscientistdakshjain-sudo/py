from tkinter import *

# Create window
root = Tk()
root.title("Number Pad")
root.geometry("300x300")
root.resizable(False, False)

# Numbers to display
nums = [
    9, 8, 7,
    6, 5, 4,
    3, 2, 1,
    "*", 0, "+"
]

# Configure grid rows & columns
for i in range(4):
    root.rowconfigure(i, weight=1, minsize=75)
    root.columnconfigure(i, weight=1, minsize=75)

# Create buttons using frames
row = 0
col = 0

for num in nums:
    frame = Frame(
        master=root,
        relief=SUNKEN,
        borderwidth=1
    )
    frame.grid(row=row, column=col, sticky="nsew")

    label = Label(
        master=frame,
        text=num,
        bg="#d0efff",
        font=("Arial", 16)
    )
    label.pack(expand=True, fill="both", padx=5, pady=5)

    col += 1
    if col == 3:
        col = 0
        row += 1

# Start GUI loop
root.mainloop()
