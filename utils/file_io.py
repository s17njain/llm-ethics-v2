import json

def load_input_from_json_file(input_file):
    try:
        print(f"Reading input from {input_file}")
        with open(input_file, 'r') as f:
            input = json.load(f)
        return input
    except FileNotFoundError:
        print(f"Error: File not found at {input_file}")
        return None
    except Exception as e:
        print(f"Error reading JSON file: {e}")
        return None

def write_output_to_json_file(responses, output_file):
    try:
        with open(output_file, 'w', encoding = "utf-8") as f:
            json.dump(responses, f, ensure_ascii = False, indent = 4)
        print(f"Output saved to {output_file}")
    except IOError as e:
        print(f"Error writing to file: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
