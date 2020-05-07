from .loader import load_files


def to_str(key, value, sign=' '):
    if type(value) == bool:
        value = str(value).lower()
    return '  {} {}: {}'.format(sign, key, value)


def generate_diff(path1, path2):
    old, new = load_files(path1, path2)

    result = [
        to_str(k, v) if v == new.get(k)
        else to_str(k, v, '-') + '\n' + to_str(k, new[k], '+') if k in new
        else to_str(k, v, '-')
        for k, v in old.items()
        ]

    result = result + [
        to_str(k, v, '+')
        for k, v in new.items()
        if k not in old
        ]

    result = ['{'] + result + ['}']

    # result = ['{']

    # new_keys = set(new.keys()) - set(old.keys())

    # for key, value in old.items():
    #     if key in new and value == new[key]:
    #         result.append(to_string(key, value))
    #     elif key in new:
    #         result.append(to_string(key, value, '-'))
    #         result.append(to_string(key, new[key], '+'))
    #     else:
    #         result.append(to_string(key, value, '-'))
    #
    # for key, value in new.items():
    #     if key not in old:
    #         result.append(to_string(key, value, '+'))

    # result.append('}')

    return '\n'.join(result)
