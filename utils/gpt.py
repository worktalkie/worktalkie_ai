import os
from openai import OpenAI

import time
import json

from dotenv import load_dotenv

load_dotenv(verbose=True)

api_key = os.getenv("OPENAI_API_KEY")
if api_key is None:
    raise ValueError("OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
client = OpenAI(api_key=api_key)


def call_gpt_api(messages, response_format, model="gpt-4o-mini", temperature=0.7, retries=3):
    attempt = 0
    while attempt < retries:
        try:
            response = client.beta.chat.completions.parse(  # 최신 인터페이스
                model=model,
                messages=messages,
                response_format=response_format,
                temperature=temperature,
            )
            response_text = response.choices[0].message.content
            response_json = json.loads(response_text)
            return response_json
        except Exception as e:
            attempt += 1
            print(f"Attempt {attempt} failed: {e}")
            time.sleep(2)
            if attempt == retries:
                print("Max retries reached. No response.")
                return None

def generate_gpt_response(user_message, response_format, system_message="You are a helpful assistant."):
    
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": user_message}
    ]

    return call_gpt_api(messages, response_format)
