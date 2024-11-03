from .prof_detail.spm import get_speech_speed
from .prof_detail.pause import get_pause_ratio
from .prof_detail.pronunciation import get_pronunciation_score

def eval_proficiency(input_conv_data, input_audio_list, input_stt_list):
    
    speed_score, speed_spm, speed_feedback = get_speech_speed(input_stt_list)

    pronunciation_score, pronunciation_level, pronunciation_feedback = get_pronunciation_score(input_audio_list)

    pause_score, pause_ratio, pause_feedback = get_pause_ratio(input_stt_list)

    proficiency_score = int((speed_score+pronunciation_score+pause_score)/3)
    proficiency_feedback = {
        'speed_score': int(speed_score),
        'speed_spm': speed_spm,
        'speed_feedback': speed_feedback,
        'pronunciation_score': int(pronunciation_score),
        'pronunciation_level': pronunciation_level,
        'pronunciation_feedback': pronunciation_feedback,
        'pause_score': int(pause_score),
        'pause_ratio': pause_ratio,
        'pause_feedback': pause_feedback
    }
    return proficiency_score, proficiency_feedback