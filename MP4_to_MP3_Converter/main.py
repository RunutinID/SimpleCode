from pydub import AudioSegment

def convert_mp4_to_mp3(input_path, output_path):
    try:
        print("Mengonversi ke MP3...")
        audio = AudioSegment.from_file(input_path, format="mp4")
        audio.export(output_path, format="mp3")
        print("Konversi selesai.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    input_video_path = "Oragne.mp4"
    output_audio_path = "Orange.mp3"
    convert_mp4_to_mp3(input_video_path, output_audio_path)