import os

def get_files_info(working_directory, directory="."):
    try:
        abs_wd = os.path.abspath(working_directory)
        full_path = os.path.join(abs_wd, directory)
        abs_full = os.path.abspath(full_path)

        if os.path.commonpath([abs_wd, abs_full]) != abs_wd:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(abs_full):
            return f'Error: "{directory}" is not a directory'
        
        dir_contents = []
        
        for name in os.listdir(abs_full):
            entry_path = os.path.join(abs_full, name)
            is_dir = os.path.isdir(entry_path)
            size = os.path.getsize(entry_path)
            dir_contents.append(f'- {name}: file_size={size} bytes, is_dir={is_dir}')
        return '\n'.join(dir_contents)

    except Exception as e:
        return f'Error: {e}'


