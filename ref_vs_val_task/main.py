import copy

def add_format(default_formats, new_format):
    new_formats = copy.deepcopy(default_formats)
    new_formats[new_format] = True
    return new_formats


def remove_format(default_formats, old_format):
    new_formats = copy.deepcopy(default_formats)
    new_formats[old_format] = False
    return new_formats