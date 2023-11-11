import tkinter as tk
from tkinter import filedialog

def select_files():
    file_paths = filedialog.askopenfilenames()
    # Do something with the selected file paths, for example, print them
    print("Selected files:", file_paths)

root = tk.Tk()
root.title("File Selection")
root.geometry("500x500")  # Set the window size to 500x500

# Create a label
label = tk.Label(root, text="Select Json files")
label.pack(pady=10)

# Create a button to select multiple files
select_button = tk.Button(root, text="Select Files", command=select_files)
select_button.pack(pady=20)

root.mainloop()
