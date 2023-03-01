# Download Audio from YouTube Video

This Python script allows you to download the audio from a YouTube video in the form of an MP3 file. It uses the `pytube` library to download the video and `moviepy` to convert it to MP3.

## Requirements

- Python 3.x
- pytube
- moviepy

## Installation

1. Clone the repository or download the ZIP file and extract its contents.
2. Install the required libraries by running the following command:

pip install -r requirements.txt


## Usage

1. Run the script by navigating to the directory where it is saved and typing the following command:
```bash 
python download-audio-video-yb.py
```

2. Enter the URL of the YouTube video when prompted.
3. Enter the destination folder where you want to save the MP3 file. If you leave this blank, the file will be saved in the current directory.
4. The script will display a progress bar while the video is downloading and converting.
5. Once the conversion is complete, the MP3 file will be saved in the destination folder you specified.

## Get Started

To get started with the script, you need to obtain your YouTube API key. You can get this by following these steps:

1. Go to the [Google Developers Console](https://console.developers.google.com/).
2. Create a new project.
3. Enable the YouTube Data API for your project.
4. Create an API key for your project.
5. Copy your API key and use it in the script where prompted.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

