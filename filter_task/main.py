def remove_invalid_lines(document):
    # lines = document.splitlines(True)
    # for line in lines:
    #     if line.startswith("-"):
    #         lines.remove(line)
    return "\n".join(filter(lambda x: not x.startswith("-"), document.split("\n")))
