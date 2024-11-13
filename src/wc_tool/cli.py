import click

from wc_tool import wc


@click.command()
@click.option("-c", "--bytes", "bytes_flag", is_flag=True, help="print the byte counts")
@click.option("-l", "--lines", is_flag=True, help="print the newline counts")
@click.option("-w", "--words", is_flag=True, help="print the word count")
@click.option("-m", "--chars", is_flag=True, help="print the character counts")
@click.argument("file_paths", required=False, nargs=-1)
def main(bytes_flag, lines, words, chars, file_paths):
    """
    Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.  A word is a non-zero-length sequence of characters delimited by white space.

    With no FILE, or when FILE is -, read standard input.
    """
    # Initialize totals

    (
        total_number_of_bytes,
        total_number_of_lines,
        total_number_of_words,
        total_number_of_chars,
    ) = (0, 0, 0, 0)

    if not file_paths or (file_paths == ("-",)):
        content = wc.read_file()

        click.echo(f"{output(content, lines, words, bytes_flag, chars)}")
    else:
        for file in file_paths:
            content = wc.read_file(file)

            if isinstance(content, Exception):
                number_of_lines, number_of_words, number_of_bytes, number_of_chars = (
                    0,
                    0,
                    0,
                    0,
                )
                click.echo(content)
            else:
                (
                    number_of_lines,
                    number_of_words,
                    number_of_bytes,
                    number_of_chars,
                ) = content
                click.echo(f"{output(content, lines, words, bytes_flag, chars)} {file}")

            total_number_of_lines += number_of_lines
            total_number_of_words += number_of_words
            total_number_of_bytes += number_of_bytes
            total_number_of_chars += number_of_chars

    if len(file_paths) > 1:
        totals = (
            total_number_of_lines,
            total_number_of_words,
            total_number_of_bytes,
            total_number_of_chars,
        )
        click.echo(f"{output(totals, lines, words, bytes_flag, chars)} total")


def output(content_count, lines, words, bytes_flag, chars):
    # Handle default flags when none are specified
    if not any([lines, words, bytes_flag, chars]):
        lines, words, bytes_flag = True, True, True

    line_str = f"{content_count[0]:>6} " * lines
    word_str = f"{content_count[1]:>6} " * words
    byte_str = f"{content_count[2]:>6} " * bytes_flag
    char_str = f"{content_count[3]:>6} " * chars

    return f"{line_str}{word_str}{byte_str}{char_str}"


if __name__ == "__main__":
    main()
