import os
from google.genai import types

def write_file(working_directory, file_path, content):
    try:
        abs_wd = os.path.abspath(working_directory)
        full_path = os.path.join(abs_wd, file_path)
        abs_full = os.path.abspath(full_path)

        if os.path.commonpath([abs_wd, abs_full]) != abs_wd:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        os.makedirs(os.path.dirname(abs_full), exist_ok=True)
        
        with open(abs_full, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'

    except Exception as e:
        return f'Error: {e}'
    
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes into a file in the specified directory, creating it if it doesnt exist, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to write into, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content intended to be written inside the file path.",
            ),
        },
        required=["file_path", "content"]
    ),
)
