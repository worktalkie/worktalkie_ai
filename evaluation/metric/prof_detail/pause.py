from ...constants import PauseRatioFeedback

from statistics import mean
import string

def remove_punctuation(text):
    return text.translate(str.maketrans('', '', string.punctuation))

def cal_pause_ratio(input_stt_list):
    pause_list = []
    for turn in input_stt_list:
        data = turn['data']['segments'][0]
        if len(turn['data']['segments']) !=1:
            print("data.segment 확인 요망")
            exit()
        start_time = data['words'][0][0]
        end_time = data['words'][-1][1]

        speech_time = 0
        for word in data['words']:
            sentence = remove_punctuation(word[2])
            if sentence not in ['음', '어', '어어', '으음']:
                speech_time += word[1]-word[0]
        
        pause_ratio = ((end_time-start_time)-speech_time)/(end_time-start_time)
        pause_list.append(pause_ratio)
    print(pause_list)
    return mean(pause_list)

def pause_rating(pause_ratio):
    if pause_ratio <= 0.3:
        return 100, PauseRatioFeedback.MODERATE
    elif 0.3 < pause_ratio <= 0.4:
        return 90, PauseRatioFeedback.SLIGHTLY_HIGH
    elif 0.4 < pause_ratio <= 0.5:
        return 70, PauseRatioFeedback.HIGH
    else:
        return 50, PauseRatioFeedback.VERY_HIGH
    
def get_pause_ratio(input_stt_list):
    pause_ratio = cal_pause_ratio(input_stt_list)
    pause_score, pause_feedback = pause_rating(pause_ratio)
    return pause_score, pause_ratio, pause_feedback