from utils.gpt import generate_gpt_response
from .metric.relevance import eval_relevance
from .metric.etiquette import eval_etiquette
from .metric.proficiency import eval_proficiency

def run_evaluation(input_conv_data, input_audio_list, input_stt_list):
    print("RUN EVALUATION...")
    # eval_relevance
    relevance_score = eval_relevance(input_conv_data)
    print(relevance_score)

    # eval_proficiency
    proficiency_score, proficiency_feedback = eval_proficiency(input_conv_data, input_audio_list, input_stt_list)
    
    # eval_etiquette
    etiquette_score, etiquette_feedback = eval_etiquette(input_conv_data)

    return {
        'relevance_score': int(relevance_score),
        'proficiency_score': int(proficiency_score),
        'proficiency_feedback': proficiency_feedback,
        'etiquette_score': int(etiquette_score),
        'etiquette_feedback': etiquette_feedback
    }
