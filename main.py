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
        for i in range(20):
            try:
                response = client.models.generate_content(
                    model='gemini-2.0-flash-001',
                    contents=messages,
                    config=types.GenerateContentConfig(tools=[available_functions], system_instruction=SYSTEM_PROMPT),
                )
                is_called_tool = False

                for candidate in response.candidates:
                    messages.append(candidate.content)

                    fn_calls = [p for p in candidate.content.parts if getattr(p, "function_call", None)]
                    for fn_call in fn_calls:
                        is_called_tool = True
                        call_obj = fn_call.function_call
                        fn_call_result = call_function(call_obj, verbose)

                        fn_response = fn_call_result.parts[0].function_response
                        if not fn_response or not fn_response.response:
                            raise Exception("Error: no tool response")

                        messages.append(
                            types.Content(role="user", parts=[types.Part(function_response=fn_response)])
                        )
                        
                        if verbose:
                            print(f"-> {fn_response.response}")
                
                if not is_called_tool and response.text:
                    print("Final response:")
                    print(response.text)
                    break
            except Exception as e:
                if verbose:
                    print(f"Error: {e}")
                break
            

        

    else:
        print('incorrect arguments')
        sys.exit(1)

    if verbose:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

if __name__ == "__main__":
    main()
