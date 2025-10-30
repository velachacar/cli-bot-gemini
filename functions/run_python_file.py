import os
import subprocess

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
    