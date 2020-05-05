import json


def to_string(key, value, sign=' '):
    return '  {} {}: {}'.format(sign, key, value)


def generate_diff(path1, path2):
    old = json.load(open(path1))
    new = json.load(open(path2))

    result = ['{']

    # new_keys = set(new.keys()) - set(old.keys())

    for key, value in old.items():
        if key in new and value == new[key]:
            result.append(to_string(key, value))
        elif key in new:
            result.append(to_string(key, value, '-'))
            result.append(to_string(key, new[key], '+'))
        else:
            result.append(to_string(key, value, '-'))

    for key, value in new.items():
        if key not in old:
            result.append(to_string(key, value, '+'))

    result.append('}')

    return '\n'.join(result)
