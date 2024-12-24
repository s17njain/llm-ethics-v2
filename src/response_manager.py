import json
import random
from .open_ai_manager import get_response_from_open_ai

def fetch_responses(prompts):
    responses_json = {}
    responses = []
    shuffled_prompts = prompts["prompts"]
    random.shuffle(shuffled_prompts)
    for prompt in shuffled_prompts:
        response = {}
        response["prompt_identifier"] = prompt.get("prompt_identifier")
        response["dilemma_identifier"] = prompt.get("dilemma_identifier")
        prompt_text = prompt.get("prompt")
        response_schema = prompt.get("response_schema")
        open_ai_response = get_response_from_open_ai(prompt_text, response_schema)
        response["response"] = json.loads(open_ai_response)
        responses.append(response)
    responses_json["responses"] = responses
    return responses_json
