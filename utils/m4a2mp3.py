import os
from pydub import AudioSegment

input_directory = 'data/test_audio'
for filename in os.listdir(input_directory):
    if filename.endswith(".m4a"):
        m4a_path = os.path.join(input_directory, filename)
        mp3_filename = filename.replace(".m4a", ".mp3")
        mp3_path = os.path.join(input_directory, mp3_filename)

        audio = AudioSegment.from_file(m4a_path, format="m4a")
        audio.export(mp3_path, format="mp3")
        print(f"{filename} -> {mp3_filename} 변환 완료.")
