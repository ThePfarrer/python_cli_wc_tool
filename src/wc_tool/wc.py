import fileinput
import locale
import sys


def read_file(file_path=None):
    """
    Reads a file or standard input and calculates line, word, byte, and character counts.
    :param file_path: The path of the file to read. If None, reads from stdin.
    :return: A tuple with counts (line_count, word_count, byte_count, char_count) or an error.
    """
    # Handle reading from stdin with optional parameters
    sys.argv[1:] = sys.argv[1:] if file_path else []

    word_count = byte_count = char_count = line_count = 0
    encoding = locale.getpreferredencoding().lower()

    try:
        with fileinput.input(files=file_path, mode="rb") as file:
            for line_count, line in enumerate(file, 1):
                word_count += len(line.split())
                byte_count += len(line)
                char_count += len(line.decode(encoding))

            return line_count, word_count, byte_count, char_count

    except FileNotFoundError:
        return FileNotFoundError(f"pywc: {file_path}: No such file or directory")
    except IOError:
        return IOError(f"pywc: {file_path}: There was an issue reading the file")
