import youtube_dl
import os
from tqdm import tqdm

# Define the options for youtube_dl
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': '%(title)s.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }]
}

# Get the URL of the YouTube video to download
url = input("Enter the URL of the YouTube video: ")

# Create a youtube_dl object with the options
with youtube_dl.YoutubeDL(ydl_opts) as ydl:

    # Extract the video information to get the title
    video_info = ydl.extract_info(url, download=False)
    video_title = video_info['title']
    print(f"Downloading audio from '{video_title}'...")

    # Download the audio stream and save as MP3 file
    ydl.download([url])

# Get the downloaded file path
audio_file_path = os.path.join(os.getcwd(), f"{video_title}.mp3")

# Verify that the file was downloaded successfully
if os.path.isfile(audio_file_path):
    print("Audio file downloaded successfully!")
else:
    print("There was an error downloading the audio file.")

# Use tqdm to show progress bar while copying the file to another folder
destination = input("Enter the destination folder (leave blank for current folder): ")
if destination == "":
    destination = "."
with open(audio_file_path, 'rb') as f:
    with tqdm(total=os.path.getsize(audio_file_path), unit='B', unit_scale=True, desc=f"Copying '{video_title}.mp3' to '{destination}'") as pbar:
        with open(os.path.join(destination, f"{video_title}.mp3"), 'wb') as f2:
            while True:
                # Read in 1MB chunks
                chunk = f.read(1024 * 1024)
                if not chunk:
                    break
                f2.write(chunk)
                pbar.update(len(chunk))

# Verify that the file was copied successfully
if os.path.isfile(os.path.join(destination, f"{video_title}.mp3")):
    print("Audio file copied successfully!")
else:
    print("There was an error copying the audio file.")
