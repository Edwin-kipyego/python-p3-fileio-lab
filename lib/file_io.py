# lib/file_io.py

def write_file(file_name, file_content):
    with open(f"{file_name}.txt", "w") as file:
        file.write(file_content)

def append_file(file_name, append_content):
    file_path = f"{file_name}.txt"
    try:
        with open(file_path, "r") as file:
            existing_content = file.read()
        needs_newline = len(existing_content) > 0
    except FileNotFoundError:
        needs_newline = False

    with open(file_path, "a") as file:
        if needs_newline:
            file.write("\n" + append_content)
        else:
            file.write(append_content)

def read_file(file_name):
    with open(f"{file_name}.txt", "r") as file:
        return file.read()