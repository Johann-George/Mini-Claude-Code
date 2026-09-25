def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
):
    working_directory_abs = os.path.abspath(working_directory)
    target_file = os.path.normpath(os.path.join(working_directory_abs, file_path))

    valid_target_dir = os.path.commonpath([working_directory_abs, target_file]) == working_directory_abs

    if not valid_target_dir:
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    if not os.path.isfile(target_file):
        return f'Error: "{file_path}" does not exist or is not a regular file'

    if target_file[:-2] != ".py":
        return f'Error: "{file_path}" is not a Python file'

    command = ["python", target_file]
    command.extend(args)
    subprocess.run()




