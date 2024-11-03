from utils.gpt import generate_gpt_response

from ..models import EvalEtiqList
from ..constants import SCRIPTS_PATH, SCRIPTS_NAME, SYSTEM_PROMPT

def format_script(script: str, input_data: dict) -> str:

    return script.format(
        dialogue=input_data['dialogue']
    )
def count_user_dialogue(input_data):
    return sum(1 for item in input_data.get('dialogue', []) if 'User' in item)

def generate_gpt_response_with_retry(formatted_script, response_format, system_prompt, valid_len, max_retries=3):
    retries = 0
    while retries < max_retries:
        # GPT 모델 호출
        response = generate_gpt_response(formatted_script, response_format, system_prompt)
        print(response)

        res_len = len(response['dialogue'])
        # response 길이가 valid_len과 같은지 확인
        if res_len == valid_len:
            return response  # 성공하면 반환

        # 길이가 맞지 않으면 재시도
        retries += 1
        print(f"Response 길이가 맞지 않습니다. 재시도 중... ({retries}/{max_retries})")

    # 최대 재시도에 도달한 경우 오류 메시지 출력
    raise ValueError(f"Response 길이가 {valid_len}과 맞지 않습니다. 최대 {max_retries}번 재시도했으나 실패했습니다.")

def cal_manners_score(dialogue):
    """
    dialogue 리스트에서 expression_type이 0인 경우를 계산하고,
    매너에 어긋나지 않은 비율을 10의 자리에서 반올림하여 점수로 반환하는 함수.
    """
    # 매너에 어긋나지 않은 턴 (expression_type이 0인 경우)
    manners_turns = sum(1 for turn in dialogue if turn['expression_type'] == 0)
    
    # 전체 턴 개수
    total_turns = len(dialogue)
    
    # 매너에 어긋나지 않은 턴의 비율을 계산하고 10의 자리에서 반올림
    if total_turns > 0:
        score = round((manners_turns / total_turns) * 100, -1)
    else:
        score = 0  # 턴이 없을 경우 0점
    
    return score

def process_dialogue(response):
    for dialogue in response['dialogue']:
        if dialogue.get('expression_type') == 0:
            dialogue['feedback'] = None
            dialogue['fixed_turn'] = None
    return response

def eval_etiquette(input_conv_data):

    # 스크립트 파일 경로 설정
    script_path = f"{SCRIPTS_PATH}/{SCRIPTS_NAME}.txt"

    # 스크립트 파일 읽기
    with open(script_path, "r", encoding="utf-8") as file:
        script = file.read()

    # 스크립트 포맷
    formatted_script = format_script(script, input_conv_data)
    print(formatted_script)
    
    response_format = EvalEtiqList
    valid_len = count_user_dialogue(input_conv_data)

    # GPT 모델 호출
    try:
        response = generate_gpt_response_with_retry(
            formatted_script, response_format, SYSTEM_PROMPT, valid_len
            )
    except ValueError as e:
        print(f"오류 발생: {e}")

    score = cal_manners_score(response['dialogue'])
    response = process_dialogue(response)

    feedback = response['dialogue']

    return score, feedback