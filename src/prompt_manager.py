import json
import random
import itertools
from .config import BASE_PROMPT, ANSWER_OPTIONS, SELF_REFLECTION_OPTIONS, ANSWER_PROPERTY, REASONING_PROPERTY, SELF_REFLECTION_PROPERTY, PROPERTIES, RESPONSE_SCHEMA

def get_perm_for_answer_options():
    return list(itertools.permutations(ANSWER_OPTIONS))

def get_perm_for_self_reflection_options():
    return list(itertools.permutations(SELF_REFLECTION_OPTIONS))

def get_answer_prop_with_answer_options():
    answer_options = get_perm_for_answer_options()
    return [ANSWER_PROPERTY.format(answer_options = json.dumps(answer_option)) for answer_option in answer_options]

def get_reasoning_prop():
    return [REASONING_PROPERTY]

def get_self_reflection_prop_with_self_reflection_options():
    self_reflection_options = get_perm_for_self_reflection_options()
    return [SELF_REFLECTION_PROPERTY.format(self_reflection_options = json.dumps(self_reflection_option)) for self_reflection_option in self_reflection_options]

def get_all_possible_response_schemas():
    response_schemas = []
    answer_property = get_answer_prop_with_answer_options()
    reasoning_property = get_reasoning_prop()
    self_reflection_property = get_self_reflection_prop_with_self_reflection_options()
    for perm in itertools.permutations([answer_property, reasoning_property, self_reflection_property], 3):
        for prop_1 in perm[0]:
            for prop_2 in perm[1]:
                for prop_3 in perm[2]:
                    response_schemas.append(RESPONSE_SCHEMA.format(properties = PROPERTIES.format(property_1 = prop_1, property_2 = prop_2, property_3 = prop_3)))
    return response_schemas

def create_prompts(dilemmas):
    prompts_json = {}
    prompts = []
    prompt_id = 1
    response_schemas = get_all_possible_response_schemas()
    shuffled_dilemmas = dilemmas["dilemmas"]
    random.shuffle(shuffled_dilemmas)
    for dilemma in shuffled_dilemmas:
        dilemma_identifier = dilemma.get("dilemma_identifier")
        dilemma_text = dilemma.get("dilemma")
        for response_schema in response_schemas:
            prompt = {}
            prompt["prompt_identifier"] = f"prompt_{prompt_id}"
            prompt["dilemma_identifier"] = dilemma_identifier
            prompt["prompt"] = BASE_PROMPT.format(dilemma = dilemma_text)
            prompt["response_schema"] = json.loads(response_schema)
            prompts.append(prompt)
            prompt_id += 1
    prompts_json["prompts"] = prompts
    return prompts_json
