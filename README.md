# ReadngTextFilePythonProject
This is a Text-to-Speech (TTS) Text File Reader written in Python. It provides users with the ability to open a .txt file, read its contents, and speak the text out using the pyttsx3 library. The project includes a basic graphical user interface using tkinter, where users can open a file using a file dialog and specify a custom reading speed.

Install pyttsx3:
-----------------------------------------------
`pip install pyttsx3`

-----------------------------------------------

import pyttsx3
import tkinter as tk
from tkinter import filedialog, simpledialog

def read_text_file():
    file_path = filedialog.askopenfilename(title="Select a Text File", filetypes=[("Text Files", "*.txt")])
    if file_path: 
        with open(file_path, "r") as book:
            book_text = book.readlines()
        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        new_rate = simpledialog.askinteger("Input", "Enter reading speed (default: {}):".format(rate))
        if new_rate:
            engine.setProperty('rate', new_rate)
        for line in book_text:
            engine.say(line)
            engine.runAndWait()
        print("The file has been read...")

root = tk.Tk()
root.withdraw() 

read_text_file()
