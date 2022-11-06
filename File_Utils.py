def open_file(path: str):
    f = open(path, "r", encoding="utf-8")
    content = f.read()
    f.close()
    return content


def save_file(path: str, content: str):
    f = open(path, "w", encoding="utf-8")
    f.write(content)
    f.close()
