import argparse
import datetime
from utils.file_io import *
from src.prompt_manager import create_prompts
from src.response_manager import fetch_responses

def generate_prompts(input_file = None, output_file = None):
    default_input_file = "data/dilemmas.json"
    if(input_file == None):
        print(f"No input file is specified. Fallback to default: {default_input_file}")
    dilemmas = load_input_from_json_file(default_input_file if input_file == None else input_file)
    if dilemmas:
        print("Processing dilemmas...")
        prompts_json = create_prompts(dilemmas)
        if prompts_json:
            print("Prompts generated! Saving...")
            default_output_file = "data/prompts.json"
            if(output_file == None):
                print(f"No output file is specified. Fallback to default: {default_output_file}")
            write_output_to_json_file(prompts_json, default_output_file if output_file == None else output_file)
        else:
            print("No prompts!")
    else:
        print("No dilemmas to process!")

def get_responses(input_file = None, output_file = None):
    default_input_file = "data/prompts.json"
    if(input_file == None):
        print(f"No input file is specified. Fallback to default: {default_input_file}")
    prompts = load_input_from_json_file(default_input_file if input_file == None else input_file)
    if prompts:
        print("Processing prompts...")
        responses_json = fetch_responses(prompts)
        if responses_json:
            print("Responses received! Saving...")
            current_time = datetime.datetime.now()
            formatted_time = current_time.strftime("%Y%m%d_%H%M%S")
            default_output_file = f"data/responses_{formatted_time}.json"
            if(output_file == None):
                print(f"No output file is specified. Fallback to default: {default_output_file}")
            write_output_to_json_file(responses_json, default_output_file if output_file == None else output_file)
        else:
            print("No responses received!")
    else:
        print("No prompts to process!")

def main():
    parser = argparse.ArgumentParser(description = "Pick a step to proceed with")
    parser.add_argument("step", choices = ["generate_prompts", "get_responses"], help = "The step to proceed with")
    parser.add_argument("--input", type = str, help = "Path to the input json file")
    parser.add_argument("--output", type = str, help = "Path to the output json file")
    args = parser.parse_args()
    if args.step == "generate_prompts":
        generate_prompts()
    elif args.step == "get_responses":
        get_responses(args.input, args.output)

if __name__ == "__main__":
    main()
