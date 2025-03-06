from openai import OpenAI
from .config import OPENAI_API_KEY, OPENAI_MODEL, OPENAI_DEVELOPER_ROLE_CONTENT

client = OpenAI(
    api_key = OPENAI_API_KEY
)

def get_response_from_open_ai(prompt, response_schema):
    try:
        completion = client.chat.completions.create(
            model = OPENAI_MODEL,
            messages = [
                {"role": "developer", "content": OPENAI_DEVELOPER_ROLE_CONTENT},
                {"role": "user", "content": prompt}
            ],
            response_format = response_schema
        )
        response = completion.choices[0].message.content
        return response
    except Exception as e:
        print(f"Error extracting response: {e}")
        return {}
