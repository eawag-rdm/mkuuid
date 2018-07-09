from tkinter import Tk
from tkinter import filedialog
from uuid import uuid4
from os import path, getcwd
from sys import exit

def main_gui():
    cwd = getcwd()
    root = Tk()
    root.withdraw()
    out_dir = filedialog.askdirectory(
        title='Choose output directory for UUID file',
        initialdir=cwd)
    if not out_dir:
        exit()
    root.destroy()
    uuid = uuid4().hex
    open(path.join(out_dir, 'uuid-{}'.format(uuid)), 'a').close()
 
    
if __name__ == '__main__':
    main_gui()
