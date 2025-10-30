import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT
from functions.get_files_info import schema_get_files_info
from functions.get_file_content import schema_get_file_content
from functions.write_file import schema_write_file
from functions.run_python_file import schema_run_python_file
from functions.call_function import call_function

def main():
    load_dotenv()
    api_key = os.environ.get('GEMINI_API_KEY')
    client = genai.Client(api_key=api_key)
    args = sys.argv[1:]
    verbose = False

    if '--verbose' in args:
        args.remove('--verbose')
        verbose = True
    
    if len(args):
        user_prompt = sys.argv[1]

        available_functions = types.Tool(
            function_declarations=[
                schema_get_files_info,
                schema_get_file_content,
                schema_write_file,
                schema_run_python_file
            ]
        )

        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]

        response = client.models.generate_content(
            model='gemini-2.0-flash-001',
            contents=messages,
            config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT),
        )


        

    else:
        print('incorrect arguments')
        sys.exit(1)

    if(verbose):
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    if response.function_calls:
            for function_call_part in response.function_calls:
                print(f"Calling function: {function_call_part.name}({function_call_part.args})")
                function_call_result = call_function(function_call_part, verbose)
                response = function_call_result.parts[0].function_response.response
                if not response:
                    raise Exception("Error: no tool response")
                else:
                    if verbose:
                        print(f"-> {response}")

                

    else:
        print(response.text)

    
if __name__ == "__main__":
    main()
