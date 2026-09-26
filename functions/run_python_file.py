import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
):
    try:
        if args is None:
            args = []
        working_directory_abs = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

        valid_target_dir = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

        if not valid_target_dir:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not target_file.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]
        command.extend(args)
        result = subprocess.run(
            command, 
            cwd=working_directory_abs, 
            capture_output=True, 
            text=True, 
            timeout=30
        )

        output_str=""
        if result.returncode != 0:
            output_str += f"Process exited with code {result.returncode}"
        if not result.stdout and not result.stderr:
            output_str += "No output produced"
        else:
            if result.stdout:
                output_str += f"STDOUT:{result.stdout}"
            if result.stderr:
                output_str += f"STDERR:{result.stderr}"
        return output_str
    
    except Exception as e: 
        return f"Error: executing Python file: {e}"


schema_run_python_file = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Runs a python file with optional arguments and returns the output",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "Path to the python file to run relative to the working directory",
                },
                "args": {
                    "type": "array",
                    "items": {
                        "type": "string",
                    },
                    "description": "Optional command-line arguments to pass to the Python file"
                }
            },
        },
    },
}


