import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path, args=[]):
    try:
        abs_wd = os.path.abspath(working_directory)
        full_path = os.path.join(abs_wd, file_path)
        abs_full = os.path.abspath(full_path)

        if os.path.commonpath([abs_wd, abs_full]) != abs_wd:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.exists(abs_full):
            return f'Error: File "{file_path}" not found.'
        if not file_path.endswith('.py'):
            return f'Error: "{file_path}" is not a Python file.'
        
        completed = subprocess.run(
            ['python', abs_full] + args, 
            cwd=abs_wd, 
            capture_output=True, 
            timeout=30, 
            text=True
        )

        if not completed.stdout and not completed.stderr:
            return 'No output produced.'
        
        msg = f'STDOUT: {completed.stdout}STDERR: {completed.stderr}'

        if completed.returncode != 0:
            msg += f'Process exited with code {completed.returncode}'
        
        return msg
    except Exception as e:
        return f'Error: executing Python file: {e}'
    
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file from the specified directory, capturing STDOUT and STDERR, has a 30 second timeout, and constrained to the working directory.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The file path where the .py file is, relative to the working directory.",
            ),
            "args": types.Schema(
                type=types.Type.ARRAY,
                items=types.Schema(type=types.Type.STRING),
                description="Optional arguments to run",
            ),
        },
        required=["file_path"],
    ),
)
    