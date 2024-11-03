from pydantic import BaseModel


class StartConv(BaseModel):
    greetings: str

class ContinueConv(BaseModel):
    answer: str
    is_mission1: bool
    is_mission2: bool
    is_mission3: bool
    is_end: bool

class TerminateConv(BaseModel):
    answer: str
    is_mission1: bool
    is_mission2: bool
    is_mission3: bool
