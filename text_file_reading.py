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
