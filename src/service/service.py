from moviepy import AudioFileClip

def mp4_to_mp3(mp4_path: str, mp3_path: str):
    convert = AudioFileClip(mp4_path)
    convert.write_audiofile(mp3_path)
    convert.close()
