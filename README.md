# ReadingTextFilePythonProject

This is a **Text-to-Speech (TTS) Text File Reader** written in Python.
It allows users to open a `.txt` file, read its contents, and listen to
the text using the `pyttsx3` library.

The project comes with a simple **Graphical User Interface (GUI)** built
using `tkinter`, where users can:
- Select a text file via file dialog.
- Set a custom reading speed before playback.

------------------------------------------------------------------------

## Features

-   Open and read any `.txt` file.
-   Text-to-Speech functionality using **pyttsx3**.
-   Customizable reading speed.
-   Lightweight and beginner-friendly Python project.

------------------------------------------------------------------------

## Installation

1.  Clone this repository:

    ``` bash
    git clone https://github.com/mayurcodes01/ReadingTextFilePythonProject.git
    cd ReadingTextFilePythonProject
    ```

2.  Install dependencies:

    ``` bash
    pip install pyttsx3
    ```

------------------------------------------------------------------------

## Usage

Run the script with Python:

``` bash
python main.py
```

1.  A file dialog will open → Select a `.txt` file.
2.  Enter your desired reading speed (default is system voice rate).
3.  The program will read the file aloud.

------------------------------------------------------------------------

## Example Code

``` python
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
```

------------------------------------------------------------------------

## Requirements

-   Python 3.x
-   `pyttsx3` library
-   `tkinter` (comes pre-installed with Python)

------------------------------------------------------------------------

## Future Improvements

-   Add pause/resume/stop functionality.
-   Support for multiple languages and voices.
-   GUI with buttons instead of dialogs.

------------------------------------------------------------------------

## License

This project is licensed under the MIT License.
