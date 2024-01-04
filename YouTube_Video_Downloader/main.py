from pytube import YouTube

def download_youtube_video(url, output_path='.'):
    # Mengunduh video YouTube
    print("Mengunduh video...")
    yt = YouTube(url)
    video_stream = yt.streams.get_highest_resolution()
    video_stream.download(output_path)

    print("Unduhan video selesai.")

if __name__ == "__main__":
   video_url = "https://www.youtube.com/watch?v=d6qCbdXqsOs"
   download_youtube_video(video_url)