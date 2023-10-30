import tkinter as tk
import os
import subprocess
import shutil
from tkinter import filedialog as fd
from moviepy.editor import VideoFileClip, concatenate_videoclips


def openAAudioFile():
    files = fd.askopenfilename(
        title="Select an audio or video file",filetypes=[("MP3 files", "*.mp3")]
    )
    
    if files:
        # custom_player_exe = "path/to/your/custom/player.exe"
        # subprocess.Popen([custom_player_exe, os.path.abspath(files)])
        return files
    
def openAVideoFile():
    files = fd.askopenfilename(
        title="Select an audio or video file",filetypes=[("MP4 files", "*.mp4")]
    )
    
    if files:
        # custom_player_exe = "path/to/your/custom/player.exe"
        # subprocess.Popen([custom_player_exe, os.path.abspath(files)])
        return files

def savefile(input_file):
    file_path = fd.asksaveasfilename(
        title="Save As",
        filetypes=[("MP4 files", "*.mp4"), ("MP3 files", "*.mp3*")]
    )
    shutil.copy(f'{input_file}',file_path)



