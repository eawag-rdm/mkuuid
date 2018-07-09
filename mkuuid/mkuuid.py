from tkinter import Tk
from tkinter import filedialog
from uuid import uuid4
from os import path, getcwd
from sys import exit
import pyperclip

def main_gui():
    cwd = getcwd()
    root = Tk()
    root.withdraw()
    out_dir = filedialog.askdirectory(
        title='Choose output directory for UUID file',
        initialdir=cwd)
    if not out_dir:
        exit()
    uuid = uuid4().hex
    fn = 'uuid-{}'.format(uuid)
    path = path.join(out_dir, fn)
    open(path, 'a').close()
    pyperclip.copy(fn)
    root.destroy()
 
    
if __name__ == '__main__':
    main_gui()
