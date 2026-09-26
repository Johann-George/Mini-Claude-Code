import os

def write_file(working_directory: str, file_path: str, content: str) -> str:

    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

    valid_target_dir = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

    if not valid_target_dir:
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory' 

    if os.path.isdir(target_file):
        return f'Error: Cannot write to "{file_path}" as it is a directory'

    parent_dir = os.path.dirname(target_file)
    os.makedirs(parent_dir, exist_ok=True)

    with open(target_file, "w") as file: 
        file.write(content)

    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


schema_write_file = {
    "type": "function",
    "function": {
        "name": "write_file",
        "description": "Writes contents to a specified file relative to the working directory",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the file to write relative to the working directory",
                },
                "content": {
                    "type": "string",
                    "description": "The content to write to the file",
                },
            },
        },
    },
}
