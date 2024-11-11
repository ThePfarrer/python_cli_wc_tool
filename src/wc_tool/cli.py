import click

from .wc import count_bytes, count_lines


@click.command()
@click.option("-c", "--bytees", is_flag=True, help="print the byte counts")
@click.option("-l", "--lines", is_flag=True, help="print the newline counts")
@click.option("-w", "--words", is_flag=True, help="print the word count")
@click.option("-m", "--chars", is_flag=True, help="print the character counts")
@click.argument("file_path")
def main(bytees, lines, words, chars, file_path):
    """
    Print newline, word, and byte counts for each FILE, and a total line if more than one FILE is specified.  A word is a non-zero-length sequence of characters delimited by white space.

    With no FILE, or when FILE is -, read standard input.
    """
    if bytees:
        number_of_bytes = count_bytes(file_path)
        click.echo(number_of_bytes)
    elif lines:
        number_of_lines = count_lines(file_path)
        click.echo(number_of_lines)
    pass


# def process_input()
if __name__ == "__main__":
    main()
