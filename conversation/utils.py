from .models import StartConv, ContinueConv, TerminateConv

def format_script(script: str, input_data: dict) -> str:

    return script.format(
        scenario=input_data['scenario'],
        background=input_data['background'],
        # role_of_ai=input_data['role_of_ai'],
        missions=input_data['missions'],
        dialogue=input_data['dialogue']
    )

def get_response_format(status):
    if status == "start_conversation":
        return StartConv
    elif status == "continue_conversation":
        return ContinueConv
    elif status == "terminate_conversation":
        return TerminateConv
