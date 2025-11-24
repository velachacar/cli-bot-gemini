import os
from google.genai import types

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    try:
        abs_wd = os.path.abspath(working_directory)
        full_path = os.path.join(abs_wd, file_path)
        abs_full = os.path.abspath(full_path)

        if os.path.commonpath([abs_wd, abs_full]) != abs_wd:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(abs_full):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        
        with open(abs_full, 'r') as f:
            file_content = f.read(MAX_CHARS)
            if len(file_content) >= 10000:
                file_content+= f'[...File "{file_path}" truncated at 10000 characters]'
            return file_content

    except Exception as e:
        return f'Error: {e}'
    
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Gets a file content from the specified directory, limited to 10000 characters plus a disclaimer, constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path to read from, relative to the working directory.",
            ),
        },
        required=["file_path"]
    ),
)