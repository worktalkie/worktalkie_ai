from utils.gpt import generate_gpt_response
from .utils import format_script, get_response_format
from .constants import SCRIPTS_PATH, SYSTEM_PROMPT

def determine_status(dialogue):
    turn_num = len(dialogue)
    if turn_num == 0:
        return "start_conversation"
    elif turn_num >= 20:
        return "terminate_conversation"
    else:
        return "continue_conversation"

def update_missions(input_data, response):
    for i in range(3):
        input_data['is_missions_completed'][i] = (
            response.get(f'is_mission{i+1}', False) or input_data['is_missions_completed'][i]
        )

    return input_data

def update_is_end(input_data, response, status):
    if status == "terminate_conversation":
        input_data['is_end'] = True  # 대화가 종료되는 경우
    else:  # continue_conversation 경우
        input_data['is_end'] = response.get('is_end', input_data.get('is_end', False))
    
    return input_data

def run_conversation(input_data):
    print("RUN CONVERSATION...")

    # 상태 결정 (start, continue, terminate)
    status = determine_status(input_data['dialogue'])

    # 스크립트 파일 경로 설정
    script_path = f"{SCRIPTS_PATH}/{status}.txt"

    # 스크립트 파일 읽기
    with open(script_path, "r", encoding="utf-8") as file:
        script = file.read()

    # 스크립트 포맷
    formatted_script = format_script(script, input_data)
    print(formatted_script)
    
    # 응답 형식 설정
    response_format = get_response_format(status)

    # GPT 모델 호출
    response = generate_gpt_response(
        formatted_script, response_format, SYSTEM_PROMPT
    )
    print(response)

    # 대화 업데이트
    if status == "start_conversation":
        input_data['dialogue'].append({"AI": response['greetings']})
    # 대화+미션 업데이트
    else:
        input_data['dialogue'].append({"AI": response['answer']})
        input_data = update_missions(input_data, response)
        input_data = update_is_end(input_data, response, status)
    

    return input_data
