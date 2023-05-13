from tkinter.filedialog import askdirectory, askopenfilename, asksaveasfile
import tkinter
import os
from enum import Enum, auto
import ctypes

try:
    ctypes.windll.shcore.SetProcessDpiAwareness(1)
except AttributeError:
    pass


class DirPathMode(Enum):
    File = auto()
    Directory = auto()
    Saving = auto()


def get_dir_path(par: DirPathMode, title='Open'):
    """
    Receive paths to objects using graphical interface
    :param par: type of object
    :param title: helping text for graphical interface
    :return: path to object
    """
    tkinter.Tk().withdraw()

    if par == DirPathMode.File:
        ans = askopenfilename(title=title, initialdir="/")

    elif par == DirPathMode.Directory:
        ans = askdirectory(title=title, initialdir="/")

    else:
        t_ans = asksaveasfile(title=title, initialdir="/", defaultextension='.pdf')
        ans = t_ans.name
        t_ans.close()
        os.remove(ans)

    return ans


def get_dir_name(path):
    return os.path.dirname(path)
