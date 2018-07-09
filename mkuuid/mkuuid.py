from tkinter import Tk
from tkinter import filedialog
from uuid import uuid4
import os.path
import sys
import pyperclip

def main_gui():
    home = os.path.expanduser('~')
    root = Tk()
    root.withdraw()
    out_dir = filedialog.askdirectory(
        title='Choose output directory for UUID file',
        initialdir=home)
    if not out_dir:
        sys.exit()
    uuid = uuid4().hex
    fn = 'uuid-{}'.format(uuid)
    path = os.path.join(out_dir, fn)
    open(path, 'a').close()
    pyperclip.copy(fn)
    root.destroy()

if __name__ == '__main__':
    main_gui()
