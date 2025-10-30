import os
from google.genai import types
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file

def call_function(function_call_part, verbose=False):
    
    print(function_call_part.name)
    function_dict = {
                     "get_files_info": get_files_info, 
                     "get_file_content": get_file_content,
                     "write_file": write_file,
                     "run_python_file": run_python_file,
                    }
    
    wd_plus_args = {"working_directory":"./calculator", **function_call_part.args}

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    if function_call_part.name not in function_dict:
        return types.Content(
          role="tool",
          parts=[
              types.Part.from_function_response(
                  name=function_call_part.name,
                  response={"error": f"Unknown function: {function_call_part.name}"},
              )
          ],
        )
    else:
        func = function_dict[function_call_part.name]
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"result": func(**wd_plus_args)},
                )
            ],
)



    
