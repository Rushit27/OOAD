from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import VideoFileClip, concatenate_videoclips
import moviepy.editor as mp
import os
import tkinter
from tkinter import filedialog
from browse import *

def cut_video(input_file,start_time, end_time):
    input_folder = os.path.dirname(input_file)
    output_file = os.path.join(input_folder, "output.mp4")
    ffmpeg_extract_subclip(input_file, start_time, end_time, targetname=output_file)

def concatenate_video(clip1,clip2):
    input_file1=VideoFileClip(f'{clip1}')
    input_file2=VideoFileClip(f'{clip2}')
    new_clip=concatenate_videoclips([input_file1,input_file2])
    file_path = filedialog.asksaveasfilename(
    title="Save Video As",
    filetypes=[("MP4 files", "*.mp4"), ("MP3 files", "*.mp3*")]
    )
    new_clip.write_videofile(file_path)