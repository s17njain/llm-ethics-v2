# LLM-Ethics-v2
Designed to assess ethical reasoning capablilites of LLMs.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/s17njain/llm-ethics-v2.git
   ```
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. To run the project and interact with the GPT-4 API, you'll need to store your OpenAI API key securely in a .env file.
   ```bash
   OPENAI_API_KEY=your_api_key_here
   ```
## Usage
1. Save your dilemmas in JSON format.
2. To generate prompts in JSON format:
   ```bash
   python main.py generate_prompts --input path/to/dilemmas.json --output path/where/to/save/prompts.json
   ```
3. To prompt the model and collect responses:
   ```bash
   python main.py get_responses --input path/to/prompts.json --output path/where/to/save/responses.json
   ```

## Initial Results
### Distribution of Answer (Yes/No) by Dilemma Context
![Distribution of Answer (Yes/No) by Dilemma Context](https://github.com/user-attachments/assets/9441e0b7-3f40-4e70-ba50-f93abd99dca4)

### Distribution of Ethical Framework (Deontology/Utilitarianism) by Dilemma Context
![Distribution of Ethical Framework (Deontology/Utilitarianism) by Dilemma Context](https://github.com/user-attachments/assets/721a1183-e513-4a28-bc6b-73f1653f3c3e)
