from pytube import YouTube
import os
from tqdm import tqdm

# Get the URL of the YouTube video to download
url = input("Enter the URL of the YouTube video: ")

# Create a YouTube object and select the audio stream
yt = YouTube(url)
audio = yt.streams.filter(only_audio=True).first()

# Get the destination folder to save the file
destination = input("Enter the destination folder (leave blank for current folder): ")
if destination == "":
    destination = "."

# Download the audio stream and save as MP3 file
out_file = audio.download(output_path=destination, filename="temp")
base, ext = os.path.splitext(out_file)
new_file = os.path.join(destination, base + '.mp3')
os.rename(out_file, new_file)

# Add a progress bar to the download process
with open(new_file, 'rb') as f:
    total_size = os.path.getsize(new_file)
    pbar = tqdm(total=total_size, unit='B', unit_scale=True)
    while True:
        buffer = f.read(8192)
        if not buffer:
            break
        pbar.update(len(buffer))
    pbar.close()

# Verify that the file was downloaded successfully
if os.path.isfile(new_file):
    print("Audio file downloaded successfully!")
else:
    print("There was an error downloading the audio file.")
