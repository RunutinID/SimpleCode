from pytube import YouTube
from pydub import AudioSegment
import os
 
def download_youtube_audio(url, output_path='.'):
    # Mengunduh video YouTube
    print("Mengunduh video...")
    yt = YouTube(url)
    video_stream = yt.streams.filter(only_audio=True).first()
    
    # Mengambil judul video dari objek YouTube
    video_title = yt.title
    output_filename = video_title.replace(" ", "_").lower()  # Mengganti spasi dengan garis bawah dan mengonversi ke huruf kecil

    video_stream.download(output_path, filename=output_filename + ".mp4")

    # Mengonversi video ke format MP3
    print("Mengonversi ke MP3...")
    audio = AudioSegment.from_file(output_path + "/" + output_filename + ".mp4", format="mp4")
    audio.export(output_path + "/" + output_filename + ".mp3", format="mp3")

    # Menghapus file video MP4 (opsional)
    print("Menghapus file video MP4...")
    video_path = output_path + "/" + output_filename + ".mp4"
    if os.path.exists(video_path):
        os.remove(video_path)

    print("Unduhan audio selesai.")

if __name__ == "__main__":
    video_url = "https://www.youtube.com/watch?v=8QPyFlJNmus&list=RDOc9NgPgUO3E&index=11"
    download_youtube_audio(video_url)
