import os
import subprocess
import tkinter as tk
from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
from tkinter import filedialog

os.system("cls & title bat to py #Free") # ความกว้่างของ Ui ของต่อย

lockreal = r"""

                                             
    ██████╗  █████╗ ████████╗    ████████╗ ██████╗     ██████╗ ██╗   ██╗████████╗██╗  ██╗ ██████╗ ███╗   ██╗
    ██╔══██╗██╔══██╗╚══██╔══╝    ╚══██╔══╝██╔═══██╗    ██╔══██╗╚██╗ ██╔╝╚══██╔══╝██║  ██║██╔═══██╗████╗  ██║
    ██████╔╝███████║   ██║          ██║   ██║   ██║    ██████╔╝ ╚████╔╝    ██║   ███████║██║   ██║██╔██╗ ██║
    ██╔══██╗██╔══██║   ██║          ██║   ██║   ██║    ██╔═══╝   ╚██╔╝     ██║   ██╔══██║██║   ██║██║╚██╗██║
    ██████╔╝██║  ██║   ██║          ██║   ╚██████╔╝    ██║        ██║      ██║   ██║  ██║╚██████╔╝██║ ╚████║
    ╚═════╝ ╚═╝  ╚═╝   ╚═╝          ╚═╝    ╚═════╝     ╚═╝        ╚═╝      ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚═╝  ╚═══╝

                                       ENTER TO CONVERT BAT TO PYTHON
        """[1:]

Anime.Fade(Center.Center(lockreal), Colors.red_to_blue, Colorate.Vertical, enter=True)

root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename(
    title="Select batch file",
    filetypes=[("Batch files", "*.bat"), ("All files", "*.*")]
)

if not file_path:
    exit()

with open(file_path, 'r') as batch_file:
    batch_contents = batch_file.read()

python_code = """import os
import subprocess

{}

""".format('\n'.join(f"subprocess.call('{command}', shell=True)" for command in batch_contents.splitlines()))

script_path = os.path.splitext(file_path)[0] + ".py"
with open(script_path, 'w') as python_file:
    python_file.write(python_code)

subprocess.call(['python', script_path])