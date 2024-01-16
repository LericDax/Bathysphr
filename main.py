import os
import tkinter as tk
from tkinter import filedialog
from pydub import AudioSegment

def convert_mp3_to_wav(input_folder):
    # Create an output folder for WAV files
    output_folder = os.path.join(input_folder, "Converted_WAV_Files")
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Convert each MP3 file to WAV
    for filename in os.listdir(input_folder):
        if filename.endswith(".mp3"):
            mp3_path = os.path.join(input_folder, filename)
            wav_filename = os.path.splitext(filename)[0] + ".wav"
            wav_path = os.path.join(output_folder, wav_filename)

            audio = AudioSegment.from_mp3(mp3_path)
            audio.export(wav_path, format="wav")

def select_folder():
    root.withdraw()  # Hide the main window
    folder_selected = filedialog.askdirectory()  # Show the folder selection dialog
    if folder_selected:
        convert_mp3_to_wav(folder_selected)

# Setting up the tkinter GUI
root = tk.Tk()
root.title("MP3 to WAV Converter")
select_button = tk.Button(root, text="Select Folder", command=select_folder)
select_button.pack(pady=20)
root.mainloop()
