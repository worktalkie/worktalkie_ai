def eval_relevance(input_conv_data):
    # 전체 미션 개수
    total_missions = len(input_conv_data["is_missions_completed"])
    
    # 달성한 미션 개수 (True로 표시된 것만 카운트)
    completed_missions = sum(input_conv_data["is_missions_completed"])

    # 달성률을 퍼센트로 계산하고 10의 자리에서 반올림
    if total_missions > 0:
        relevance_score = round((completed_missions / total_missions) * 100, -1)
    else:
        relevance_score = 0  # 미션이 없으면 0%
    
    return relevance_score