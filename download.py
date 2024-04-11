from pytube import YouTube
import os

def download(url, path):
    if not os.path.exists(path):
        os.makedirs(path)

    yt = YouTube(url)

    audio = yt.streams.filter(only_audio=True).first()
    if audio:
        audio.download(output_path=path)
        for content in os.listdir(path):
            if content.split(".").pop() == "mp4":
                base_name, _ = os.path.splitext(path+"/"+content)
                new_file_path = base_name + "." + "mp3"
                os.rename(path+"/"+content, new_file_path)
