def doc_format_checker_and_converter(conversion_function, valid_formats):
    def inner_func(filename, content):
        filename_split = filename.split('.')
        filename_format = filename_split[-1]
        if filename_format in valid_formats:
            return conversion_function(content)
        else:
            raise ValueError("Invalid file format")
    return inner_func

# Don't edit below this line


def capitalize_content(content):
    return content.upper()


def reverse_content(content):
    return content[::-1]