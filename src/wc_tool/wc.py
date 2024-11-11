import sys


def read_file(file_path=None, flag="r"):
    try:
        chunk_size = 1024
        if file_path:
            with open(file_path, flag) as file:
                while chunk := file.read(chunk_size):
                    yield chunk
        else:
            while chunk := sys.stdin.read(chunk_size):
                yield chunk

    except FileNotFoundError:
        yield FileNotFoundError(f"pywc: {file_path}: No such file or directory")
    except IOError:
        yield IOError(f"pywc: {file_path}: There was an issue reading the file")


def count_bytes(file_path):
    count = 0
    file_content = read_file(file_path, "rb")
    for content in file_content:
        if isinstance(content, Exception):
            return content
        else:
            count += len(content)

    return f"{count} {file_path}"


def count_lines(file_path):
    count = 0
    file_content = read_file(file_path, "r")
    for content in file_content:
        if isinstance(content, Exception):
            return content
        else:
            count += content.count("\n")

    return f"{count} {file_path}"
