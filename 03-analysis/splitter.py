# A line splitting generator courtesy of GollyJer by Stackoverflow
# https://stackoverflow.com/questions/52787585/how-to-efficiently-read-a-large-file-with-a-custom-newline-character-using-pytho
def line_splitter(file, newline, chunk_size=4096):
    tail = ''
    while True:
        chunk = file.read(chunk_size).decode(encoding="utf-8")
        if not chunk:
            if tail:
                yield tail
            break
        lines = chunk.split(newline)
        tail = (tail + lines[0]).split(newline)
        if len(tail) > 1:
            lines[0] = tail[1]
        else:
            del lines[0]
        tail = tail[0]
        if lines:
            yield tail
            tail = lines.pop()
            yield from lines
