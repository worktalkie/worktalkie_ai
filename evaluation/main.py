import os
import json
import argparse
from .eval import run_evaluation
from pydub import AudioSegment
from pydub.utils import which

def load_input_data(input_file):
    with open(input_file, 'r') as f:
        return json.load(f)

def load_user_audio_folder(folder_path):
    audio_files = []

    # 폴더 내 모든 파일을 탐색
    for file_name in os.listdir(folder_path):
        # .mp3 확장자를 가진 파일만 처리
        if file_name.endswith('.mp3'):
            audio_path = os.path.join(folder_path, file_name)
            # MP3 파일을 AudioSegment로 읽어들임
            AudioSegment.converter = which("ffmpeg")
            audio = AudioSegment.from_mp3(audio_path)
            # 파일 제목과 오디오 객체를 딕셔너리로 묶어서 리스트에 추가
            audio_files.append({
                'title': file_name,      # 파일 이름 (제목)
                'audio': audio           # AudioSegment 객체
            })

    return audio_files

def load_user_stt_folder(json_folder_path):
    json_data_list = []

    # 폴더 내의 모든 파일을 순회
    for filename in os.listdir(json_folder_path):
        file_path = os.path.join(json_folder_path, filename)

        # JSON 파일만 처리
        if os.path.isfile(file_path) and filename.lower().endswith('.json'):
            try:
                # 파일명에서 ID 추출 (예: USER_0001 -> 1)
                file_id = int(filename.split('_')[1].split('.')[0])

                # JSON 파일 읽기
                with open(file_path, 'r', encoding='utf-8') as json_file:
                    data = json.load(json_file)

                # ID와 JSON 데이터를 포함한 딕셔너리 형태로 추가
                json_data_list.append({'id': file_id, 'data': data})
            except Exception as e:
                print(f"Failed to load {file_path}: {e}")
    
    json_data_list = sorted(json_data_list, key=lambda x: x['id'])

    return json_data_list

def save_output_data(output_file, output_data):
    with open(output_file, 'w', encoding='utf-8') as json_file:
        json.dump(output_data, json_file, ensure_ascii=False, indent=4)

def main():
    parser = argparse.ArgumentParser(description='Process a JSON file and send it to the GPT API.')
    parser.add_argument('input_conv_file', type=str, help='The path to the JSON input file.')
    parser.add_argument('input_audio_folder', type=str, help='The path to the MP3 input file.')
    parser.add_argument('input_stt_folder', type=str, help='The path to the JSON input file.')
    parser.add_argument('result_file', type=str, help='The path to the JSON output file.')

    args = parser.parse_args()

    input_conv_data = load_input_data(args.input_conv_file)
    input_audio_list = load_user_audio_folder(args.input_audio_folder)
    input_stt_list = load_user_stt_folder(args.input_stt_folder)

    output_data = run_evaluation(input_conv_data, input_audio_list, input_stt_list)
    save_output_data(args.result_file, output_data)

if __name__ == "__main__":
    main()
