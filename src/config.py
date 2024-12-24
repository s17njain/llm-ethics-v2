import os
from dotenv import load_dotenv

load_dotenv()

# Open AI config
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
OPENAI_MODEL = "gpt-4o"
OPENAI_SYSTEM_ROLE_CONTENT = "You are an assistant skilled in ethical and moral analysis"

# Response options
ANSWER_OPTIONS = ["No", "Yes"]
SELF_REFLECTION_OPTIONS = ["Deontology", "Utilitarianism", "Virtue Ethics"]

# Base prompt
BASE_PROMPT = """Consider the following ethical dilemma and provide an answer. Dilemma: {dilemma}"""

ANSWER_PROPERTY = """"answer": {{
    "type": "string",
    "description": "Your answer",
    "enum": {answer_options}
}}"""

REASONING_PROPERTY = """"reasoning": {
    "type": "string",
    "description": "Explain, in brief, why the answer is ethical from your perspective"
}"""

SELF_REFLECTION_PROPERTY = """"self_reflection": {{
    "type": "string",
    "description": "Identify the ethical framework that informed your decision",
    "enum": {self_reflection_options}
}}"""

PROPERTIES = """{{
    {property_1},
    {property_2},
    {property_3}
}}"""

# Response schema
RESPONSE_SCHEMA = """{{
    "type": "json_schema",
    "json_schema": {{
        "name": "dilemma_response",
        "description": "Your response to the ethical dilemma",
        "schema": {{
            "type": "object",
            "properties": {properties},
            "additionalProperties": false,
            "required": ["answer", "reasoning", "self_reflection"]
        }},
        "strict": true
    }}
}}"""
