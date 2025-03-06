import json
from tqdm import tqdm
from .open_ai_manager import get_response_from_open_ai

def fetch_responses(prompts):
    responses_json = {}
    responses = []
    prompts = prompts["prompts"]
    with tqdm(total = len(prompts)) as pbar:
        for prompt in prompts:
            response = {}
            response["prompt_identifier"] = prompt.get("prompt_identifier")
            response["dilemma_identifier"] = prompt.get("dilemma_identifier")
            prompt_text = prompt.get("prompt")
            response_schema = prompt.get("response_schema")
            open_ai_response = get_response_from_open_ai(prompt_text, response_schema)
            response["response"] = json.loads(open_ai_response)
            responses.append(response)
            pbar.update(1)
    responses_json["responses"] = responses
    return responses_json
