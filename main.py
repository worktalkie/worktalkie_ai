from fastapi import FastAPI
from pydantic import BaseModel
import os
import json
import subprocess

app = FastAPI()

class ScenarioData(BaseModel):
    scenario: str
    background: str
    role_of_ai: str
    missions: list
    is_missions_completed: list
    is_end: bool
    dialogue: list

@app.post("/conversation/talk")
async def process_scenario(data: ScenarioData):
    current_dir = os.path.dirname(os.path.realpath(__file__))
    # 파일 경로 생성
    input_file_path = os.path.join(current_dir, "data", "user_conv", "input.json")
    output_file_path = os.path.join(current_dir, "results", "output.json")

    # 인풋 JSON 파일로 저장
    with open(input_file_path, "w") as infile:
        print("Saving input data to", input_file_path)
        json.dump(data.dict(), infile, ensure_ascii=False, indent=4)
    
    # 파이썬 스크립트 실행
    command = f"python3 -m conversation.main {input_file_path} {output_file_path}"
    process = subprocess.run(command, shell=True, capture_output=True, text=True)
    
    # 스크립트 실행 에러 확인
    if process.returncode != 0:
        return {"error": process.stderr}
    
    # 출력 파일 읽기
    with open(output_file_path, "r") as outfile:
        output_data = json.load(outfile)
    
    return output_data
