import json


def generate_diff(path1, path2):
    def to_string(key, value, sign=' '):
        return '  {} {}: {}'.format(sign, key, value)

    old = json.load(open(path1))
    new = json.load(open(path2))

    result = ['{']

    new_keys = set(new.keys()) - set(old.keys())

    for key, value in old.items():
        if key in new:
            if value == new[key]:
                result.append(to_string(key, value))
            else:
                result.append(to_string(key, value, '-'))
                result.append(to_string(key, new[key], '+'))
        else:
            result.append(to_string(key, value, '-'))

    for key in new_keys:
        result.append(to_string(key, new[key], '+'))

    result.append('}')

    return '\n'.join(result)
