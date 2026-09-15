import os

def get_files_info(working_directory: str, directory: str = ".") -> str:

    working_directory_abs = os.path.abspath(working_directory)
    target_dir = os.path.normpath(os.path.join(working_directory_abs, directory))

    valid_target_dir = os.path.commonpath([working_directory_abs, target_dir]) == working_directory_abs

    if not valid_target_dir:
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    if not os.path.isdir(target_dir):
        return f'Error: "{directory}" is not a directory'

    for i in target_dir:


    return f'Success: "{directory}" is within the working directory'
