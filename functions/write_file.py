import os

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
    

    
