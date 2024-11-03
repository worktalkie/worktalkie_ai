from pydantic import BaseModel
from typing import List
from enum import Enum

class ExpressionType(Enum):
    PERFECT = 0  # 완벽한 표현
    SLANG = 1  # 비속어/은어/축약어 사용
    INCOMPLETE = 2  # 비문, 문장이 끝나지 않은 경우
    IMPOLITE = 3  # 실례가 될 수 있는 표현
    UNPROFESSIONAL = 4  # 덜 전문적인 문장

class EvalEtiq(BaseModel):
    turn: str
    expression_type: ExpressionType
    feedback: str
    fixed_turn: str

class EvalEtiqList(BaseModel):
    dialogue: List[EvalEtiq]