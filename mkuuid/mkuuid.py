# -*- coding: utf-8 -*-

from tkinter import Tk
from tkinter import filedialog
from uuid import uuid4
import os.path
import sys

def main_gui():
    home = os.path.expanduser('~')
    root = Tk()
    root.withdraw()
    out_dir = filedialog.askdirectory(
        title='Choose output directory for UUID file',
        initialdir=home)
    if not out_dir:
        sys.exit()
    root.destroy()
    print(out_dir)
    uuid = uuid4().hex
    print(uuid)
    open(os.path.join(out_dir, 'uuid-{}'.format(uuid)), 'a').close()
 
    
if __name__ == '__main__':
    main_gui()
