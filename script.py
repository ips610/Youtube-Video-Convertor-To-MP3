import os
from pytube import YouTube
import certifi
os.environ["SSL_CERT_FILE"] = certifi.where()

def download_youtube_audio(url, output_path="."):
    try:
        # Create a YouTube object
        youtube = YouTube(url)

        # Get the audio stream with the highest quality
        audio_stream = youtube.streams.filter(only_audio=True, file_extension='mp4').first()

        # Determine the parent folder of the script's location
        script_directory = os.path.dirname(os.path.realpath(__file__))
        parent_folder = os.path.abspath(os.path.join(script_directory, ".."))

        # Combine the parent folder with the provided output path
        output_folder = os.path.abspath(os.path.join(parent_folder, output_path))

        # Download the audio stream
        audio_stream.download(output_folder)

        print(f"Download successful: {audio_stream.title}")

    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    # Replace 'your_youtube_video_url' with the actual YouTube video URL
    video_url = input("Enter YouTube video URL: ")
    
    # Specify the relative path to the output folder
    output_folder = input("Enter output folder relative to parent folder (press Enter for current folder): ") or "."

    download_youtube_audio(video_url, output_folder)
