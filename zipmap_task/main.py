def zipmap(keys, values):
    dict = {}
    if len(keys) == 0 or len(values) == 0:
        return {}
    dict = zipmap(keys[1:], values[1:])
    dict[keys[0]] = values[0]
    return dict
    