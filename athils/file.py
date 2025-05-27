def file_ends_with_newline(filename):
    with open(filename, 'rb') as f:
        try:
            f.seek(-1, 2)  # Go to the last byte of the file
            return f.read(1) == b'\n'
        except OSError:  # Handle empty files
            return False