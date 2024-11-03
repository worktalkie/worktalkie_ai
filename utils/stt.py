import json
import os

from clova_speech_client import ClovaSpeechClient

def process_stt(input_audio_path, output_json_path):
    # ClovaSpeechClient 인스턴스 생성
    client = ClovaSpeechClient()

    # 오디오 파일 전송 및 결과 받기
    try:
        response = client.req_upload(input_audio_path=input_audio_path, completion='sync')

        # 응답 결과를 json 파일로 저장
        if response.status_code == 200:
            result = response.json()
            with open(output_json_path, 'w', encoding='utf-8') as json_file:
                json.dump(result, json_file, ensure_ascii=False, indent=4)
            print(f"Transcription saved to {output_json_path}")
        else:
            print(f"Failed to transcribe audio. Status code: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"An error occurred: {e}")

def process_stt_from_folder(input_audio_folder, output_json_folder):
    # 입력 폴더에 있는 모든 파일 목록을 가져옴
    if not os.path.exists(output_json_folder):
        os.makedirs(output_json_folder)

    for filename in os.listdir(input_audio_folder):
        input_audio_path = os.path.join(input_audio_folder, filename)

        # 오디오 파일만 처리하기 위해 확장자 확인
        if os.path.isfile(input_audio_path) and filename.lower().endswith(('.mp3', '.wav', '.m4a')):
            output_filename = f"{os.path.splitext(filename)[0]}.json"
            output_json_path = os.path.join(output_json_folder, output_filename)

            # 오디오 파일을 변환하고 JSON으로 저장
            process_stt(input_audio_path, output_json_path)

# 사용 예시
input_audio_folder = 'data/test_audio'  # 오디오 파일들이 저장된 폴더
output_json_folder = 'data/test_text'   # 변환된 결과를 저장할 폴더

process_stt_from_folder(input_audio_folder, output_json_folder)